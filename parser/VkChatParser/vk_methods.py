import requests
import copy
from vk_api.keyboard import VkKeyboardColor,  VkKeyboard
import constants
import json
import time 
import os

def responseErrorHandler(func):
	def handler(self):
		response = func(self)
		if 'failed' in response:
			if int(response['ts']) != int(self.ts):
				# Если номер ts неправильный, то мы берем ts, который вернул сервер вместе с ошибкой
				self.ts = int(response['ts'])
			else:
				#обновляем ключ для запроса к серверу
				self.KEY = constants.key_extraction()
		return response
	return handler

class VKBot():
	def __init__(self):

		self.SERVER = constants.SERVER
		self.URL = constants.URL
		self.KEY = constants.KEY
		self.TOKEN = constants.TOKEN
		self.ts = 1

		self._commands = [
								'Начать логирование',
								'Остановить'
		]

	def checkForEvent(self, response):
		if len(response['updates']) > 0:
			self.ts += 1
			if response['updates'][0]['type'] == 'message_new':
				if response['updates'][0]['object']['message']['text'].capitalize() == self._commands[0]:
					self.sendMessage(self.getUsrId(response), 'Чтобы остановить бота нажмите кнопку', self.getPollingBoard())
					self.startPolling()
				else:
					self.sendMessage(self.getChatId(response), "Нажмите на кнопку, чтобы начать работу бота", self.getMainMenuBoard())

	def sendMessage(self, chat_id, text='', board=None):
		message = requests.post(self.URL + 'messages.send?peer_id={}&random_id=0&message={}&keyboard={}&access_token={}&v=5.110'.format(chat_id, text, board.get_keyboard(), self.TOKEN)); 
		self.ts += 1
		print(f'[{time.ctime()}] Отправлен ответ на сообщение пользователя id' + str(chat_id) + ', ответ сервера: {}'.format(message.json()), '\n')
		return message

	def getChatId(self, response):
		try:
			return response['updates'][0]['object']['message']['peer_id']
		except KeyError:
			return None

	def getUsrId(self, response):
		try:
			return response['updates'][0]['object']['message']['from_id']
		except KeyError:
			return None

	def getMainMenuBoard(self):
		bot_keyboard = VkKeyboard(one_time=True, inline=False)
		bot_keyboard.add_button(self._commands[0], color=VkKeyboardColor.PRIMARY)
		return bot_keyboard

	def getPollingBoard(self):
		bot_keyboard = VkKeyboard(one_time=True, inline=False)
		bot_keyboard.add_button(self._commands[1], color=VkKeyboardColor.NEGATIVE)
		return bot_keyboard

	def startPolling(self):
		message = '' 
		json_data = []
		
		while message.capitalize() != self._commands[1]:
			response = self.sendResponse()
			data = {
				'user':{
					'name': '',
					'avatar': ''
				},

				'message': {
					'type': '',
					'img': '',
					'text': ''
				}
			} 
			if ('updates' in response.keys()):
				if len(response['updates']):
					if response['updates'][0]['type'] == 'message_new':
						self.ts += 1
						message = response['updates'][0]['object']['message']['text']
						user_data = requests.get(self.URL + 'users.get?access_token={}&name_case=nom&user_ids={}&fields=photo&v=5.110'.format(self.TOKEN, self.getUsrId(response))).json()
						user_data = user_data['response'][0]
						data['user']['name'] = user_data['first_name'] + ' ' + user_data['last_name']
						data['user']['avatar'] = user_data['photo'] 



						if len(response['updates'][0]['object']['message']['attachments']):
							###########????
							try:
								data['message']['text'] = response['updates'][0]['object']['message']['attachments'][0]['photo']['text'],
								data['message']['img'] = response['updates'][0]['object']['message']['attachments'][0]['photo']['sizes'][0]['url'],
								data['message']['type'] = 'photo'
							except:
								pass
						else:
							data['message']['text'] = message
							data['message']['type'] = 'message'

						with open(os.getcwd()+r"\..\..\view\src\logs.json", 'w') as f:
							json_data.append(copy.deepcopy(data))
							try:
								while len(json_data) > 10:
									json_data.pop(0);
								json.dump(json_data, f, indent=4)
								f.close()
								self.sendMessage(self.getChatId(response), ' ', self.getPollingBoard())
							except:
								f.close()

	@responseErrorHandler
	def sendResponse(self):
		response = requests.get(f'{self.SERVER}?act=a_check&key={self.KEY}&wait=5&ts={self.ts}').json()
		print(f'[{time.ctime()}] Отправлен запрос на сервер, ответ сервера: {response}')
		return response
	
	def run(self):
		run = True

		while run:
			resp = self.sendResponse()
			if 'failed' not in resp:
				self.checkForEvent(resp) 


