import obsws_python as obs

class OBS_API():
    screen = None

    def __init__(self) -> None:
        pass

    def connect(self, host: str, port: int, password: str):
        client = obs.ReqClient(host=host, port=port, password=password)
        print(client.create_scene("MyNewScene"))

    def getObjOnTheScreen(self):
        pass

    def render(self, currentScreen, object):
        #obs.obs_enter_graphics()
        #obs.obs_leave_graphics()
        pass

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
obsClient.connect('26.234.129.130', 4455, '8jbzwYaiZtAUFTit')
