arr = [2,5,8,2,11,9,12,1]
n = len(arr)

'''
# Selection sort....

a = []
b = arr[0]
for i in range(0,n-1):
    for j in range(i+1,n):
        if (arr[j]<arr[i]):
            arr[j],arr[i] = arr[i],arr[j]

print(arr)

'''
    
##############################################

'''

# Bubble sort....

c = 1
while (c<n):
    for i in range(n-c):
        if (arr[i]>arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]

    c+=1
print(arr)

'''


###############################################



'''

# Insertion sort....

for i in range(1,n):
    c = arr[i]
    j = i-1
    while (j>=0 and arr[j]>c):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=c

print(arr)

'''
