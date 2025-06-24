import random
def pl(d):
    for i in d:
        print(*i)
matrix_1 = [[random.randint(-1000, 1000) for _ in range (10)] for _ in range (10)]
matrix_2 = [[random.randint(-1000, 1000) for _ in range (10)] for _ in range (10)]

print("matrix_1")
pl (matrix_1)   
print("matrix_2")    
pl (matrix_2)  
matrix_3 = [
    [matrix_1[i][j] + matrix_2[i][j] for j in range(10)] 
    for i in range(10)  
]
print("matrix_3")  
pl (matrix_3)