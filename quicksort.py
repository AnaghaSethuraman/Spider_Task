def part(arr,small,big):
    pivot=arr[big]
    left=small-1
    for i in range(small,big):
        if(arr[i]<pivot):
            left=left+1
            k=arr[left]
            arr[left]=arr[i]
            arr[i]=k
    l=arr[left+1]
    arr[left+1]=arr[big]
    arr[big]=l
    return(left+1)

def quicksort(arr, small, big):
    if(small<big):
        p= part(arr,small,big)
        quicksort(arr,small,p-1)
        quicksort(arr,p+1,big)

if __name__ == '__main__':
    n = int(input(print("Enter the number of elemnets in array ")))
    arr= []
    for i in range(n):
            x =int(input())
            arr.append(x)

    print("The array entered is :")
    for i in range( len(arr)):
        print(arr[i])

    quicksort(arr,0,n-1) #with last element as pivot
    print("The sorted array is  :")
    for i in range(len(arr)):
        print(arr[i])
