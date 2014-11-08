from FileMonitor import FileMonitor
import os, time
#code taken from http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html

monitor = FileMonitor()
path_to_watch = os.getcwd() #Assumed to be watching the current directory
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
timeElapsed = 0;
timeBefore = time.clock()
while 1:
  timeAfter = time.clock()
  timeElapsed = (timeAfter-timeBefore)
  if timeElapsed >= 1:
    monitor.printStatistics()
    timeElapsed = 0;
    timeBefore += 1;

  time.sleep(.001) #otherwise the file is accessed too fast
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  before = after;
  if added:
    #print "Added: ", ", ".join (added)
    for file in added:
      monitor.parseFile(file)

