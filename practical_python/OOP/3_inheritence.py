# class Cat:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def speak(self):
# 		print("Meow")

# class Dog:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def speak(self):
# 		print("Bark")

# Cat and Dog are similar, so ideally we would like to have a parent class

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
	def speak(self):
		print("Meow " * 3)

class Dog(Pet):
	def speak(self):
		print("Bark " * 3)

p = Pet("Jerry", 7)
p.show()

c = Cat("Meowda", 8)
c.show()
c.speak()

d = Dog("Wangda", 9)
d.show()
d.speak()
