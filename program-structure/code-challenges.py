numbers = [20,30,35]

def divisible_by_ten(nums):
    counter = 0

    for number in nums:
        if number%10 == 0:
            counter+=1

    # print(counter)    
    return counter

divisible_by_ten(numbers)


names = ["justin", "steven", "tony"]
nameGreetings = []

def add_greetings(names):

    for name in names:
        name = "Hello " + name
        nameGreetings.append(name)

    # print('nameGreetings', nameGreetings) 
    return nameGreetings

add_greetings(names)


my_list = [4, 8, 10, 11, 12, 15]

# delete even numbers until first index is odd

def delete_starting_evens(my_list):
    if len(my_list)>0:
       
        while (len(my_list)>0 and my_list[0] % 2 == 0 ):
# notation for slicing. basically start:stop    if one is omitted, it doesn't have a specific start or end point
            my_list=my_list[1:]

        # print('my_list', my_list)
        return my_list
        

delete_starting_evens(my_list)

# odd indices
new_list = [4, 3, 7, 10, 11, -2]
odd_list = []


def odd_indices(new_list):
    for num in new_list:
        num_index = new_list.index(num)
        if num_index % 2 != 0:
            odd_list.append(num)

    # print('odd_list', odd_list)
    return odd_list
        
odd_indices(new_list)


# exponents

bases = [2,3,4] 
powers = [1,2,3]
answers = []

def exponents(bases, powers):
    for base in bases:
      
        for power in powers:
            powered = base**power
            answers.append(powered)

    print('answers', answers)
    return answers

exponents(bases, powers)