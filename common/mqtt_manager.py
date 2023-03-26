from __future__ import annotations

import logging
import sys

from abc import ABC, abstractmethod
from dataclasses import dataclass
from queue import Queue
from typing import Optional, Union

from paho.mqtt import client as mqtt


LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 1883


@dataclass
class BrokerConfigs:
    host: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None


class AbstractMqttManager(ABC):

    @abstractmethod
    def __init__(self, broker_conf: Union[dict, BrokerConfigs], pub_topics: list, sub_topics: list) -> None:
        ...

    @abstractmethod
    def publish(self, message: str) -> None:
        ...

    @abstractmethod
    def start(self) -> None:
        ...


class MqttManager(AbstractMqttManager):

    def __init__(self, broker_conf: Union[dict, BrokerConfigs], pub_topics: list, sub_topics: list) -> None:
        if isinstance(broker_conf, dict):
            try:
                broker_conf = BrokerConfigs(**broker_conf)
            except TypeError as exc:
                logging.info(exc)
                logging.info(f"Using default broker configs: {LOCAL_HOST} and {LOCAL_PORT}.")
                broker_conf = BrokerConfigs(host=LOCALHOST, port=LOCAL_PORT)
        self._broker_confs = broker_conf
        self._client = mqtt.Client()
        self._recived_msg_queue = Queue()
        self._pub_topics = pub_topics
        self._sub_topics = sub_topics

        self._client.on_connect = self._on_connect
        self._client.on_disconnect = self._on_disconnect
        self._client.on_message = self._on_message

        if (self._broker_confs.username) and (self._broker_confs.password):
            self._client.username_pw_set(self._broker_confs.username, self._broker_confs.password)

    def _on_connect(self, client, userdata, flags, rc):
        if rc != 0:
            logging.debug(
                f'Impossible to connected to mqtt broker "{self._broker_confs.host}" on tcp port {self._broker_confs.port}. Result code {rc}.')
            sys.exit()
        else:
            logging.debug(
                f'connected to mqtt broker "{self._broker_confs.host}" on tcp port {self._broker_confs.port} with result code {rc}...')
        for topic in self._sub_topics:
            self._client.subscribe(topic)

    def _on_disconnect(self, client, userdata, rc):
        if rc != 0:
            logging.error(f"unexpectedly disconnected from {self._broker_info.host} with result code {rc}...")
            logging.error("stopping execution...")
            sys.exit()

    def _on_message(self, client, userdata, message):
        logging.debug(f"Recieved message {message.payload} from topic {message.topic}")
        self._recived_msg_queue.put(message.payload)

    def publish(self, msg: str) -> None:
        for topic in self._pub_topics:
            self._client.publish(topic, msg)

    def start(self) -> None:
        self._client.connect(self._broker_confs.host, self._broker_confs.port)
        self._client.loop_forever()
