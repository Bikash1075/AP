# Find missing number
def find_missing_number(arr):
    s= set(arr)
    output=[]
    for i in range(1,arr[-1]):
        if i not in s:
            output.append(i)
    return output
arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_number(arr))