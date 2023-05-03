# Hello World

Turning on the built in LED :D ... exciting stuff!

## Gotach!

https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf

> "The on-board LED on Raspberry Pi Pico is connected to GPIO pin 25, whereas on Raspberry Pi Pico W it is connected to the wireless chip." 

This means for the `Pi Pico W` you use

```
from machine import Pin
led = Pin("LED", Pin.OUT)
led.toggle()
```

And for the `Pi Pico` you use

```
from machine import Pin
led = Pin(25, Pin.OUT)
led.toggle()
```

- https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5
- 