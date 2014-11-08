import os
from FileMonitor import FileMonitor
import win32file
import win32event
import win32con

#code taken from http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
#requires pywin32
monitor = FileMonitor();
path_to_watch = os.getcwd()

#
# FindFirstChangeNotification sets up a handle for watching
#  file changes. The first parameter is the path to be
#  watched; the second is a boolean indicating whether the
#  directories underneath the one specified are to be watched;
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
#
change_handle = win32file.FindFirstChangeNotification (
  path_to_watch,
  0,
  win32con.FILE_NOTIFY_CHANGE_FILE_NAME
)

#
# Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
#
try:

  before = dict ([(f, None) for f in os.listdir (path_to_watch)])
  while 1:
    result = win32event.WaitForSingleObject (change_handle, 1000)

    #
    # If the WaitFor... returned because of a notification (as
    #  opposed to timing out or some error) then look for the
    #  changes in the directory contents.
    #
    if result == win32con.WAIT_OBJECT_0:
      after = dict ([(f, None) for f in os.listdir (path_to_watch)])
      added = [f for f in after if not f in before]
      before = after;
      if added:
        #print "Added: ", ", ".join (added)
        for file in added:
            if(os.path.isdir(file)):
                continue;
            monitor.parseFile(file)
    monitor.printStatistics()
    win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)