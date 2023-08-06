# -*- coding: utf-8 -*-


import threading
import json

from websocket import WebSocket
from ._events import EventEmitter

class WebSocketIO(WebSocket,EventEmitter):
  def __init__(self,**options):
    EventEmitter.__init__(self)
    WebSocket.__init__(self,options)
    pass

  def __wsRun__(self):

    try:
      super(WebSocketIO,self).connect(self.cntUrl,**self.cntOpts)
      self.emit("open")
    
      while(self.connected):
        try:
          payload=json.loads(self.recv())
          self.emit("message",payload)
        except:
          pass
      
      self.emit("close")
    except:
      self.emit("error")
      pass


  def connect(self,url,**options):
    self.cntUrl=url
    self.cntOpts=options
    self.td=threading.Thread(target=self.__wsRun__)
    self.td.setDaemon(True)
    self.td.start()

  # def close(self):
  #   if self.connected :
  #     self.emit("close")
  #   super(WebSocketIO,self).close()
    

    


