import confluent_kafka
import logging
from confluent_kafka import TopicPartition, KafkaException, KafkaError, OFFSET_END
from ..utils.filesystem import get_project_root


def do_assign(consumer, partitions):
    for tp in partitions:
        lo, hi = consumer.get_watermark_offsets(tp)
        if hi <= 0:
            # No previous offset (empty partition): skip to end
            tp.offset = OFFSET_END
        else:
            tp.offset = hi - 1
    consumer.assign(partitions)


class Consumer:

    def __init__(self, **kwargs):
        self.bootstrap_servers = kwargs.pop('bootstrap_servers', None)
        self.consumer_topic = kwargs.pop('consumer_topic', None)
        self.security_protocol = kwargs.pop('security_protocol','plaintext')

        self.consumer = confluent_kafka.Consumer({'bootstrap.servers': self.bootstrap_servers,
                                                  'group.id': 'grouip',
                                                  'session.timeout.ms': 6000,
                                                  'enable.auto.commit': 'false',
                                                  'log.connection.close': 'false',
                                                  'default.topic.config': {'auto.offset.reset': 'latest'},
                                                  'security.protocol': self.security_protocol
                                                  })

        self.consumer.assign(list(map(lambda p: TopicPartition(self.consumer_topic, p), range(0, 3))))
        logging.basicConfig(
            format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
            level=logging.INFO
        )
        logging.getLogger('urllib3.connectionpool').setLevel(logging.INFO)

    def stop(self):
        self.consumer.close()

    def run(self):
        pass
