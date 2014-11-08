from unittest import TestCase
from FileMonitor import FileMonitor
from StringIO import StringIO
import sys
class TestFileMonitor(TestCase):

    def test_parseFile(self):
        monitor = FileMonitor()
        out = StringIO()
        sys.stdout = out
        monitor.parseFile("doesNotExist.json")
        monitor.parseFile("run.py")
        output = out.getvalue().strip()
        assert output == "The system could not open the file named: doesNotExist.json\n" \
                         "The created file was not a valid json file."
        monitor.parseFile("door.json")
        monitor.parseFile("img.json")
        monitor.parseFile("alarm.json")
        monitor.parseFile("alarm-2.json")
        assert monitor.doorCount == 1
        assert monitor.alarmCount == 2
        assert monitor.imageCount == 1
        assert monitor.avgProcessingTime > 0
        
    def test_printStatistics(self):
        monitor = FileMonitor();
        monitor.parseFile("door.json")
        monitor.parseFile("img.json")
        monitor.parseFile("alarm.json")
        monitor.parseFile("alarm-2.json")
        out = StringIO()
        sys.stdout = out
        monitor.printStatistics()
        output = out.getvalue().strip()
        assert output.startswith("DoorCnt: 1, ImgCnt: 1, AlarmCnt: 2, avgProcessingTime : ")
        assert output.endswith("ms")