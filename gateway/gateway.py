from __future__ import annotations

import time

from dataclasses import dataclass
from threading import Thread
from typing import TYPE_CHECKING

from common.mqtt_manager import MqttManager, BrokerConfigs

if TYPE_CHECKING:
    from common.mqtt_manager import AbstractMqttManager


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

    def _send_downlink(self):
        while True:
            self._device_mqtt_manager.publish("Test Gateway message")
            time.sleep(20)

    def run(self):
        Thread(target=self._device_mqtt_manager.start).start()
        Thread(target=self._send_downlink).start()
