import datetime

class Milo:
    def __init__(self, data = None):
        self.data=data
        self.day = None
        self.month = None
        self.year = None
        self.x, self.y, self.z =  [int(item) for item in self.data.split('/')]
        self.milolist = [
        (self.x, self.y, self.z),
        (self.x, self.z, self.y),
        (self.y, self.x, self.z),
        (self.y, self.z, self.x),
        (self.z, self.x, self.y),
        (self.z, self.y, self.x)]

    def milo_date_possible(self, date_possible):
        correctDate = None
        try:
            self.year, self.month, self.day = date_possible
            if len(str(self.year))<=3:
                self.year+=2000
            new_date = datetime.date(year=self.year,month=self.month,day=self.day)
            correct_date = new_date
        except ValueError:
            correct_date = False
        return correct_date

    def printdates(self):
        for item in self.milolist:
            print(item, self.milo_date_possible(item))
    
    def milo_earliest_possible(self):
        earliest = datetime.date(3000,1,1)
        for item in self.milolist:
            current = self.milo_date_possible(item)
            if current:
                if current < earliest:
                    earliest = current
        return earliest
    
    def milo_answer(self):
        earliest=self.milo_earliest_possible()
        if earliest==datetime.date(3000,1,1):
            return "is illegal"
        else:
            return str(earliest)
        
                
with open("dates.txt") as f:
    for line in f:
        milo = Milo(data = line)
        #print("input: {:s}, the earliest possible legal date is ${:s}".format(line.rstrip(), milo.milo_answer()))
        print(milo.milo_answer())
