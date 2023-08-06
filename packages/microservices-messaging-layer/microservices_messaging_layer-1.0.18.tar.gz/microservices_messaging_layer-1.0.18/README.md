# Messaging Layer for Microservices 



![](http://www.italiamappe.it/mappa/ImmaginiVetrine/0000106274/Immagine1lrg.jpg)


```json
     _ _          _       _                     
    | (_)        | |     (_)                    
  __| |_ ___  ___| | __ _ _ _ __ ___   ___ _ __ 
 / _` | / __|/ __| |/ _` | | '_ ` _ \ / _ \ '__|
| (_| | \__ \ (__| | (_| | | | | | | |  __/ |   
 \__,_|_|___/\___|_|\__,_|_|_| |_| |_|\___|_|   
                                                
                                                
```

This service is in his early age. **DO NOT USE in production** or if you want to, please be aware you are going to use a piece of code which probably will be
changed or improved ( and not necessarily in this order) soon and very often. You have been warned!
This service requires at least another service listening to a few KAFKA topics.

# Service description


This service provides microservices with an universal communication layer based on KAFKA messages.
It provides two kind of Producer. One based on KAFKA and the other one based on the Confluent KAFKA version. 



# Required ENV variables 

* brokers=mybroker1:9093,mybroker2:9093,mybroker3:9093
* monitoring_topic=tcservicesmonitor

If you are using AVRO you must have 
* schema_registry=https://my_avro_schema_registry:8081


# How to use it 

### PLAIN TEXT connection

```python
from messaging_middleware.avro_communication_layer.Producer import Producer
producer = Producer(bootstrap_servers="your broker list here",
                                 schema_reqistry_url="your schema registry here",topic='mytopic')

        
producer.produce_message(
            value={your json message here},
            key={your key schema here}, callback=my_callback_function)



```
### SSL configuration 


in order to connect to brokers using the SSL protocol, we need to pass the following kwargs to consumers/producers configuration 


```python
from messaging_middleware.avro_communication_layer.Consumer import Consumer as AvroConsumer
from messaging_middleware.avro_communication_layer.Producer import Producer as AvroProducer

if __name__ == "__main__":
    c = AvroConsumer(
        bootstrap_servers="sslbroker:29080",
        security_protocoll='ssl', consumer_topic='my-topic')

    p = AvroProducer(
        bootstrap_servers="sslbroker:29080",
        security_protocoll='ssl', topic='my-topic')
```


## Integrated Logging System 

By default, the Logger is connected to the following ENV variables 

* brokers=mybroker:202021,mybroker2:202019
* schema_registry="https://sksk:8081"
* monitoring_topic=tcservicesmonitor

```python
from messaging_middleware.utils.logger import Logger

logger = Logger()


```