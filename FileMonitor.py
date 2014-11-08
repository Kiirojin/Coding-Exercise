import json
import time
import os
class FileMonitor:
    def __init__(self):
        self.doorCount = 0 
        self.alarmCount = 0 
        self.imageCount = 0 
        self.totalProcessingTime = 0 
        self.numFiles = 0 
        self.avgProcessingTime = 0 
    def parseFile(self, fileName):
        try:
            data = json.load(open(fileName))
            start = os.path.getctime(fileName)
            type = data["Type"].lower()
            if type == "img":
                self.imageCount += 1
            elif type == "door":
                self.doorCount += 1
            elif type == "alarm":
                self.alarmCount += 1
            end = time.time()
            self.totalProcessingTime += (end - start)
            self.numFiles += 1
            self.avgProcessingTime = self.calculateAverage()
        except IOError:
           print "The system could not open the file named: %s" % fileName
        except ValueError:
            print "The created file was not a valid json file."

    def calculateAverage(self):
        if self.numFiles == 0:
            return 0 
        else:
            return self.totalProcessingTime/self.numFiles
    def printStatistics(self):
        print "DoorCnt: %d, ImgCnt: %d, AlarmCnt: %d, avgProcessingTime : %dms" % (self.doorCount, self.imageCount, self.alarmCount, self.avgProcessingTime*1000)
