from datetime import datetime
import pytz
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = pytz.timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(pytz.timezone('Asia/Kolkata'))
print(bang_d)

print('*'*50)
from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
