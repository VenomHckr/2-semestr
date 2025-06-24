text = input()
vowels = {'a': False , 'e': False, 'i': False, 'o': False, 'u': False }
vowels_count = 0
for char in text:
    if char in vowels:
        vowels [char] += 1
        vowels_count += 1
print(vowels_count)
print (vowels)