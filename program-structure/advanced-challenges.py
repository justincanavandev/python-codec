# return larger sum

list1 = [1,9,5]
list2 = [2,3,7]

def larger_sum(list1, list2):
    list1_total = 0
    list2_total = 0
    for num in list1:       
        list1_total += num
    # print(list1_total)
    for num in list2:
        list2_total += num
    # print(list2_total)

    if (list1_total>=list2_total):
        # print('list1', list1)
        return list1
    else:
        # print('list2', list2)
        return list2

larger_sum(list1, list2)

# over 9000

list = [8000, 900, 120, 5000]

def over_nine_thousand(list):
    total_num = 0
    if len(list) == 0:
        return 0
    for num in list:
        
        total_num += num
      
        if total_num > 9000:
            # print('total', total_num)
            return total_num  
    return total_num    
over_nine_thousand(list)


# max num

nums = [50, -10, 0, 75, 20]

maximum_num = nums[0]
# print('max', maximum_num)

def max_num(nums):
    for num in nums:
        if num>maximum_num:
            maximum_num = num
            return num
        else:
            continue
    return maximum_num

# same values

nums1 = [5, 1, -10, 3, 3]
nums2 = [5, 10, -10, 3, 5]

def same_values(nums1, nums2):
    matches = []
    for index, num1 in enumerate(nums1):
        if num1 == nums2[index]:
            matches.append(index)
        else:
            continue

    return matches

same_values(nums1, nums2)

# reversed list

listy1 = [1, 2, 3]
listy2 = [3, 2, 1]
listy3 = [1,5,3]
listy4 = [3,2,1]

def reversed_list(list1, list2):
    list2_length = len(list2)
    subtract_var = 1
    for num1 in list1:

        if num1 == list2[list2_length-subtract_var]:
            # print('num1', num1)
            # print('list2num', list2[list2_length-subtract_var] )
            subtract_var +=1
            continue
        else: 
            # print("false")
            return False
    # print("true")
    return True

reversed_list(listy1, listy2)
reversed_list(listy3, listy4)