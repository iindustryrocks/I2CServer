import pigpio
import time
import os

pi = None
slave_addr = 0x04

print("Listening...")


def i2cInterrupt(id, tick):
    global pi
    global slave_addr
    status, bytes_read, data = pi.bsc_i2c(slave_addr)  # pi.bsc_i2c(slave_addr, data=" ACK")
    if bytes_read:
        if data == "OK":
            print("Message:")
            print(data[:-1])


pi = pigpio.pi()  # inicia a conexao
int_handler = pi.event_callback(pigpio.EVENT_BSC, i2cInterrupt)
pi.bsc_i2c(slave_addr)
time.sleep(500)
int_handler.cancel()
pi.bsc_i2c(0)
pi.stop()
