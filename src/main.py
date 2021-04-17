import serial
import os
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

import helpers

# Ardino Setup
device = os.getenv('DEVICE_PORT', '/dev/ttyUSB0')
brate = os.getenv('BAUD_RATE', 9600)

print(f'connecting to {device} with {brate}')
arduino = serial.Serial(device, brate, timeout=10)
print(arduino.name)

# InfluxDB Setup
influx_db_host = os.environ['DB_HOST']
token = os.environ['TOKEN']
org = os.environ['ORG']
bucket = os.environ['BUCKET']

print(f'Connecting to database: {influx_db_host}, bucket: {bucket}')
client = InfluxDBClient(url=influx_db_host, token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    line = arduino.readline().decode('utf-8').strip()
    data = line.split(':')
    if len(data) == 2:
        data = f'{helpers.formatTitle(data[0])},host=host1 value={float(data[1])}'
        write_api.write(bucket, org, data)
        print(f'wrote: {data}')
    else:
        print(f'unexpected line format: {line}')
