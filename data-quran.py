import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

# Procedures
#
# 1. Get the data from Splash
# 2. Make soup out of content
# 3. Find all 'media-body' class which contains data
# 4. Loop the data structure as stack using while
# 5. Get the text from pop()
# 6. Use function format_data to format the text insert the result to the
#	 front of the temp_queues
# 7. Loop over the queues and get the items data
# 8. Store result on key/value as number/data 
# 9. Open a json file and write dumps out to file
# 10. Dumps the json result with indentation and sorted keys

def format_data(s):
	"""Format the data given by media-body texts into a usable form

	Args:
		s (string): text from media-body
	
	Returns:
		tuples of (surah_name, num_in_order, translation)
	"""
	s = s.replace(" (", ", ").replace(")", ", ").split(", ")

	return tuple(s)


if __name__ == "__main__":
	data = OrderedDict()
	temp_queues = []

	# 1
	r = requests.get('http://localhost:8050/render.html?url=https://quran.kemenag.go.id/&timeout=10&wait=0.5')

	# 2
	soup = BeautifulSoup(r.content, 'html.parser')

	# 3
	body_data = soup.find_all("div", "media-body")

	# 4
	while body_data:
		# 5
		text = body_data.pop().get_text()

		# 6
		temp_queues.insert(0, format_data(text))


	for i, item in enumerate(temp_queues):
		# 7
		name, ayat, translation = item

		# 8
		data[i + 1] = { "nama_surat": name, "arti_surat": translation, "ayat": ayat }

	# 9
	with open("data_quran.json", "w") as f:
		
		# 10
		json.dump(data, f, indent=4)
