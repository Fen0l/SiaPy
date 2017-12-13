from SiaPy import Client
import json

client = Client(endpoint="127.0.0.1:9980", force_discover=True, auth_key="OmZvb2Jhcg==")

# Delete gateway
# client.post("/gateway/disconnect/178.32.103.208:9981")

To unlock the wallet
params = {}
params['encryptionpassword'] = ""
client.post("/wallet/unlock", params)


# Setup host
params = {
	'acceptingcontracts': False,
	'maxduration': 25920
}
client.post("/host", params)

info_host = client.get("/host").text
print(info_host)

# Disconnect gateways when the version is below 1.3.x
result = client.get("/gateway").text
gateways = json.loads(result)
for gateway in gateways['peers']:
	if gateway['version'] < '1.3.0':
		client.post("/gateway/disconnect/{netaddress}".format(netaddress = gateway['netaddress']))