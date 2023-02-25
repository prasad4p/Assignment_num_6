# Assignment_num_6 = Assign_num_2

class Dog:
    def __init__(self,dog_name,dog_age,coat_color):
        self.dog_name = dog_name
        self.dog_age = dog_age
        self.coat_color = coat_color

    def description(self):
        name = self.dog_name
        age = self.dog_age
        print(f"Name : {name} \nAge : {age}")

    def get_info(self):
        color = self.coat_color
        return color
    
class JackRussellTerrier(Dog):
    def __init__(self,dog_name,dog_age,coat_color,origin):
        super().__init__(dog_name,dog_age,coat_color)
        self.origin_jack = origin
    def Jack_origin(self):
        return (f"Origin Country of JackRussell : {self.origin_jack}")
    
class Bulldog(Dog):
    def __init__(self,dog_name,dog_age,coat_color,origin):
        super().__init__(dog_name,dog_age,coat_color)
        self.origin_bulldog = origin
    def Bull_origin(self):
        return (f"Origin Country of Bulldog : {self.origin_bulldog}")
    

# obj_1 = Dog("Poee","5 Month","white_brown")
# obj_1.description()
# print((obj_1.get_info()))

obj_1 = JackRussellTerrier("Jack","4 Month","white","England")
obj_1.description()
print((obj_1.get_info()))
print((obj_1.Jack_origin()))

obj_2 = Bulldog("Browne","1 yr","Brown","England")
obj_2.description()
print((obj_2.get_info()))
print((obj_2.Bull_origin()))

    