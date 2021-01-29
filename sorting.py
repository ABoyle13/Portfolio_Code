import random
import time

def bubblesort(a):
    currenttime = time.clock()
    print("Bubble start time: ", currenttime)
    n = len(a)
    #print(n)
    while n != 1:
        for count in range (0, n-1):
            if a[count] > a[count + 1]:
                x = a[count]
                a[count] = a[count + 1]
                a[count + 1] = x

        n -= 1
    print(a)
    newtime = time.clock()
    print("Bubble end time: ",newtime)
    timetaken = newtime - currenttime
    print("Bubble time taken: ", timetaken)

def insertionsort(b):
    currenttime2 = time.clock()
    print("Insertion start time: ", currenttime2)
    n = len(b)
    #print(n)
    for j in range(1, n):
        nextCard = b[j]
        i = j - 1
        while i >= 0 and b[i] > nextCard:
            b[i+1] = b[i]
            i = i - 1
        b[i+1] = nextCard
    print(b)
    newtime2 = time.clock()
    print("Insertion end time: ", newtime2)
    timetaken2 = newtime2 - currenttime2
    print("Insertion time taken: ", timetaken2)

def mergesort(c):
    currenttime3 = time.clock()
    print("Merge start time: ", currenttime3)
    n = len(c)
    if n > 1:
        mid = n//2
        left_half = c[:mid]
        right_half = c[mid:]
        
        mergesort(left_half)
        mergesort(right_half)
        #print(left_half)
        #print(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                c[k] = left_half[i]
                i += 1
            else:
                c[k] = right_half[j]
                j += 1
            k += 1
            #check if left half has elements not merged
            while i < len(left_half):
                c[k] = left_half[i]
                i += 1
                k += 1
            #check if right half has elements not merged
            while j < len(right_half):
                c[k] = right_half[j]
                j += 1
                k += 1
            n -= 1
    print(c)
    newtime3 = time.clock()
    print("Merge end time: ", newtime3)
    timetaken3 = newtime3 - currenttime3
    print("Merge time taken: ", timetaken3)

#main program starts here

a = []
b = []
c = []
for i in range(0, 100):
    x = random.randint(1, 100)
    a.append(x)
    b.append(x)
    c.append(x)
#print(a)

bubblesort(a)
print("")
insertionsort(b)
print("")
mergesort(c)
