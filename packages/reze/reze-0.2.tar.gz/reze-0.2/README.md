# Reze
A Python client for easy use of the Reze recommendation API.

If you don't have an account at Reze yet, you can create a free account [here](http://103.116.100.241:8000)

## Installation

Install the client with pip:

> pip install reze

(use pip3 instead of pip if you use Python 3)

## Examples

```python
# import
from reze.api_client import RezeClient
from reze.api_requests import SalebotAddInteraction, SalebotBoughtTogether, SalebotItemsToItem

app_id = "your_app_id"
app_key = "your_key"
server_url = "current_reze_api_server"

client = RezeClient(app_id, app_key, server_url)

# Send the data to Reze
request_add_interaction = SalebotAddInteraction(1, "tag_content", 1, "VIEW")
print(client.send(request_add_interaction))

# Get recommendations
request_bought_together = SalebotBoughtTogether("bô")
recommended_bought_together = client.send(request_bought_together)
print("Bought together items: ")
for tag in recommended_bought_together['data']:
    print(tag['tag'])

# Get recommendations
request_items_to_item = SalebotItemsToItem("bô")
recommended_items_to_item = client.send(request_items_to_item)
print("Recommended items to item: ")
for tag in recommended_items_to_item['data']:
    print(tag['tag'])
```