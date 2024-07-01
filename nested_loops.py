# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# #outer loop
# for x in list1:
#     #inner loop
#     for y in list2:
#         print(y, end=" ")
#     print()

#running time of the code

import time
start_time = time.time()

#outer loop
for i in range(100):
    #inner loop
    for i in range(100):
        print(i, end=" ")
    print()

print(round((time.time() - start_time),2))

# complexity O(n)