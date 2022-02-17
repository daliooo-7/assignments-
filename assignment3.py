"""
Author: Dalio Benavidez Jr.
Class: Intro to Scripting
Date: 2/16/22
"""
class Car: # class name
    def __init__(self, make, model): # the data attributes
        self.__make = make
        self.__year_model = model
        self.__speed = 0 # set speed to 0

    def accelerate(self):
        self.__speed += 5 # increments by 5 each time it is called

    def brake(self):
        self.__speed -= 5 # decreases by 5 each time it is called
        if (self.__speed < 0):
            self.__speed = 0

    def get_speed(self):
        return self.__speed # return speed

if __name__ == '__main__':
    thisCar = Car(2021, 'Lamborghini') # main function

    thisCar.accelerate() # calls accelerate
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.accelerate()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.accelerate()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.accelerate()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.accelerate()
    print("Lamborghini's current speed:", thisCar.get_speed())

    print()

    thisCar.brake() # calls break
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.brake()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.brake()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.brake()
    print("Lamborghini's current speed:", thisCar.get_speed())
    thisCar.brake()
    print("Lamborghini's current speed:", thisCar.get_speed())


#question 2

class Employee: # class declaration
    def __init__(self, name="", IDNum = 0, dep="", job=""): # class data attributes
        self.__name = name
        self.__IDNum = IDNum
        self.__dep = dep
        self.__job = job


    def setName(self, nameX): # sets name
        self.__name = nameX

    def setID(self, IDx): # sets ID
        self.__IDNum = IDx

    def setDep(self, depX): # sets Department
        self.__dep = depX

    def setJob(self, jobX): # sets Job
        self.__job = jobX

    def getName(self): # returns name
        return self.__name

    def getID(self): # returns ID number
        return self.__IDNum

    def getDep(self): # returns Department
        return self.__dep

    def getJob(self): # returns Job
        return self.__job

emp1 = Employee() # creates object
emp2 = Employee()
emp3 = Employee()

emp1.setName("Susan Meyers") # assigns attributes to each object
emp1.setID(47899)
emp1.setDep("Accounting")
emp1.setJob("Vice President")

emp2.setName("Mark Jones") # assigns attributes to each object
emp2.setID(39119)
emp2.setDep("IT")
emp2.setJob("Programmer")

emp3.setName("Joy Rogers") # assigns attributes to each object
emp3.setID(81774)
emp3.setDep("Manufacturing")
emp3.setJob("Engineer")

print("Name:", emp1.getName()," ", "ID Number:", emp1.getID()," ", "Department:", emp1.getDep()," ", "Job:", emp1.getJob())
print("Name:", emp2.getName()," ", "ID Number:", emp2.getID()," ", "Department:", emp2.getDep()," ", "Job:", emp2.getJob())
print("Name:", emp3.getName()," ", "ID Number:", emp3.getID()," ", "Department:", emp3.getDep()," ", "Job:", emp3.getJob())

print()


# question 3

class Employee: # class declaration
    def __init__(self, name="", IDNum = 0, dep="", job=""): # class data attributes
        self.__name = name
        self.__IDNum = IDNum
        self.__dep = dep
        self.__job = job


    def setName(self, nameX): # sets name
        self.__name = nameX

    def setID(self, IDx): # sets ID
        self.__IDNum = IDx

    def setDep(self, depX): # sets Department
        self.__dep = depX

    def setJob(self, jobX): # sets Job
        self.__job = jobX

    def getName(self): # returns name
        return self.__name

    def getID(self): # returns ID number
        return self.__IDNum

    def getDep(self): # returns Department
        return self.__dep

    def getJob(self): # returns Job
        return self.__job

emp1 = Employee() # creates object
emp2 = Employee()
emp3 = Employee()

emp1.setName("Susan Meyers") # assigns attributes to each object
emp1.setID(47899)
emp1.setDep("Accounting")
emp1.setJob("Vice President")

emp2.setName("Mark Jones") # assigns attributes to each object
emp2.setID(39119)
emp2.setDep("IT")
emp2.setJob("Programmer")

emp3.setName("Joy Rogers") # assigns attributes to each object
emp3.setID(81774)
emp3.setDep("Manufacturing")
emp3.setJob("Engineer")

print("Name:", emp1.getName()," ", "ID Number:", emp1.getID()," ", "Department:", emp1.getDep()," ", "Job:", emp1.getJob())
print("Name:", emp2.getName()," ", "ID Number:", emp2.getID()," ", "Department:", emp2.getDep()," ", "Job:", emp2.getJob())
print("Name:", emp3.getName()," ", "ID Number:", emp3.getID()," ", "Department:", emp3.getDep()," ", "Job:", emp3.getJob())

print()

#question 4

class Students(): # class declaration
    def __init__(self, student, courseA, courseB, courseC, courseD, courseE, courseF):
        self.student = student
        self.courseA = courseA
        self.courseB = courseB
        self.courseC = courseC
        self.courseD = courseD
        self.courseE = courseE
        self.courseF = courseF

    def sum (self): # determines average percentage
        num = self.courseA + self.courseB + self.courseC + self.courseD + self.courseE + self.courseF
        sum = num / 600
        return (round(sum, 2))

def average(course): # determines average
    val = 0
    for x in range(0, 25):
        val += course[x]
    val /= 25
    return round(val, 2)


if __name__ == '__main__': # main function
    import random # imports random library

    students=["Willie", "Marina", "Jalen", "Brady", "James", # group of all students
              "Sam", "Ram", "Tam", "Michael", "Symon",
              "Julian", "Clint", "Kayle", "Breanna", "Daisy",
              "Eric", "Hector", "Pooch", "Gibby", "Gabe",
              "Clarissa", "Nutter", "Nate", "Snooky", "Fausto"]

    courseA = [random.uniform(0,100) for i in range(0,25)] # assigns course and student to random
    courseB = [random.uniform(0,100) for i in range(0,25)]
    courseC = [random.uniform(0,100) for i in range(0,25)]
    courseD = [random.uniform(0,100) for i in range(0,25)]
    courseE = [random.uniform(0,100) for i in range(0,25)]
    courseF = [random.uniform(0,100) for i in range(0,25)]

    classmate = [Students(students[x], courseA[x], courseB[x], courseC[x], courseD[x], courseE[x], courseF[x]) for x in range (0,25)]

    percents = [classmate[x].sum() for x in range(0,25)] # assigns percentage amongst 25 students

    size = len(percents) # loops for the 25 students 
    for j in range(size):
        for i in range(j+1, size):
            if (percents[j] > percents[i]):
                temp = percents[j]
                percents[j] = percents[i]
                percents[i] = temp
                temp2 = students[j]
                students[j] = students[i]
                students[i] = temp2

    averages = [average(courseA), average(courseB), average(courseC), average(courseD), average(courseE), average(courseF)]

    top = 0 # determines the top grade average
    for i in range(0,6):
        if averages[top] < averages[i]:
            top = i


    print("Student with the highest percentage:", students[24])
    print("Percentage:", percents[24])
    print("Course with the highest average: Course", top + 1)
    print("The average was:", averages[top])
