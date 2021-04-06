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
        if(self.convertTime(end) > 11):
            return False
        elif(self.convertTime(end) < self.convertTime(start)):
            return False
        elif(self.convertTime(end) == self.convertTime(start)):
            return False
        else:
            return True
        pass

    def validateBedtime(self, start, bedtime) -> bool: # allow the babysitter to leave before bedtime BUT cannot start after bedtime
        if(self.convertTime(bedtime) < self.convertTime(start)): # bedtime occurs before start
            return False
        elif(self.convertTime(bedtime) < 0 or self.convertTime(bedtime) > 11): # ensure it is within the 5-4 time range
            return False
        elif(bedtime < 0):
            return False
        else:
            return True


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


# __TESTS__
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
assert sitter.validateStart(5,1) == True # start at 5
assert sitter.validateStart(6,4) == True # start at 6 end at 4
assert sitter.validateStart(3,12) == False #try starting before 5
assert sitter.validateStart(5,4) == True # try longest shift possible
assert sitter.validateStart(10,8) == False # try to end before start time

# -------- testing validateEnd() ----------
assert sitter.validateEnd(5,4) == True # test full shift
assert sitter.validateEnd(5,15) == False # test invalid end time
assert sitter.validateEnd(10,10) == False # test end == start
assert sitter.validateEnd(5, 12) == True # edge case
assert sitter.validateEnd(5,1) == True # start at 5 end at 1am 

# -------- Testing validateBedtime() -----
assert sitter.validateBedtime(8,5) == False #bedtime is before arrival
assert sitter.validateBedtime(5,12) == True #normal case
assert sitter.validateBedtime(5,5) == True #can start right at bedtime
assert sitter.validateBedtime(6,4) == True #edge case (bedtime is latest sitter can work)
assert sitter.validateBedtime(5,-2) == False #invalid parameter