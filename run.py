from FileMonitor import FileMonitor
import os, time
#code taken from http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html

monitor = FileMonitor()
path_to_watch = os.getcwd() #Assumed to be watching the current directory
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (1)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  before = after;
  if added:
      #print "Added: ", ", ".join (added)
      for file in added:
          monitor.parseFile(file)
  monitor.printStatistics()
