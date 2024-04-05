import time
import numpy as np
import matplotlib.pyplot as plt

def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

sorts = [
    {
        "name": "Selection Sort",
        "sort": lambda arr: selectionSort(arr)
    },
    {
        "name": "Insertion Sort",
        "sort": lambda arr: insertionSort(arr)
    },
    {
        "name": "Bubble Sort",
        "sort": lambda arr: bubbleSort(arr)
    },
]

elements = np.array([p * 1000 for p in range(1, 5)])

plt.xlabel('List Length')
plt.ylabel('Time Complexity')

for sort in sorts:
    times = []
    start_all = time.time()
    for p in range(1, 5):
        start = time.time()
        a = np.random.randint(1000, size=p*1000)
        sort["sort"](a)
        end = time.time()
        times.append(end-start)
        print(sort["name"], "sorted", p * 1000, "Elements in", end - start, "S")
    end_all = time.time()
    print(sort["name"], "sorted elements in", end_all - start_all, "S")
    plt.plot(elements, times, label=sort["name"])

plt.grid()
plt.legend()
plt.show()                                   
