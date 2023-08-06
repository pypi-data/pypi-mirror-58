# python-garminconnect
Python 3 API wrapper for Garmin Connect to get activity statistics

See https://connect.garmin.com/

## Usage
Create a new connection by supplying your user credentials
```
from garminconnect import Garmin

api = Garmin(YOUR_EMAIL, YOUR_PASSWORD)
```

Fetch your Garmin Connect activities data
```
print(api.fetch_stats())
```
