from machine import Pin

motor_a_fw = Pin(18, Pin.OUT)
motor_a_bk = Pin(19, Pin.OUT)
motor_b_fw = Pin(20, Pin.OUT)
motor_b_bk = Pin(21, Pin.OUT)

def read_html():
    text_file = open("html.htm", "r")
    data = text_file.read()
    text_file.close()
    return data

def move_forward():
    print("moving forward")
    motor_a_fw.value(1)
    motor_b_fw.value(1)
    motor_a_bk.value(0)
    motor_b_bk.value(0)
    
def move_left():
    print("moving left")
    motor_a_fw.value(1)
    motor_b_fw.value(0)
    motor_a_bk.value(0)
    motor_b_bk.value(1)

def stop_motors():
    print("stop motors")
    motor_a_fw.value(0)
    motor_b_fw.value(0)
    motor_a_bk.value(0)
    motor_b_bk.value(0)

def move_right():
    print("moving right")
    motor_a_fw.value(0)
    motor_b_fw.value(1)
    motor_a_bk.value(1)
    motor_b_bk.value(0)

def move_back():
    print("moving back")
    motor_a_fw.value(0)
    motor_b_fw.value(0)
    motor_a_bk.value(1)
    motor_b_bk.value(1)

async def serve_client(reader, writer):
    stop_motors()
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)

    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass

    request = str(request_line)
    forward = request.find('/motor/forward')
    left = request.find('/motor/left')
    stop = request.find('/motor/stop')
    right = request.find('/motor/right')
    back = request.find('/motor/back')

    if forward == 6:
        move_forward()

    if left == 6:
        move_left()

    if stop == 6:
        stop_motors()

    if right == 6:
        move_right()

    if back == 6:
        move_back()

    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(read_html())

    await writer.drain()
    await writer.wait_closed()
    print("Client disconnected")