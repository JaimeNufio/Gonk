from datetime import datetime
from dateutil import parser

x = "2021-02-04 21:01:45.447344"
dt = parser.parse(x)

print("{}/{}/{} {}:{}".format(dt.month,dt.day,dt.year,dt.hour,dt.min))