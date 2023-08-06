# Sixgill Client

This module provides a simple Sixgill Darkfeed & Alerts API clients written in Python.

# Sixgill's client arguments
1. client_id        (Mandatory) - Your client id obtained by Sixgill’s Developer portal, 
2. client_secret    (Mandatory) - Your client secret obtained by Sixgill’s Developer portal, 
3. channel_code     (Mandatory) - Supported Sixgill channel code. If you don't have such a code please contact Sixgill's support (support@cybersixgill.com). 
4. logger           (Optional)  - Logger.
5. bulk_size        (Optional)  - requests bulk size, default 1000 items. 

## Quick Example
```
from sixgill.sixgill_darkfeed_client import SixgillDarkFeedClient
from sixgill.sixgill_alert_client import SixgillAlertClient
 
CLIENT_ID = "<Replace with your client id>"
CLIENT_SECRET = "<Replace with your client secret>"
CHANNEL_CODE = "<Replace with channel code>"

sixgill_darkfeed_client = SixgillDarkFeedClient(CLIENT_ID, CLIENT_SECRET, CHANNEL_CODE)

for incident in sixgill_darkfeed_client.get_incidents():
    sixgill_darkfeed_client.mark_digested_item(incident)
    print(incident)

sixgill_alert_client = SixgillAlertClient(CLIENT_ID, CLIENT_SECRET, CHANNEL_CODE)

for alert in sixgill_alert_client.get_alerts():
    sixgill_alert_client.mark_digested_item(alert)
    print(alert)
    
```