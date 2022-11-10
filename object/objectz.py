#create a class
class Person:
    #create a constructor
    likes = "cats"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #create a method
    def myName(self):
        print("Hello my name is " + self.name)
        
    def howOld(self):
        print("Hello my age is " + str(self.age))
        
    def intro(self):
        print("Hello my name is " + self.name + " and my age is " + str(self.age) + " and I like " + self.likes)

#create an object
p1 = Person("John", 36)

p1.intro()

print("---------------------------------")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def intro(self):
        print("Hello my name is " + self.name + " and my age is " + str(self.age) + " and I like " + self.likes + " and my grade is " + str(self.grade))

s1 = Student("Mike", 12, 7)
s1.intro()
s1.howOld()