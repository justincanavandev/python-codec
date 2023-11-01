# try and except

# if the nums array is all numbers, it will print the sum of the numbers. if say one is a string, it will print the except block
# finally will execute no matter what

nums = [0, 1, 2, 3]    
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')

finally:
   print('Hope you got the result you want!')