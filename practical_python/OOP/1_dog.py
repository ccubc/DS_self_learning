# Object Oriented Programming in Python
# One simple class example

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age


d = Dog("Jerry", 7)
print(d.get_age())

d.set_age(33)
print(d.get_age())

# particularly useful to use classes, when you need to create more than one instances in this class

