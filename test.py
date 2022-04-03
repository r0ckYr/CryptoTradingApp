#!/usr/bin/env python3
from wazirx_sapi_client.rest import Client
import time

# public
client = Client()
print(client.send("ping"))
print(client.send("time"))
print(client.send("system_status"))
#print(client.send("exchange_info"))

# private
api_key = "YOUR_API_KEY"
secret_key = "YOUR_SECRET_KEY"

client = Client(api_key=api_key, secret_key=secret_key)

#print(client.send("historical_trades",
#{"limit": 10, "symbol": "btcinr", "recvWindow": 10000, "timestamp": int(time.time() * 1000)}
 #            ))

print(client.send('create_order',
             {"symbol": "btcinr", "side": "buy", "type": "limit", "price": 50, "quantity": 1, "recvWindow": 10000,
              "timestamp": int(time.time() * 1000)}))
