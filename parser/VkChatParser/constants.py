import requests

SERVER = "https://lp.vk.com//wh192318642"
URL = 'https://api.vk.com/method/'
TOKEN = "54fb9edb6b2325c6334ed5b913bb7f920cf726885ddfdb5285b345c606d48d856ea59dc6b30b2b81a9236"

def key_extraction():
	request = requests.post('https://api.vk.com/method/groups.getLongPollServer?' + 
							'group_id=192318642&access_token=' + 
							'{0}&v=5.110'.format(TOKEN)).json()
	#if not request['error']:
	return request['response']['key']
	#print(request)

KEY = key_extraction()
