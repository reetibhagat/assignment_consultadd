# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class MyTime():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(t1, t2):
        hours = int((t1.minutes + t2.minutes) / 60)

        minutes = t1.minutes + t2.minutes

        if (minutes > 60):
            minutes = (t1.minutes + t2.minutes) % 60

        hours += t1.hours + t2.hours
        newtime = MyTime(hours, minutes)
        return newtime

    def __repr__(self):
        return "Test hours:% s minutes:% s" % (self.hours, self.minutes)

    def display_time(self):
        print("time in hours:", self.hours, 'hours')

    def display_mins(self):
        print("time in totalmins:", (self.hours * 60) + self.minutes, 'minutes')






a = MyTime(2, 50)
b = MyTime(1, 40)
c = MyTime.add_time(a, b)
print([c])
c.display_time()
c.display_mins()
