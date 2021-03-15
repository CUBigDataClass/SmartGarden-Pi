import serial
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

device = '/dev/ttyUSB0'
brate = 115200
brate = 9600
print('here')
arduino = serial.Serial(device, brate, timeout=10)
print(arduino.name)

# You can generate a Token from the "Tokens Tab" in the UI
token = "JmcahFWa2q2eRjI1Vmkos51vSeot_IPz1-gZ3a3z2wHu1AaubxYge3it7IjB_Q79D3RY0Ikz4Xe7pCiBu1glig=="
org = "Falkreath-Hold"
bucket = "TestBucket"

client = InfluxDBClient(url="http://10.10.8.1:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    line = arduino.readline().decode('utf-8').strip()
    data = line.split(':')
    if len(data) == 2:
        data = f"{data[0]},host=host1 value={float(data[1])}"
        write_api.write(bucket, org, data)
        # time.sleep(0.25)
        print(f'wrote: {data}')
    else:
        print(f'unexpected line format: {line}')
