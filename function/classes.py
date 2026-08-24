class business:
    def __init__(self,selling_price,total):
        self.price = selling_price
        # self.loss = loss
        self.total = total
    def gain(self):
        total= self.total - self.price 
        print(total)

amount = business(200,500)
amount.gain()
# print(boy)

class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade


class course:
    def __init__(self,name,max_student):
        self.name= name # self basically means this particular object
        self.max_student= max_student
        self.students = []

    def add_student(self,students):
        if len(self.students) < self.max_student:
            self.students.append(students)
            return True
        return False
    
    def get_average(self):
        value = 0
        for student in self.students:
            value +=  student.get_grade()
            return value / len(self.students)

s1 = student("boy",12,34)
s2 = student("car",12,34)

# print(s1.get_grade())
d1 = course("boy",2)
print(d1.add_student(s1))
print(d1.add_student(s2))
print(d1.get_average())