def bubble_Sort(arr):

    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
            if not swapped:
                break
    return arr
nums = [9,8,7,6,5,4,3,2,1]
print(nums)
bubble_Sort(nums)
print(nums)

                