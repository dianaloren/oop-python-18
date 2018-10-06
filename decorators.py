def add_div(func):
	def func_wrapper(name):
		return "<div>{0}</div>".format(func(name))
	return func_wrapper
		
def add_strong(func):
	def func_wrapper(name):
		return "<strong>{0}</strong>".format(func(name))
	return func_wrapper

def p_decorate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper
	
#mytext = add_div(p_decorate(add_strong(get_text)))
#print(mytext('Diana'))

@add_div
@p_decorate
@add_strong
def get_text(name):
	return "loren impsum, {0} variable".format(name)
	
print(get_text("Diana"))


class Person:
	def __init__(self):
		self.name = "John"
		self.family = "Doe"
		
	@p_decorate
	def get_fullname(self):
		return self.name
		
p = Person()
print(p.get_fullname())


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator
	
@tags("p")
def get_text(name):
    return "Hello "+name

print(get_text("John"))