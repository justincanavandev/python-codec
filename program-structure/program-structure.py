def main():
  print('This line is printed directly from the main function of the program')
  secondary_function()

def secondary_function():
  print('This line is printed from a secondary function call within the main function')

# code doesn't run w/o line 10

# if __name__ == '__main__':
#   main()




# input and output

# takes in user input, saving the users input in the variable "name"

# allows you to type in the terminal a response to the input "what is your name".. if you type Justin in the terminal, after that it will print("Very nice... justin... !")
name = input("what is your name? ")
age = input("how old are you? ")

# comma automatically puts a space between strings. a "+" is string concatenation and will read literally. these both print the same.

# string concatenation
print('Very nice to meet you, my name is ' + name + ' and I am ' + age + ' years old!') 

# commas
print('Very nice to meet you, my name is',name,'and I am', age,'years old!') 

# string literal
print(f'Very nice to meet you, my name is {name} and I am {age} years old!')

# uppercase method
print(f'Hi {name.upper()}!')

#format string method... empty object is a placeholder for the values provided in format method
print('Very nice to meet you, my name is {} and I am {} years old!'.format(name, age))