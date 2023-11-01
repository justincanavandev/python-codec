# pass keyword    -basically means do nothing. so if the condition is true, do nothing.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# for name in names:
#    if 'n' in name.lower():
#        pass
#    else:
#        print(name)


# break keyword   -once the condition is met, the loop stops. this will print only "Joyce" because the loop stops at "Hannah"

# for name in names:
#   if 'h' in name.lower():
#       break
#   else:
#       print(name)


# continue keyword   -if condition is met, that iteration is skipped over and moves onto the next iteration

for name in names:
  if 'm' in name.lower():
      continue
  else:
      print(name)

# in context

# if the continue keyword statement is true, it WILL NOT go to the elif statements. it will move ahead to the following iteration of the array (ie if we're on Amanda, it will skip to Rachel and run the loop) .

# if the pass keyword is true, it will just continue to the following elif statement since it's not interupting the loop at all, it's just doing nothing

# if the break condition is met, the entire loop will stop running.


names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']
 
for name in names:
  if 'm' in name.lower():
      continue
      
  elif 'r' in name.lower():
      pass
      
  elif 'j' in name.lower():
      break
  else:
       print(name)