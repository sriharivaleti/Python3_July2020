class ClassAttributeDemo:
    
    #Class attribute
    thisisclassvariable = "sreehari"

    def __init__(self, name,age):
        self.name =name
        self.age = age

    def run(self):
        print("name :", self.name, "age :", self.age)



object1 = ClassAttributeDemo("sreehari",34)

print(object1.name, object1.age, object1.thisisclassvariable)

object2 = ClassAttributeDemo("jyostna",24)

print(object2.name, object2.age, object2.thisisclassvariable)

object2.thisisclassvariable ='Jyostna'


print(object1.name, object1.age, object1.thisisclassvariable)
print(object2.name, object2.age, object2.thisisclassvariable)

object1.run()
object2.run()


