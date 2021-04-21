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
    def __convertTime(self,time):
        if ( time <= 12 and time >= 5):
            return (time - 5)
        elif(time == 0):
            raise Exception("Sorry, invalid time entered.")
        else:
            return (time + 7)

# public method used to validate the start, end, and bedtime. Exception thrown if one of the methods returns false or input is 0 
    def validateTimes(self,start,end,bedtime) -> bool:
        if(start < 0 or end < 0 or bedtime < 0):
            #return False
            raise Exception("Time can not be 0 or negative.")

        if(self.__validateStart__(start,end) and self.__validateEnd__(start,end) and self.__validateBedtime__(start,bedtime)):
            return True
        else:
            #return False
            raise Exception("Sorry, invalid times supplied. Please try again.")
            
            
        
    # ensure start is before endtime and not greater than 5pm.
    def __validateStart__(self,start,end) -> bool:
        print(self.__convertTime(start))
        if(self.__convertTime(start) > self.__convertTime(end)): # end comes before start return false
            return False
        elif(self.__convertTime(start) < 12):
            return True
        else:
            return False

    def __validateEnd__(self, start, end) -> bool:
        if(self.__convertTime(end) > 11):
            return False
        elif(self.__convertTime(end) < self.__convertTime(start)):
            return False
        elif(self.__convertTime(end) == self.__convertTime(start)):
            return False
        else:
            return True

    def __validateBedtime__(self, start, bedtime) -> bool: # allow the babysitter to leave before bedtime BUT cannot start after bedtime
        if(self.__convertTime(bedtime) < self.__convertTime(start)): # bedtime occurs before start
            return False
        elif(self.__convertTime(bedtime) < 0 or self.__convertTime(bedtime) > 11): # ensure it is within the 5-4 time range
            return False
        elif(bedtime < 0):
            return False
        else:
            return True


    def calculateRegularHours(self,start,end,bedtime) -> int:

        soonestTime = min(self.__convertTime(end), self.__convertTime(bedtime), self.__convertTime(12)) # determine which comes first
        return (soonestTime - self.__convertTime(start))
        

    def calculateBedtimeHours(self,end,bedtime) -> int:
        if (self.__convertTime(bedtime) >= self.__convertTime(12)): # if midnight or later return 0
            return 0
        elif(self.__convertTime(bedtime) >= self.__convertTime(end)): # if babysitter ends before bedtime return 0
            return 0
        else:
            return ( min(self.__convertTime(12),self.__convertTime(end)) - self.__convertTime(bedtime))

    def calculateMidnightHours(self,end) -> int:
        if(self.__convertTime(end) > self.__convertTime(12)):
            return self.__convertTime(end) - self.__convertTime(12)
        else:
            return 0


    def calculateTotalPay(self, start, end, bedtime) -> int:
        return ( (self.calculateRegularHours(start,end,bedtime) * self.regularShiftPay) + 
                (self.calculateBedtimeHours(end, bedtime) * self.bedtimeShiftPay) + 
                (self.calculateMidnightHours(end) * self.midnightShiftPay))
