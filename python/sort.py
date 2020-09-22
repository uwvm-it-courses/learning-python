
def selection_sort (A) :
    for i in range (len(A)):
        min_idx = i
        for j in range(i + 1, len(A)) :
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    print('Масив відсортований вибірковим способом', A)
def bubble_sort (A) :
    swapped = True
    while swapped :
        swapped = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
    print('Масив відсортованний бульбашковим способом з циклом while', A)

def bubble_sort1 (A) :
    for i in range (len(A)-1) :
        for j in range (len(A)-i-1):
            if A[j] > A[j+1]:
                buff = A[j]
                A[j] = A[j+1]
                A[j+1] = buff
    print('Масив відсортованний бульбашковим способом з циклом for', A)

def insertion_sort(A):
    for i in range(1, len(A)):
        b = A[i]
        j = i-1
        while j >= 0 and A[j] > b:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = b
    print('Масив відсортований способом вставки', A)

import random
array = [random.randrange(0, 100) for i in range(10)]
print('Масив з випадковими числами', array)
selection_sort(array)
bubble_sort(array)
bubble_sort1 (array)
insertion_sort(array)
