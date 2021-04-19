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

    # converts to int in range [0,11] because 11 hours is max. Military time will not work
    def convertTime(self,time):
        if ( time <= 12 and time >= 5):
            return (time - 5)
        elif(time == 0):
            raise Exception("Sorry, invalid time entered.")
        else:
            return (time + 7)

    def validateTimes(self,start,end,bedtime) -> bool:
        if(start < 0 or end < 0 or bedtime < 0):
            return False
          #  raise Exception("Time can not be 0 or negative.")

        if(self.__validateStart__(start,end) and self.__validateEnd__(start,end) and self.__validateBedtime__(start,bedtime)):
            return True
        else:
            return False
           # raise Exception("Sorry, invalid times supplied. Please try again.")
            
            
        
    # ensure start is before endtime and not greater than 5pm.
    def __validateStart__(self,start,end) -> bool:
        print(self.convertTime(start))
        if(self.convertTime(start) > self.convertTime(end)): # end comes before start return false
            return False
        elif(self.convertTime(start) < 12):
            return True
        else:
            return False

    def __validateEnd__(self, start, end) -> bool:
        if(self.convertTime(end) > 11):
            return False
        elif(self.convertTime(end) < self.convertTime(start)):
            return False
        elif(self.convertTime(end) == self.convertTime(start)):
            return False
        else:
            return True
        pass

    def __validateBedtime__(self, start, bedtime) -> bool: # allow the babysitter to leave before bedtime BUT cannot start after bedtime
        if(self.convertTime(bedtime) < self.convertTime(start)): # bedtime occurs before start
            return False
        elif(self.convertTime(bedtime) < 0 or self.convertTime(bedtime) > 11): # ensure it is within the 5-4 time range
            return False
        elif(bedtime < 0):
            return False
        else:
            return True


    def calculateRegularHours(self,start,end,bedtime) -> int:

        soonestTime = min(self.convertTime(end), self.convertTime(bedtime), self.convertTime(12)) # determine which comes first
        return (soonestTime - self.convertTime(start))
        

    def calculateBedtimeHours(self,end,bedtime) -> int:
        if (self.convertTime(bedtime) >= self.convertTime(12)): # if midnight or later return 0
            return 0
        elif(self.convertTime(bedtime) >= self.convertTime(end)): # if babysitter ends before bedtime return 0
            return 0
        else:
            return ( min(self.convertTime(12),self.convertTime(end)) - self.convertTime(bedtime))

    def calculateMidnightHours(self,end) -> int:
        if(self.convertTime(end) > self.convertTime(12)):
            return self.convertTime(end) - self.convertTime(12)
        else:
            return 0


    def calculateTotalPay(self, start, end, bedtime) -> int:
        return ( (self.calculateRegularHours(start,end,bedtime) * self.regularShiftPay) + 
                (self.calculateBedtimeHours(end, bedtime) * self.bedtimeShiftPay) + 
                (self.calculateMidnightHours(end) * self.midnightShiftPay))


# __TESTS__
sitter = Babysitter()


# ------ testing calculateBedtimeHours() ----
assert (sitter.calculateBedtimeHours(2,10) == 2) # regular case
assert (sitter.calculateBedtimeHours(12,11) == 1) #bedtime is 11
assert (sitter.calculateBedtimeHours(8,8) == 0) #bedtime is same as end
assert (sitter.calculateBedtimeHours(10,12) == 0) #bedtime is after end
assert (sitter.calculateBedtimeHours(12,8) == 4) # bedtime is same as start

# ----- testing calculateMidnightHours() ----
assert (sitter.calculateMidnightHours(2) == 2) # regular case
assert (sitter.calculateMidnightHours(12) == 0) # end == midnight
assert (sitter.calculateMidnightHours(10) == 0) # end is before midnight
assert (sitter.calculateMidnightHours(4) == 4) # edge case where end == 4

# ----- calculateTotalPay() --------------
assert (sitter.calculateTotalPay(5,7,6) == 20)
assert (sitter.calculateTotalPay(10,2,12) == 56)
assert (sitter.calculateTotalPay(5,4,10) == 140)
assert (sitter.calculateTotalPay(12, 2, 12) == 32)
assert (sitter.calculateTotalPay(5,1,10) == 92)
