from kivymd.app import MDApp

from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (1080/2, 1920/2)

class Main(MDApp):
    def build(self):
        return Builder.load_file("style.kv")
    
if __name__ == '__main__':
    Main().run()