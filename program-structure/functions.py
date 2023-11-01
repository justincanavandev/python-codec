# creating a function

# : indicates the start of the function body.

def add_three(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum


sum_total = add_three(2, 4, 6)
# prints 12
print(sum_total)   

# function with if statements

def greetings(language):
    if language == "Spanish":
        greeting = "Hola"
    elif language == "English":
        greeting = "Hello"
    elif language == "French":
        greeting = "Bonjour"
    else:
        greeting = "unknown"

    print(greeting)

greetings("English")

