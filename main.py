#Write a function that accepts any number of integers
# as positional arguments and any number of keyword arguments
# as students' attributes (name, age, country, class) and 
# prints the result of multiplying all of the integers with 
# a greeting based on the student attributes given.

def details_multiplied(*args,**kwargs):
    multiply=1
    for num in args:
        multiply*=num
        print(multiply)
    print(f"Hello{kwargs}")
