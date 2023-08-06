## DS1631 module

This pure python module provides a raspberry pi i2c interface for Maxim-Dallas DS1621 DS1631 DS1631A DS1721 DS1731 high-precision digital thermometer and thermostat.

### Datasheets

- [DS1631-DS1731](https://datasheets.maximintegrated.com/en/ds/DS1631-DS1731.pdf)
- [DS1621](https://datasheets.maximintegrated.com/en/ds/DS1621.pdf)
- [DS1721](https://datasheets.maximintegrated.com/en/ds/DS1721.pdf)

### 2-wire serial data bus

DS1631s are connected to Raspberry pi i2c GPIO (8 devices max) with 4 wires :

- SDA i2c bus (GPIO2)
- SCL i2c bus (GPIO3)
- Power (3.3 V or 5 V)
- Ground

### Basic usage

Raspberry pi : OS Raspbian  

First, you need python 3 ```smbus``` module :  

```
sudo apt install python3-smbus
```

#### DS1631 device simple example

```python
import DS1631
import time

i2c_address = 0x48
ic1 = DS1631.DS1631(1, i2c_address)
# thermostat config
ic1.set_tout_polarity("active-low")
ic1.set_thigh(22.5)
ic1.set_tlow(20.5)
# thermometer config
ic1.set_conversion_mode("continuous")
ic1.set_resolution(12)
ic1.start_convert()
# read temperature
while True:
    time.sleep(0.75)
    temperature = ic1.get_temperature()
    print("Temperature  : {} °C".format(temperature))
```

#### Virtual device simple example

```DS1631``` module provides a ```DS1631virtualdevice``` class for development without raspberry pi or DS1631s devices.

On–Off controller (hysteresis controller) simulation is performed :  

+ if temperature > thigh then electric radiator OFF
+ if temperature < tlow then electric radiator ON

Of course, you don't need python 3 ```smbus``` module, so you can work with a Windows OS computer or Android OS device (pydroid3).

```python
import DS1631
import time

# virtual device
room = DS1631.DS1631virtualdevice(initial_temperature=18,
                                  thigh=20, tlow=19,
                                  P=1000, R=0.02,
                                  tau=360,
                                  Text_max=15,Text_min=10,
                                  period=24*3600)
while True:
    time.sleep(0.75)
    temperature = room.get_temperature()
    print("Temperature  : {} °C".format(temperature))
```
