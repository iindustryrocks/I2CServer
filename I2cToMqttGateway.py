import python_i2c_estg as i2c
import python_mqtt_estg as mqtt


def message_handler(client, userdata, i2c_message, cenas):
    print(i2c_message)
    mqtt.publish(message=i2c_message)


i2c.connect(0x04, message_handler, True)
