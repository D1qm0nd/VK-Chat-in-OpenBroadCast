from vk_methods import VKBot

bot = VKBot()

if __name__ == '__main__':
	bot.run()

'''
while True:
	last_time = time.time()

	if int(response['ts']) > int(ts):
			ts = int(response['ts'])

	response = requests.get(f'{SERVER}?act=a_check&key={KEY}&wait=5&ts={ts}').json()
	print(f'[{time.ctime()}] Отправлен запрос на сервер, ответ сервера: {response}')

	if 'failed' in response:
		print('[{}] Произошла ошибка код ошибки - {}\n'.format(time.ctime(), response['failed']))
		time.sleep(120)

	if new_time > 599:
		KEY = constants.key_extraction()
		new_time = 0
	new_time += time.time() - last_time

	if bot.check_for_event(response):
		bot.main_menu(response)
'''

#{
#"response": {
#"key": "b884bca91605270cf31d9a4e34164fa7f77a71b3",
#"server": "https://lp.vk.com/wh192318642",
#"ts": "1"
#}
#}

#https://lp.vk.com/wh192318642?act=a_check&key=b884bca91605270cf31d9a4e34164fa7f77a71b3&wait=25&ts=2

#https://api.vk.com/method/groups.getLongPollServer?group_id=192318642&access_token=54fb9edb6b2325c6334ed5b913bb7f920cf726885ddfdb5285b345c606d48d856ea59dc6b30b2b81a9236&v=5.110

#{
#	'inline':'true',
#	'buttons':[
#				[
#					{	'action':{
#									'type':'text',
#									'payload':'"{\"button\":\"4\"}"',
#									'label':'Уровни'
#								}
#						'color':'primary'
#					}
#				]
#			]
#}









