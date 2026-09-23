def merge(arr):
    if len(arr)>1:
        n = len(arr)//2

        L = arr[:n]
        R = arr[n:]

        merge(L)
        merge(R)
        i=j=k =0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
nums = [9,8,7,6,5,4,3,2,1]
print(nums)
merge(nums)
print(nums)


        

