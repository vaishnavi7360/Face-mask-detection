
from views.AuthView import AuthView
from views.DetectionView import DetectionView

class MyApp:

    def run(self):
        # av = AuthView()
        # av.load()

        dv = DetectionView()
        dv.load()

    def printSomething(self):
        print("This is My App print function")


app = MyApp()
app.run()