import random

N = 10

def input_data(data):
    for i in range(N):
        data.append(random.randint(0,N))
    return data
def quicksort(left,right):
    if left >= right:
        return
    else:
        pivot = data[right]
        partition = division(left,right,pivot)
        quicksort(left,partition -1)
        quicksort(partition + 1,right)
def division(left, right, pivot):
    p = 0
    leftnum = left
    rightnum = right - 1
    while left <= right:
        while data[rightnum] > pivot:
            rightnum = rightnum -1
        while data[leftnum] < pivot:
            leftnum = leftnum + 1
        if leftnum < rightnum:
            data[rightnum],data[leftnum] = data[leftnum],data[rightnum]
        elif leftnum >= rightnum:
            break
    temp = data[leftnum]
    data[leftnum] = pivot
    data[right] = temp
    p = leftnum
    return p

if __name__ == "__main__":
    data = []
    data = input_data(data)
    print(data)
    quicksort(0,N - 1)
    print(data)