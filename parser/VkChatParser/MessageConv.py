from abc import ABC, abstractclassmethod
from typing import Dict


class DataConvert(ABC):
	@abstractclassmethod
	def Convert():
		pass

	@

class MessageTransfer():
    def __init__(self) -> None:
    pass

class MessageConverter(DataConvert): 
    def __init__(self) -> None:
        self.msgTranf = MessageTransfer()
        self.dataTraforet = {
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
            

    def Convert(self, ata: Dict):
