import os
import shutil
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
fromFolder='C:/Users/Lap_AcerTM/Downloads'
class FileMovement(FileSystemEventHandler):
    def on_created(self,event):
        print(event)


eventHandler=FileMovement()



observer=Observer()
observer.schedule(eventHandler,fromFolder,recursive=True)
observer.start()