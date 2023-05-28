import obsws_python as obs

class OBS_API():
    eventManager = obs.EventClient()

    def __init__(self) -> None:
        self._running = False
        self._client = None
        self.eventManager.callback.register(
            [
                self.OnSceneCreated
            ]
        )

    def Connect(self, host: str, port: int, password: str):
        self._client = obs.ReqClient(host=host, port=port, password=password)
        self._running = True

    def OnSceneCreated(self, data):
        """A new scene has been created."""
        print(f"scene {data.scene_name} has been created")

    def GetObjOnTheScreen(self):
        pass

    def GetCurrentScene(self):
        return self._client.get_current_program_scene()

    def Render(self, currentScreen, object):
        self._client.create_scene_item(currentScreen.name, object)

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
obsClient.Connect('localhost', 4455, '8jbzwYaiZtAUFTit')
#obsClient.Render(obsClient.GetCurrentScene(), '<p>asdasd</p>')
