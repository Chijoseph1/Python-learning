# class attributes are specific to a class not an instance of the class, it not an instance of the class so it can't be passed a parameter. 

# when changing the attribute of a class, class attributes doesnt change 

# class attribute is also you as, like a constant attribute,when you want it for everybody.
class person:
    number_of_person=0

    def __init__(self,name):
        self.name = name

# when we call it 
p1 = person("jim")
p1.number_of_person() # output is 0 it doesnt change affect the class
# we can change it like this
person.number_of_person = 8
print(p1.number_of_person()) # output = 8