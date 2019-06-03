import pigpio
import time
import os

message_protocol = {
    "0" : "Up",
    "1" : "Down",
    "2" : "Right",
    "3" : "Left",
    "4" : "Enter"
}

pi = None
slave_addr = 0x04

print ("Listening")

def i2cInterrupt(id, tick):
   global pi
   global slave_addr

   status, bytes_read, data = pi.bsc_i2c(slave_addr)

   if bytes_read:
      print(data)
      for byte in data:
         print(message_protocol[byte])

pi = pigpio.pi()
int_handler = pi.event_callback(pigpio.EVENT_BSC, i2cInterrupt)
pi.bsc_i2c(slave_addr)

time.sleep(500)

int_handler.cancel()
pi.bsc_i2c(0)
pi.stop()