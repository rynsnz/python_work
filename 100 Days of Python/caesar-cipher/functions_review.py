'''
1. Create a function called greet().
2. Write 3 print statements inside the function.
3. Call the greet() function and run your code.
'''

def greet():
    print('Hello!')
    print('Hello!!')
    print('Hello!!!')

greet()

'''
1. Create a function that expects a parameter
'''
# (parameter expected)
def greet_with_name(name):
    print(f'Hello {name}!')
    print(f'Hello {name}!!')
    print(f'Hello {name}!!!')

# (argument passed to function)
greet_with_name('Ryan')
greet_with_name('Erwin')

'''
1. Create a function that expects two parameters
'''

def greet_with(name, location):
    print(f'Hello {name} from {location}!')

greet_with(location='Chicago', name='Ryan')