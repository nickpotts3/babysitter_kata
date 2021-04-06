# WORKING HOURS 5PM-4AM 
# CAN NOT START BEFORE 5 OR END AFTER 4 
# REGULAR SHIFT START-TIME TO BEDTIME = $12/HOUR
# BEDTIME SHIFT: BEDTIME-MIDNIGHT = $8/HOUR
# MIDNIGHT SHIFT: MIDNIGHT - END-TIME = $16/HOUR


# 5 6 7 8 9 10 11 12 1 2 3  4 

# 0 1 2 3 4 5  6  7  8 9 10 11




class Babysitter:
    def __init__(self) -> None:
        self.regularShiftPay = 12
        self.bedtimeShiftPay = 8
        self.midnightShiftPay = 16
        self.regularHours = 0
        self.bedtimeHours = 0
        self.midnightHours = 0

    # converts to int in range [0,11] because 11 hours is max. Military time will not work
    def convertTime(self,time):
        if ( time <= 12 and time >= 5):
            return int(time - 5)
        elif(time == 0):
            return -1
        else:
            return int(time + 7)

    # ensure start is before endtime and not greater than 5pm. Allow babysitter to start AFTER bedtime
    def validateStart(self,start,end) -> bool:
        if(self.convertTime(start) > self.convertTime(end)):
            return False
        elif(self.convertTime(start) < 11):
            return True
        else:
            return

    def validateEnd(self, start, end) -> bool:
        pass

    def validateBedtime(self,bedtime, start) -> bool: # allow the babysitter to leave before bedtime (end < bedtime) is okay
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
zero = sitter.convertTime(5)
assert zero == 0

seven = sitter.convertTime(12)
assert seven == 7

fourTo11 = sitter.convertTime(4)
assert fourTo11 == 11

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

assert sitter.validateEnd(5,6) == False # ensuring can not end after 4

assert sitter.validateEnd(5,5) == False # start and end time can not be the same because pointless

assert sitter.validateEnd(5,4) == True # edge case of earliest start time and latest end time 

assert sitter.validateEnd(8,7) == False