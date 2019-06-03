import python_mqtt_estg as mqtt
import python_i2c_estg as i2c


def on_publish(client, userdata, result):  # create function for callback
    print("Published")


i2c.


mqtt.publish("localhost", 1883, "default/topic", "Test Message", "Client Name 2", on_publish)
