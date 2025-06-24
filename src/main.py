from kivymd.app import MDApp

from kivy.lang.builder import Builder
from kivy.core.window import Window

import json

Window.size = (1080/2, 1920/2)

class Main(MDApp):
    def build(self):
        return Builder.load_file("style.kv")
    
    def screen(self, id_screen):
        self.root.current = id_screen

    def add_todo(self):
        text = self.root.ids.text_to.text
        if text == "":
            pass
        else:
            to_do = {"CheckBox": "No", "Text": text}
            file_name = text + ".json"
            with open(file_name, "w") as f:
                json.dump(to_do, f, indent=4)
        
            
if __name__ == '__main__':
    Main().run()