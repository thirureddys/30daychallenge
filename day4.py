class Person:
    def __init__(self,initialAge):
        self.age=initialAge
        print self.age

            
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age >= 18:
            print self.age
            print "You are old."
        elif self.age in range(13,18):
            print "You are Teenager."
        elif self.age < 0:
            self.age=0
            print "Age is not valid, setting age to 0."
            print "You are young."
        elif self.age < 13:
            print "You are young."
        
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
        self.age+=1


t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())         
    p = Person(age)  
    p.amIOld()
    print "am before"
    for j in range(0, 3):
        p.yearPasses()
    print p.age
    p.amIOld()
    print("")
              
