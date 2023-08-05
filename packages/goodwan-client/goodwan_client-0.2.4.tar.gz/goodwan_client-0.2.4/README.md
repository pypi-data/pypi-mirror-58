# GoodWan python client

GoodWan IoT python client

## Getting Started

```python
import datetime

from goodwan_client import Client


# Use system/pytz timezone name e.g. Europe/Moscow 
client = Client("login", "password", "timezone")

t_from = datetime.datetime(2019, 1, 1, 0, 0, 0)
t_to = datetime.datetime(2019, 3, 1, 23, 59, 59)
events = client.events(t_from=t_from, t_to=t_to)

# events is a list of goodwan_client.event.Event class
for event in events:
    print(event)
    
"""
<goodwan_client.event.Event id_event=123123123, id_system=0, id_transmitter=123, 
 data_type=101, data=2525.0, data_ext=0.0, signal_lvl=0, 
 timestamp=2019-02-28 05:15:22+03:00, 
 device=<goodwan_client.devices.TempSensor data=2525.0, data_ext=0.0, temp=2525.0>,
 device_name=temp_sensor
>
"""
```

For more info, see classes goodwan_client.event.Event and goodwan_client.devices.*


### Prerequisites

- Python >= 3.5


### Installing

```bash
pip install goodwan_client
```
## Authors

* **Dmitry Konovalov** - *Initial work* - [kanavis](http://www.kanavis.pw)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
