import paho.mqtt.client as mqtt

broker_address = "localhost"
port = 1883


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


client1 = mqtt.Client("test1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.connect(broker_address, port)  # establish connection
ret = client1.publish("mqtt/sample", "hello")