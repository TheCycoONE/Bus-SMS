import re
from rapidsms.apps.base import AppBase
from BusSMS.models import StopTimes

class App(AppBase):
   # Handles recieving an SMS from the client
   #
   # Expected format is 'HSR stopnum busnum' or 'HSR stopnum'
   # e.g. HSR 1234 52A or HSR 1234
   #
   # Parses input responds with an SMS that contains the times when
   # the bus will be available.
   # e.g.
   # HSR Next bus 10 min, 2nd bus 15 min, 3rd bus 30 min
   # or
   # HSR Next Rte 1A 10 min, Rte 2 15 min, Rte 4 17 min.
   # Use HSR 1234 1A for more King.  Use 1234 2 for more Barton
   def handle(self, message):
      msg = message.raw_text.strip().upper();
      
      #validate sms to ensure proper format
      if(re.match("^HSR \d{4}( [0-9A-Z]{1,4})?$",msg,0) == None):
          message.respond('Invalid request')
          return 

      parts = msg.split(' ')
      resp = 'name:' + parts[0] + ' stop:' + parts[1]

      #handle optional bus #
      if(len(parts) > 2):
          resp += ' bus:' + parts[2]
 
      #TODO: implement lookup of bus schedule

      message.respond(resp)
