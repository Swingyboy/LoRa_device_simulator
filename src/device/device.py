from __future__ import annotations

import time

from threading import Thread
from typing import TYPE_CHECKING

from src.common import MqttManager, BrokerConfigs

if TYPE_CHECKING:
    from src.common import AbstractMqttManager


GATEWAY_TO_DEVICE_TOPIC = "device/rx"
DEVICE_TO_GATEWAY_TOPIC = "device/tx"


class Device:
    def __init__(self, local_mqtt_conf: BrokerConfigs) -> None:
        self._dev_rx_topic = [GATEWAY_TO_DEVICE_TOPIC]
        self._dev_tx_topic = [DEVICE_TO_GATEWAY_TOPIC]
        self._mqtt_manager: AbstractMqttManager = MqttManager(
            local_mqtt_conf,
            pub_topics=self._dev_tx_topic,
            sub_topics=self._dev_rx_topic
        )

    def _send_uplink(self):
        while True:
            self._mqtt_manager.publish("Test Device message")
            time.sleep(30)

    def run(self):
        Thread(target=self._mqtt_manager.start).start()
        Thread(target=self._send_uplink).start()
