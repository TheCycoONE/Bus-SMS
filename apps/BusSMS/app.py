from rapidsms.apps.base import AppBase

class App(AppBase):
   def handle(self, message):
      message.respond('hello world')
