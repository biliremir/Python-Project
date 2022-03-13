# Task 1

def flatten(A):
    for B in A:
        if isinstance(B, list):
            yield from flatten(B)
        else:
            yield B
 
 
first_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
final_list = list(flatten(first_list))
print(final_list) 

# Task 2


first_list = [[1,2],[3,4],[5,6,7]]

first_list.reverse()

for l in first_list:
    l.reverse() 

print(first_list) 
