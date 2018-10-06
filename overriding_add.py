#Day class, which contains the visits and contacts that a web page generates during a day.

class Day:
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts
        
    def __str__(self):
        return "Visits {} and Contacts {}".format(self.visits, self.contacts)
        
    # 2. now I want to return a Day instance that has the total number of visits and contacts
    def __add__(self, other):
        total_visits = self.visits + other.visits
        total_contacts = self.contacts + other.contacts
        return Day(total_visits, total_contacts)
        
    # 3. implement the reverse (commutative property) of add
    def __radd__(self, other):
        if other == 0:
            print('other is 0')
            return self
        else:    
            print('other is not 0')
            return self.__add__(other)
            
        
# 1. create instances
day1 = Day(10, 2)
day2 = Day(20, 3)        

#print(repr(day1))
print("day1: ", day1)
print("day2: ", day2)

# 2.1. create the new instance
dayTotals = day1 + day2
print("Totals: ", dayTotals)

# 3. let's say we want to use the operator 'sum'
print("Totals with sum: ", sum([day1, day2]))