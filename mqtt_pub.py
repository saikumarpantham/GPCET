import paho.mqtt.client as mqtt

pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com')
print('Broker Connected')

pub_client.publish('gpcet/ai','charan mg')



