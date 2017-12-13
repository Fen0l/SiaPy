# (SiaPy) Unofficial Python wrapper for the siad API

[![Sia Logo](http://sia.tech/img/svg/sia-green-logo.svg)](http://sia.tech)

Sia is a new decentralized cloud storage platform that radically alters the landscape of cloud storage. By leveraging smart contracts, client-side encryption, and sophisticated redundancy (via Reed-Solomon codes), Sia allows users to safely store their data with hosts that they do not know or trust. The result is a cloud storage marketplace where hosts compete to offer the best service at the lowest price. And since there is no barrier to entry for hosts, anyone with spare storage capacity can join the network and start making money.

### Currently under development


Installation
============

The python wrapper works with Python 2.6+ and Python 3.2+.

The easiest way to get the latest stable release is to grab it from `the repository <git@github.com:Fen0l/SiaPy.git>` himself using ``git``.

.. code:: bash

    git clone git@github.com:Fen0l/SiaPy.git
    pip install -r requirements.txt

Or for Python3.2+

.. code:: bash

    git clone git@github.com:Fen0l/SiaPy.git
    pi3 install -r requirements.txt

Example Usage
=============

```python
from SiaPy import Client
import json

# Connect to the siad API (force_discover will automaticaly try to discover the daemon)
client = Client(endpoint="127.0.0.1:9980", force_discover=True, auth_key="mykey")

# Unlock the wallet
params = {}
params['encryptionpassword'] = "words words words words"
client.post("/wallet/unlock", params)

# Get information about our host
host = client.get("/host")
print(json.loads(host.text))

# Disconnect gateways when the version is below 1.3.x
result = client.get("/gateway").text
gateways = json.loads(result)
for gateway in gateways['peers']:
	if gateway['version'] < '1.3.0':
		client.post("/gateway/disconnect/{netaddress}".format(netaddress = gateway['netaddress']))

```

All endpoint are listed [on their GitHub](https://github.com/NebulousLabs/Sia/blob/master/doc/API.md)


Next steps
 * Read from config file
 * Create local fnc for each endpoint
 * ...


