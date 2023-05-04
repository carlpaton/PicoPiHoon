from machine import Pin

led = Pin(15, Pin.OUT)

def read_html():
    text_file = open("html.htm", "r")
    data = text_file.read()
    text_file.close()
    return data

async def serve_client(reader, writer):
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)

    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass

    request = str(request_line)
    led_on = request.find('/led/on')
    led_off = request.find('/led/off')
    print('led on = ' + str(led_on))
    print('led off = ' + str(led_off))

    if led_on == 6:
        print("led on")
        led.value(1)

    if led_off == 6:
        print("led off")
        led.value(0)

    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(read_html())

    await writer.drain()
    await writer.wait_closed()
    print("Client disconnected")