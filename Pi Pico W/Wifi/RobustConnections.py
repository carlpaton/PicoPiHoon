import time, network
import urequests as requests
from mywifi import networksetting

ssid, password = networksetting()
max_wait = 10

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    
while True:

    # Do things here, perhaps measure something using a sensor?

    # ...and then define the headers and payloads
    payload = {
        "name": "carl",
        "no": 123
    }
    headers = {'Content-Type':'application/json'}

    try:
        print("sending...")
        #response = requests.post("http://httpbin.org/post", headers=headers, data=payload)
        response = requests.post("http://httpbin.org/post")
        print(str(response.status_code))
        print(response.content)
        print(response.json())
        print(wlan.status())
        response.close()
    except:
        print("could not connect (status =" + str(wlan.status()) + ")")
        if wlan.status() < 0 or wlan.status() >= 3:
            print("trying to reconnect...")
            wlan.disconnect()
            wlan.connect(ssid, password)
            if wlan.status() == 3:
                print('connected in except')
            else:
                print('failed')

    time.sleep(5)