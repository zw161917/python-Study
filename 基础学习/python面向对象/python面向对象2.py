'''
定义一个学生类，用来形容学生
'''
#定义一个空的类
class Student():
    #类下必须有内容
    pass

#定义一个对象
mingyue = Student()

class pythonStudent():
    #用None给不确定的值赋值
    name = None

class stu():
    name = "dana"
    age = 18
    def say(self):
        self.name = "naan"
        self.age = 12
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
sru = stu()
sru.say()
