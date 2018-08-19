from pyspider.libs.base_handler import *
import codecs
import logging
import json

class Handler(BaseHandler):
    crawl_config = {
    }

    logging.basicConfig(level = logging.INFO)

    #client = KafkaClient(hosts = "192.168.0.101:9092",zookeeper_hosts="192.168.0.101:2181")

    #生产kafka数据，通过字符串形式
    #def produce_kafka_data(kafka_topic,result):
        #with kafka_topic.get_producer(delivery_reports=True) as producer:
             #type(json.dump(result))
             #producer.produce(json.dump(result))

    def on_result(self, result):
        topic = self.client.topics["gakki"]
        print(result)
       # self.produce_kafka_data(topic,result)
        #存入mongoDb

    #@every(minutes=24 * 60)
    def on_start(self):
        for x in range(1, 5):
            self.crawl('https://m.weibo.cn/api/container/getIndex?containerid=1076031882811994&page=%d' % x, callback=self.json_parser,validate_cert=False
                       )

    def json_parser(self, response):
        return [{ "card": x
                  } for x in response.json['data']['cards']]

