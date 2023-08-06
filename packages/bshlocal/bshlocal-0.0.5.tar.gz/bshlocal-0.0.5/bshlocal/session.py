import typing
import logging
import threading
import time
import sys

from .api import BSHLocalAPI, JSONRPCError
from .device import BSHLocalDevice
from .room import BSHLocalRoom
from .services_impl import SUPPORTED_DEVICE_SERVICE_IDS

logger = logging.getLogger("bshlocal")


class BSHLocalSession:
    def __init__(self, controller_ip: str, certificate, key):
        # API
        self._api = BSHLocalAPI(controller_ip=controller_ip, certificate=certificate, key=key)

        # Subscription status
        self._poll_id = None

        # All devices
        self._rooms_by_id = {}
        self._devices_by_id = {}

        self._enumerate_devices()
        self._enumerate_rooms()

        self._polling_thread = None
        self._stop_polling_thread = False

    def _enumerate_devices(self):
        raw_devices = self._api.get_devices()
        for raw_device in raw_devices:
            device_id = raw_device['id']

            if set(raw_device['deviceServiceIds']).isdisjoint(SUPPORTED_DEVICE_SERVICE_IDS):
                logger.info(f"Skipping device id {device_id} which has no services that are supported by this library")
                continue

            device = BSHLocalDevice(api=self._api, raw_device=raw_device)
            self._devices_by_id[device_id] = device

    def _enumerate_rooms(self):
        raw_rooms = self._api.get_rooms()
        for raw_room in raw_rooms:
            room_id = raw_room["id"]
            room = BSHLocalRoom(api=self._api, raw_room=raw_room)
            self._rooms_by_id[room_id] = room

    def _long_poll(self, wait_seconds=30):
        if self._poll_id is None:
            self._poll_id = self.api.long_polling_subscribe()
            logger.debug(f"Subscribed for long poll. Poll id: {self._poll_id}")
        try:
            raw_results = self.api.long_polling_poll(self._poll_id, wait_seconds)
            for raw_result in raw_results:
                self._process_long_polling_poll_result(raw_result)

            return True
        except JSONRPCError as json_rpc_error:
            if json_rpc_error.code == -32001:
                self._poll_id = None
                logger.warning(f"SHC claims unknown poll id. Invalidating poll id and trying resubscribe next time...")
                return False
            else:
                raise json_rpc_error

    def _maybe_unsubscribe(self):
        if self._poll_id is not None:
            self.api.long_polling_unsubscribe(self._poll_id)

    def _process_long_polling_poll_result(self, raw_result):
        assert raw_result["@type"] == "DeviceServiceData"
        device_id = raw_result["deviceId"]
        if device_id in self._devices_by_id.keys():
            device = self._devices_by_id[device_id]
            device.process_long_polling_poll_result(raw_result)
        else:
            logger.debug(f"Skipping polling result with unknown device id {device_id}.")

    def start_polling(self):
        if self._polling_thread is None:
            def polling_thread_main():
                while not self._stop_polling_thread:
                    try:
                        if not self._long_poll():
                            logging.warning("_long_poll returned False. Waiting 1 second.")
                            time.sleep(1.0)
                    except RuntimeError as err:
                        if self._stop_polling_thread:
                            logging.info("Stopping polling thread after expected runtime error.")
                            return
                        else:
                            logging.error(f"Runtime error in running polling thread: {err}. Waiting 15 seconds.")
                            time.sleep(15.0)
                    except Exception as ex:
                        logging.error(f"Error in polling thread: {ex}. Waiting 15 seconds.")
                        time.sleep(15.0)

            self._polling_thread = threading.Thread(target=polling_thread_main, name="BSHLocalPollingThread")
            self._polling_thread.start()

        else:
            raise ValueError("Already polling!")

    def stop_polling(self):
        if self._polling_thread is not None:
            self._stop_polling_thread = True
            self._polling_thread.join()

            self._maybe_unsubscribe()
            self._polling_thread = None
        else:
            raise ValueError("Not polling!")

    @property
    def devices(self) -> typing.Sequence[BSHLocalDevice]:
        return list(self._devices_by_id.values())

    def device(self, device_id) -> BSHLocalDevice:
        return self._devices_by_id[device_id]

    @property
    def rooms(self) -> typing.Sequence[BSHLocalRoom]:
        return list(self._rooms_by_id.values())

    def room(self, room_id) -> BSHLocalRoom:
        return self._rooms_by_id[room_id]

    @property
    def api(self):
        return self._api
