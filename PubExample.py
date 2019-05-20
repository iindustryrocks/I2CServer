import python_mqtt_estg as mqtt


def on_publish(client, userdata, result):  # create function for callback
    print("Published")


mqtt.publish("localhost", 1883, "default/topic", "Test Message", "Client Name 2", on_publish)
