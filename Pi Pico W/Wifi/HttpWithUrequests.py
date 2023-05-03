# It is much simpler to use the urequests library to make an HTTP connection.

# Connect to network
import network
from mywifi import networksetting

ssid, password = networksetting()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print(wlan.status()) # 3 == success

# Make GET request
import urequests
response = urequests.get("http://date.jsontest.com")
print(response.status_code)
print(response.content)
print(response.json())


# You must close the returned response object after making a request using the urequests library using
#response.close(). If you do not, the object will not be garbage-collected, and if the request is being made inside a loop
#this will quickly lead to a crash.

response.close()