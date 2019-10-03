import json
import requests
from collections import OrderedDict
import time

# Procedures
#
# 1. Load data_quran.json data, deserialize it into OrderedDict
# 2. Loop over the OrderedDict
# 3. Do API access to get the data
# 4. Embed the data onto the OrderedDict
# 5. Sleep the api request calls :)
# 6. Dump the data into a new json data

if __name__ == "__main__":
	with open('data_quran.json', 'r') as f:
		# 1
		od = json.load(f, object_pairs_hook=OrderedDict)
		
	# 2
	for k, v in od.items():
		# logging helper
		print(f"{k} - {v['nama_surat']}")

		# 3
		api_data = requests.get(f"https://quran.kemenag.go.id/index.php/api/v1/ayatweb/{k}/0/0/500")

		# 4
		v["data_ayat"] = OrderedDict(api_data.json())

		# 5
		time.sleep(3)



	# 6
	with open("data_surat.json", "w") as f:
		json.dump(od, f, indent=4)