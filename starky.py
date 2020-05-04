import requests
from requests.exceptions import ConnectionError

#https://stackoverflow.com/a/58937394/13033981
def retry_on_connectionerror(f, max_retries=5):
	retries = 0
	while retries < max_retries:
		try:
			return f()
		except ConnectionError:
			retries += 1
		raise Exception("Maximum retries exceeded")

def removebg(file,API):
	response = requests.post(
	'https://api.remove.bg/v1.0/removebg',
	files={'image_file': open(f'{file}', 'rb')},
	data={'size': 'auto'},
	headers={'X-Api-Key': f'{API}'},
	)
	print('working....')
	if response.status_code == 200:
		with open('no-bg.png', 'wb') as out:
			out.write(response.content)
	else:
		print("Error:", response.status_code, response.text)


#retry_on_connectionerror(removebg(FILE, API))

def urbandictionary(word):
	url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
	querystring = {"term":"f{word}"}

	headers = {
	'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
	'x-rapidapi-key': ""
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)

#urbandictionary('test')