def div(a,b):
	print(a/b)

def add_fun(func):
	def inner(a,b):
		if a<b:
			a,b=b,a
		return func(a,b)


	return inner

div1=add_fun(div)
div1(20,5)
