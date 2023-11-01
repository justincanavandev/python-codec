# calls the function in the else condition until the if condition is met.

def recursive_function(number):
    if number == 1:
        print("done", number)
        return 1
    else:
        print("recurring", number)
        return number * recursive_function(number-1)
    
recursive_function(20)