n = int(input())
arr = list(map(int, input().split()))
low = 0
high = n-1
def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(low, high, arr):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        while True:
            i+=1
            if(arr[i] > pivot):
                break
        while True:
            j-=1
            if(arr[j] < pivot):
                break
        if(i<j):
            swap(i,j,arr)
    swap(low, j, arr)
    return j

def quicksort(low, high, arr):
    if(low < high):
        j = partition(low, high, arr)
        quicksort(low, j-1, arr)
        quicksort(j, high, arr)





quicksort(low, high, arr)
print(*arr)


        


