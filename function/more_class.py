# inheritance : this are two classes that are very similar

class pet: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old.")
    def speak(self):
        say =input("i dont know what to say\n")
        while say != "meow":
            print("input correct sound")
            say =input("what the sound?")
        print("correct sound")



# this can be called child class or derived class because it inherited, from the parent
class Dog(pet):
    def speak(self):
        print("bark")

class Cat(pet):
    def __init__(self, name, age,color):
        super().__init__(name, age) # refering to the super class the class we inheritanted from.
        self.color = color

    def speak(self):
        print("meow")
        print(f"I am {self.name} and i am {self.age} years old, and am {self.color} in color")

class Fish(pet):
    pass

# p = pet("boy",12)
# p.speak()
# d= Dog("bool", 13)
# d.speak()
c= Cat("bool", 13,"blue")
c.speak()
# f= Fish("bool", 13)
# f.speak()
# p1.show()
# but we can call the speak method also
