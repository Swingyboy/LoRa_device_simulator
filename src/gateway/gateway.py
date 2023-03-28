from __future__ import annotations

import time

from threading import Thread
from typing import TYPE_CHECKING

from src.common import MqttManager, BrokerConfigs

if TYPE_CHECKING:
    from src.common import AbstractMqttManager


GATEWAY_TO_DEVICE_TOPIC = "device/rx"
DEVICE_TO_GATEWAY_TOPIC = "device/tx"


class Gateway:
    def __init__(self, local_mqtt_conf: BrokerConfigs) -> None:
        self._to_device_topic = [GATEWAY_TO_DEVICE_TOPIC]
        self._from_device_topic = [DEVICE_TO_GATEWAY_TOPIC]
        self._device_mqtt_manager: AbstractMqttManager = MqttManager(
            local_mqtt_conf,
            pub_topics=self._to_device_topic,
            sub_topics=self._from_device_topic
        )

    def _start_device_listening(self):
        self._device_mqtt_manager.start()

    def _start_downlink_loop(self):
        while True:
            self._device_mqtt_manager.publish("Test Gateway message")
            time.sleep(20)

    def _start_ns_listening(self):
        ...

    def run(self):
        Thread(target=self._start_device_listening).start()
        Thread(target=self._start_ns_listening).start()
