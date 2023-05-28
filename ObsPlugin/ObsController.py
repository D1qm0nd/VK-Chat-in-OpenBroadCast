from asyncio.windows_events import NULL
import obspython as obs

class OBS_API():
    screen = NULL

    def __init__(self) -> None:
        pass

    def getObjOnTheScreen(self):
        pass

    def render(self, currentScreen, object):
        pass


#Добавляет описание к скрипту в OBS
def script_description():
            return """<center><h2>ChatAvtomat v2.0</h2></center>
            <p>Customized chat output from Telegram to OBS (don't forget to reassign)</p>"""

def script_defaults(settings):
    pass

def script_load(settings):
    pass

def script_update(settings):
    pass

def script_tick(seconds):
    pass

obsClient = OBS_API()
script_description()