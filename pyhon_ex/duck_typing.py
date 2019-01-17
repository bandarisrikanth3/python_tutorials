
class Pycharm:
    def execute(self):
        print('pycharm editor')

class Myeditor:
    def execute(self):
        print('myeditor editor')

class Compile:
    def code(self,ide):
        ide.execute()

ide = Pycharm()
editor = Compile()
editor.code(ide)

ide1 = Myeditor()
editor.code(ide1)