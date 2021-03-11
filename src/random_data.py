from datetime import datetime
import time
import numpy as np

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "JmcahFWa2q2eRjI1Vmkos51vSeot_IPz1-gZ3a3z2wHu1AaubxYge3it7IjB_Q79D3RY0Ikz4Xe7pCiBu1glig=="
org = "Falkreath-Hold"
bucket = "TestBucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)


# Write: Option 1
write_api = client.write_api(write_options=SYNCHRONOUS)

for i in range(50):
    data = f"mem,host=host1 used_percent={30 * np.random.rand()}"
    write_api.write(bucket, org, data)
    time.sleep(0.25)

# Write: Option 2
# point = Point("mem")\\
#  .tag("host", "host1")\\
#  .field("used_percent", 23.43234543)\\
#  .time(datetime.utcnow(), WritePrecision.NS)

#write_api.write(bucket, org, point)


# Write: Option 3
#sequence = ["mem,host=host1 used_percent=23.43234543",
#            "mem,host=host1 available_percent=15.856523"]
#write_api.write(bucket, org, sequence)


# Query
# query = f'from(bucket: \\"{bucket}\\") |> range(start: -1h)'
# tables = client.query_api().query(query, org=org)
