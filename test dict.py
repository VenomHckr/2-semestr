my_dict = {}
for num in range(10, -6, -1):  
    if num != 0:  
        my_dict[num] = num ** num
print('\n'.join(f"{key}: {value}" for key, value in my_dict.items()))
  