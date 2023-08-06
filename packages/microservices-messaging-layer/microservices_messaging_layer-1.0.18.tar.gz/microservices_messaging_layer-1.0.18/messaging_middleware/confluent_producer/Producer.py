# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-07-03
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# =============================================================================
#
# Produce  messages from Confluent Cloud
# Using Confluent Python Client for Apache Kafka
#
# =============================================================================

import json
import logging
import os
import sys
from confluent_kafka import Producer
from ..utils.filesystem import get_project_root


class ConfluentProducer:

    def __init__(self, *args, **kwargs):
        self.__servers = kwargs.get('servers', None)
        self.topic = kwargs.get('topic', None)
        self.security_protocol = kwargs.get('security_protocol', 'plaintext')
        self.ssl_ca_location = kwargs.get('ssl_ca_location', './configuration/cacert.pem')

        # -- for CCLOUD --
        # mechanisms = PLAIN for CCLOUD
        self.sasl_mechanisms = kwargs.get('sasl_mechanisms', None)
        self.sasl_username = kwargs.get('sasl_username', None)
        self.sasl_password = kwargs.get('sasl_password', None)
        self.basic_auth_credentials_source = kwargs.get('basic_auth_credentials_source', None)
        self.basic_auth_user_info = kwargs.get('basic_auth_user_info', None)
        # -----------------
        if not self.topic:
            sys.stderr.write('%% Topic name not specified: \n')
            raise ValueError("Topic name not specified")
        logging.basicConfig(
            format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
            level=logging.ERROR
        )
        logging.getLogger('kafka').setLevel(logging.INFO)
        if self.basic_auth_user_info is not None:
            producer_conf = {'bootstrap.servers': self.__servers,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location,
                             'sasl.mechanisms': self.sasl_mechanisms,
                             'sasl.username': self.sasl_username,
                             'sasl.password': self.sasl_password

                             }
        else:
            producer_conf = {'bootstrap.servers': self.__servers,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location

                             }

        # Create MsgProducer instance
        self.producer = Producer(**producer_conf)

    def _get_basic_auth_credentials(self):
        """
        the BASIC AUTH credentials are store as USERNAME:PASSWORD
        """
        try:
            username = self.basic_auth_user_info.split(':')[0]
            password = self.basic_auth_user_info.split(':')[1]
            return username, password
        except Exception as error:
            print("EXCEPTION getting BASIC AUTH credentials:", error)
            return 0

    def _delivery_callback(self, err, msg):
        if err:
            sys.stderr.write("Failed to deliver message: {}".format(err))
        else:

            sys.stderr.write("Produced record to topic {} partition [{}] @ offset {}"
                             .format(msg.topic(), msg.partition(), msg.offset()))

    def produce_message(self, **kwargs):
        message = kwargs.get('message', None)
        try:
            self.producer.produce(self.topic, value=json.dumps(message), callback=self._delivery_callback)
            self.producer.poll(0)
            self.producer.flush()
            return {"topic": self.topic, "sent": True}
        except BufferError as e:
            sys.stderr.write('%% Local producer queue is full ' \
                             '(%d messages awaiting delivery): try again\n' %
                             len(self.producer))
            return 0