# Q Write a Python function sum_list(arr) that returns the sum of all numbers in the list.
# Q Write a Python function find_smallest(arr) that returns the smallest number in a non-empty list.
# Q Write a Python function count_even(arr) that returns how many even numbers are present in the list.
# Q Write a Python function linear_search(arr, target) that returns the index of target if found.
#   If target is not found, return -1.
# Q Write a Python function reverse_list(arr) that returns a new list with elements in reverse order.
# Q Write a Python function count_occurrences(arr, target) that counts how many times target appears in the list.
# Q Write a Python function remove_duplicates(arr) that returns a new list with duplicate values removed.
# Q Write a Python function second_largest(arr) that returns the second largest unique number in the list.
# Q Write a Python function is_sorted(arr) that returns True if the list is sorted in non-decreasing order.
# Q Write a Python function count_vowels(s) that returns the number of vowels in the string.


def sum_list():
    arr=[2,4,6,8]
    sum = 0
    for i in arr:
        sum += i
    return sum

def  smallet_num():
    arr = [2,4,3,1,9,-1,0]
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min

def count_even():
    arr=[1,2,3,4,5,6]
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    print(even)       
    return len(even)

def liner_srch(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def reverse_list(arr):
   
    # while left<right:
    #     arr[left],arr[right] = arr[right],arr[left]
    #     left,right = left+1,right-1
    # return arr
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return arr
    
def count_occurrences(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count +=1
    return count

def remove_duplicates(arr):
    remove_duplicate=[]
    for i in range(len(arr)):
        if arr[i] not in remove_duplicate:
            remove_duplicate.append(arr[i])
            print(arr[i])
        else:
            i+=1
    return remove_duplicate        



def second_largest(arr):
    fst_max = max(arr)
    sec_max = fst_max
    for i in arr:
        if fst_max > i:
            sec_max = i
    return sec_max

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True    

def bubbel_in_one(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp =arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp
    return arr


def palandrom():
    text='1223221'
    reverse = '' 
    for i in text:
        reverse = i +reverse
  
    if reverse == text:
        return True
    else:
        return False



def count_vovels():
    text = "programming"
    vovels = ['a','e','i','o','u']
    count =0
    for t in text:
        if t in vovels:
            count+=1
    # for i in range(len(text)):
    #     for j in range(len(vovels)):
    #        if text[i] == vovels[j]:
    #         count +=1
    return count


def chr_frequency(word):
    f={}
    for ch in word:
        f[ch]=f.get(ch,0)+1
    return f


       

output= count_occurrences([10,20,4,9,8,8],3)
print(output)
