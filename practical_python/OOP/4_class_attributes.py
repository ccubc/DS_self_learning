GRAVITY = -9.8 

class Person:
	PLANET = 'Earth' # Person.PLANET would also work if using this Class in other code
	number_of_people = 0 # attribute

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod # classmethod acts on class, not object. It will only access class attributes
	def number_of_people_(cls):
			return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1


p1 = Person("Jerry")
p2 = Person("Jill")
print(Person.number_of_people_())