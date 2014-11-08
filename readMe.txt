The two files to run are run.py and runFaster.py.
run.py should work in any os with Python installed. This program is expensive because it continually polls the folder for new files.

runWithoutPolling.py , Leverages notifications instead of polling. Is much less expensive than run.py
However, runWithoutPolling.py is specific to Windows and furthermore needs pywin32 to be installed.
http://sourceforge.net/projects/pywin32/files/pywin32/

It is assumed that the current working directory is the one to be monitored, but this can be easily changed.
Be careful that the json inputs are proper. Specifically the "Type" value of some of the example input was not wrapped in quotes.
If it is the case that a file is created that is not a valid json file, it will be ignored.

Tests are included for the FileMonitor class. run.py and runFaster.py are left untested, but could and probably should be tested.


BUG REPORT:
runFaster.py would randomly be unable to open files with IOError: [Errno13] Permission denied.
The problem seems to have something to do with the calls to the win32api and is solved on lines 49 and 50 by
if(os.path.isdir(file)):
    continue;

It is unclear why this seems to fix the problem. Debugging inconclusive, further testing needed.

UPDATE: This seems to actually be because the program seems to be trying to access the file so fast that an error is thrown.
The if statement simply just wastes time, giving the file some breathing room after it is created. We can (and should) replace
it with something like time.sleep(.001).