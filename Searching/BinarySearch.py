def BinSearch(lst,x):
    beg = 0
    end = len(lst)
    mid = (beg+end)//2
    if beg == end:
        if lst[mid] == x:
            return f'found at index {mid}'
        else:
            return f'not found'
    else:
        while beg <= end:
            mid = (beg+end)//2
            if lst[mid] == x:
                return f'found at index {mid}'
            else:
                if x <= lst[mid]:
                    end = mid
                else:
                    beg = mid + 1
    return "not found"
                
x  = int(input("Enter element to search:"))  
print("Enter array")
lst = list(map(int,input())) #check how to take negative num in list also
print(lst)
#lst = [-1,0,2,3,4]
res = BinSearch(lst,x)
print(res)