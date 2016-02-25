import os
import shutil
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class CleanCache(FileSystemEventHandler):
    def on_any_event(self, event):
        path = '_build/doctrees'
        if os.path.isdir(path): shutil.rmtree(path)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '../dichalcogenides'
    event_handler = CleanCache()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
