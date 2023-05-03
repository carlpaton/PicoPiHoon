import uasyncio as asyncio
from machine import Pin

onboard = Pin("LED", Pin.OUT, value=0)

async def boot_led():   
    onboard.off()
    boot_show = 3
    wait_for = 0.3
    while boot_show > 0:
        print(boot_show)
        onboard.on()
        await asyncio.sleep(wait_for)
        onboard.off()
        await asyncio.sleep(wait_for)
        boot_show -= 1

async def heartbeat():   
    while True:
        onboard.on()
        print("heartbeat")
        await asyncio.sleep(0.25)
        onboard.off()
        await asyncio.sleep(5)
