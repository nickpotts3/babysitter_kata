# WORKING HOURS 5PM-4AM 
# CAN NOT START BEFORE 5 OR END AFTER 4 
# REGULAR SHIFT START-TIME TO BEDTIME = $12/HOUR
# BEDTIME SHIFT: BEDTIME-MIDNIGHT = $8/HOUR
# MIDNIGHT SHIFT: MIDNIGHT - END-TIME = $16/HOUR





class Babysitter:
    def __init__(self) -> None:
        self.regularShiftPay = 12
        self.bedtimeShiftPay = 8
        self.midnightShiftPay = 16
        self.regularHours = 0
        self.bedtimeHours = 0
        self.midnightHours = 0

    # converts to military time
    def convertTime(self,time):
        if ( time <= 12 and time >= 5):
            return int(time)
        elif(time == 0):
            return -1
        else:
            return int(time + 12)

    # ensure start is before endtime and not greater than 5pm. Allow babysitter to start AFTER bedtime
    def validateStart(self,start,end) -> bool:
        if(self.convertTime(start) > 5):
            return False
        elif(self.convertTime(start) > self.convertTime(end)):
            return False
        elif(self.convertTime(start) == self.convertTime(end)):
            return False
        else:
            return True

    def validateEnd(self, start, end) -> bool:
        if(end > 16):
            return False
        elif(self.convertTime(start) > self.convertTime(end)):
            return False
        elif(self.convertTime(end) == self.convertTime(start)):
            return False
        else:
            return True

    def validateBedtime(self,bedtime) -> bool:
        pass

    def calculateRegularHours(self,start,end,bedtime) -> int:
        pass

    def calculateBedtimeHours(self,start,end,bedtime) -> int:
        pass

    def calculateMidnightHours(self,end) -> int:
        if(self.convertTime(end) > self.convertTime(12)):
            return self.convertTime(end) - self.convertTime(12)
        else:
            return 0


    def calculateTotalPay(self, start, end, bedtime) -> int:
        pass

sitter = Babysitter()

# ------ testing convertTime() -----------
five = sitter.convertTime(5)
assert five == 5

twelve = sitter.convertTime(12)
assert twelve == 12

threeTo15 = sitter.convertTime(3)
assert threeTo15 == 15

negOne = sitter.convertTime(0)
assert negOne == -1

# ------- testing validateStart() ----------
assert sitter.validateStart(5,10) == True # start at 5 

assert sitter.validateStart(10,5) == False # end is before start

assert sitter.validateStart(4,1) == False # ensuring can not start before 5

assert sitter.validateStart(5,5) == False # start and end time can not be the same because pointless

assert sitter.validateStart(5,4) == True # testing edge case 

# -------- testing validateEnd() ----------
assert sitter.validateEnd(5,10) == True # start at 5 end at 10 

assert sitter.validateEnd(10,5) == False # end is before start

assert sitter.validateEnd(4,1) == False # ensuring can not start before 5

assert sitter.validateEnd(5,5) == False # start and end time can not be the same because pointless

assert sitter.validateEnd(5,4) == True # edge case of earliest start time and latest end time 