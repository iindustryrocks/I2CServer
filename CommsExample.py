# pip install git+https://github.com/iindustryrocks/PythonComms@master
import python_i2c_estg as i2c
import python_mqtt_estg as mqtt


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_publish(client, userdata, result):  # create function for callback
    print("Published")


mqtt.subscribe("localhost", 1883, "default/topic", "Client name", on_message)
mqtt.publish("localhost", 1883, "default/topic", "Test Message", "Client Name 2", on_publish)
