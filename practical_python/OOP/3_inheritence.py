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

	def speak(self):
		print("I don't know what to say")


class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) # super references the parent class
		self.color = color

	def speak(self):
		print("Meow " * 3)

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
	def speak(self):
		print("Bark " * 3)

p = Pet("Jerry", 7)
p.show()

c = Cat("Meowda", 8, "white")
c.show()
c.speak()

d = Dog("Wangda", 9)
d.show()
d.speak()
