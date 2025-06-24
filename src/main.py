from kivymd.app import MDApp

from kivy.lang.builder import Builder


class Main(MDApp):
    def build(self):
        return Builder.load_file("style.kv")
    
if __name__ == '__main__':
    Main().run()