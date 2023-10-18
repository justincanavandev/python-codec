# for loops

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("num + 1    ", number + 1)

# for loops with range

for i in range(3):
    print("i    ", i) #prints 0   1   2.... basically goes up to 2 and stops at 3

# nested for loops ... used for accessing nested data.

teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
    print('team', team) # prints each individual array ["Jody", "Abe"]
    for name in team:  
        print("name", name) # prints each individual array item "Jody"

# while loop... executes code with condition evaluates to true

num = 3
while num<6:
    print(num) #prints 3 4 5 then stops because the number will be 6
    num +=1

# pass 
