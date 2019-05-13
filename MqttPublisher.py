import paho.mqtt.client as mqtt

broker_address = "localhost"
port = 1883


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


def publish(topic="default_topic", message="test", client_name="default_client"):
    publisher = mqtt.Client(client_name)  # create client object
    publisher.on_publish = on_publish  # assign function to callback
    publisher.connect(broker_address, port)  # establish connection
    publisher.publish(topic, message)
