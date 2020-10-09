class Math:
	@staticmethod
	# do not have access to instance, they don't change anything
	def add5(x):
		return x + 5

	@staticmethod
	def pr():
		print("run")

print(Math.add5(5)) # doesn't need to initiate this instance

Math.pr()