from consumers.KafkaConsumerSync import KafkaConsumerSync
from producers.KafkaProducerSync import KafkaProducerSync


kafka_consumer_sync = KafkaConsumerSync()
kafka_producer_sync = KafkaProducerSync()

kafka_producer_sync.test(n=10)
kafka_consumer_sync.test(avg_time=1, n=10)
