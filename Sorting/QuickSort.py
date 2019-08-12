def partition(lst,low,high):
    i = low -1
    pivot = lst[high]
    for j in range(low,high):
        if lst[j] <= pivot:
            i+=1
            #swap(lst[i],lst[j])
            lst[i],lst[j] = lst[j],lst[i]

    #swap(lst[i+1],lst[high])
    lst[i+1],lst[high] = lst[high],lst[i+1]
    return i+1

def quickSort(lst,low,high):
    if low < high:
        pi =partition(lst,low,high)
        quickSort(lst,low,pi-1)
        quickSort(lst,pi+1,high)
    return lst

if __name__ == "__main__":
    print("Enter list elements")
    lst = list(map(int,input().split(" ")))
    print(lst)
    lst=quickSort(lst,0,len(lst)-1)
    print(lst)
    
