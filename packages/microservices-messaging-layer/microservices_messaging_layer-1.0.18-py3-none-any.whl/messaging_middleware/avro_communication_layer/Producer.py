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
# Produce AVRO messages from Confluent Cloud
# Using Confluent Python Client for Apache Kafka
#
# =============================================================================


from confluent_kafka.avro import AvroProducer
from avro import schema
import sys, requests, json
from confluent_kafka import Producer, KafkaError


class Producer:
    """
    Produce AVRO messages from Confluent Cloud
    """

    def __init__(self, *args, **kwargs):

        self.__servers = kwargs.get('bootstrap_servers', None)
        self.__registry = kwargs.get('schema_reqistry_url', None)
        self.topic = kwargs.get('topic', None)
        # security.protocol = SASL_SSL for CCLOUD
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

        self.debug_level = kwargs.get('debug_level', 'security')
        if not self.topic:
            sys.stderr.write('%% Topic name not specified: \n')
            raise ValueError("Topic name not specified")

        if self.basic_auth_user_info is not None:
            username, password = self._get_basic_auth_credentials()
            BASIC_AUTH = {"username": username, "password": password}
            producer_conf = {'bootstrap.servers': self.__servers,
                                      'schema.registry.url': self.__registry,
                                      'log.connection.close': 'false',
                                      'security.protocol': self.security_protocol,
                                      'ssl.ca.location': self.ssl_ca_location,
                                      'sasl.mechanisms': self.sasl_mechanisms,
                                      'sasl.username': self.sasl_username,
                                      'sasl.password': self.sasl_password,
                                      'schema.registry.basic.auth.credentials.source': self.basic_auth_credentials_source,
                                      'schema.registry.basic.auth.user.info': self.basic_auth_user_info

                                      }
        else:
            BASIC_AUTH = None
            producer_conf = {'bootstrap.servers': self.__servers,
                                      'schema.registry.url': self.__registry,
                                      'log.connection.close': 'false',
                                      'security.protocol': self.security_protocol,
                                      'ssl.ca.location': self.ssl_ca_location


                                      }
        schema_id, default_value_schema = self._find_latest_schema(topic=self.topic + "-value",
                                                                   SCHEMA_REGISTRY_URL=self.__registry,
                                                                   BASIC_AUTH=BASIC_AUTH)
        schema_id, default_key_schema = self._find_latest_schema(topic=self.topic + "-key",
                                                                 SCHEMA_REGISTRY_URL=self.__registry,
                                                                 BASIC_AUTH=BASIC_AUTH)

        # print("default_value_schema=",default_value_schema)
        # print("default_key_schema=",default_key_schema)

        self.producer = AvroProducer(producer_conf,
                                     default_key_schema=default_key_schema, default_value_schema=default_value_schema)

        self.default_value_schema = default_value_schema

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

    def _find_latest_schema(self, topic, SCHEMA_REGISTRY_URL, BASIC_AUTH=0):
        """
        This method makes two request to the SCHEMA_REGISTY in order
        to get the latest schema version of the given topic.
        The first request lists all the available versions. The second one is the one
        to get the latest schema version.
        If the BASIC_AUTH is not False means that it is a dictionary with username and password as keys.
        They are required when we work with a Confluent Cloud brokers and not with a on-premise ones
        """
        subject = topic
        try:
            if BASIC_AUTH:
                from requests.auth import HTTPBasicAuth
                versions_response = requests.get(
                    url="{}/subjects/{}/versions".format(SCHEMA_REGISTRY_URL, subject),
                    headers={
                        "Content-Type": "application/vnd.schemaregistry.v1+json"},
                    auth=HTTPBasicAuth(BASIC_AUTH.get('username', None), BASIC_AUTH.get('password', None))

                )
            else:
                versions_response = requests.get(
                    url="{}/subjects/{}/versions".format(SCHEMA_REGISTRY_URL, subject),
                    headers={
                        "Content-Type": "application/vnd.schemaregistry.v1+json",
                    },
                )
            # print("versions_response.json()=", versions_response.json())
            latest_version = versions_response.json()[-1]
            # print("latest_version=", latest_version)

            if BASIC_AUTH:
                schema_response = requests.get(
                    url="{}/subjects/{}/versions/{}".format(SCHEMA_REGISTRY_URL, subject, latest_version),
                    headers={
                        "Content-Type": "application/vnd.schemaregistry.v1+json",
                    },
                    auth=HTTPBasicAuth(BASIC_AUTH.get('username', None), BASIC_AUTH.get('password', None))
                )
            else:

                schema_response = requests.get(
                    url="{}/subjects/{}/versions/{}".format(SCHEMA_REGISTRY_URL, subject, latest_version),
                    headers={
                        "Content-Type": "application/vnd.schemaregistry.v1+json",
                    },
                )
            # print("schema_response.json()=", schema_response.json())
            schema_response_json = schema_response.json()

            return schema_response_json["id"], schema.Parse(schema_response_json.get("schema"))
        except Exception as error:
            print("EXCEPTION finding the lastest topic's verson")
            return 0

    def produce_message(self, **kwargs):

        """
            Sends message to kafka by encoding with specified avro schema
                @:param: topic: topic name
                @:param: value: An object to serialize
                @:param: key: An object to serialize
        """

        # get schemas from  kwargs if defined
        callback_function = kwargs.pop('delivery_callback', self._delivery_callback)
        value = kwargs.pop('value', None)
        key = kwargs.pop('key', None)
        try:
            self.producer.produce(topic=self.topic, value=value, key=key, callback=callback_function)
            self.producer.poll(0)
            self.producer.flush()
            return {"topic": self.topic, "value": value, "sent": True}
        except BufferError as e:
            sys.stderr.write('%% Local producer queue is full ' \
                             '(%d messages awaiting delivery): try again\n' %
                             len(self.producer))
            return 0