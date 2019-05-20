import python_mqtt_estg as mqtt


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


mqtt.subscribe("localhost", 1883, "default/topic", "Client name", on_message)

while True:
    cenas = ""

