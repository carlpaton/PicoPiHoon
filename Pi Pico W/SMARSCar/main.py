import uasyncio as asyncio

from myboot import boot_led, heartbeat
from mynetwork import connect_to_network
from myclient import serve_client

async def main():
    print('Boot...')
    await boot_led()
    
    print('Connecting to Network...')
    connect_to_network()

    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    await heartbeat()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()






