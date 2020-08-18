from TurtleEngine.Gui import *
from TurtleEngine import *
class WelcomeScreen:

    def __init__(self):
        LogErr("Here3")
        self._window = TurtleWindow.New()

        LogErr("Here4")
        self._CreateGui()

        self._window.StartDrawingCycle()
        pass

    def _CreateGui(self):
        root = self._window.GetRoot()

        newProject = Element.New()
        newProject.SetName("New project")
        newProject.SetSize(-0.5, -0.5)
        newProject.SetPosX(-0.5, -0.5)
        newProject.SetBackgroundColor(200, 200, 200, 255)
        root.AddElement(newProject)

        openRecent = Element.New()
        openRecent.SetName("Open recent")
        openRecent.SetSize(-0.5, -0.5)
        openRecent.SetBackgroundColor(255, 255, 255, 255)
        root.AddElement(openRecent)



    pass