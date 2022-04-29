"""
2751번 수 정렬하기 2

1.  수 정렬을 각 선택정렬, 삽입정렬, 버블정렬, 합병정렬로 구현
"""

import sys

N = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(N)]


def pythonSort(numbers):
    numbers.sort()
    return numbers


def selectionSort(numbers):
    for i in range(N):
        minIdx = i
        for j in range(i, N):
            if numbers[j] < numbers[minIdx]:
                minIdx = j
        numbers[minIdx], numbers[j] = numbers[j], numbers[minIdx]

    return numbers


def insertionSort(numbers):
    for i in range(1, N):
        curr = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] >= curr:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = curr

    return numbers


def bubbleSort(numbers):
    for i in range(N):
        for j in range(1, N):
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

    return numbers


def merge(numbers, start, mid, end):
    newNumbers = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if numbers[i] < numbers[j]:
            newNumbers.append(numbers[i])
            i += 1
        else:
            newNumbers.append(numbers[j])
            j += 1

    while i <= mid:
        newNumbers.append(numbers[i])
        i += 1
    while j <= end:
        newNumbers.append(numbers[j])
        j += 1

    index = 0
    for idx in range(start, end + 1):
        numbers[idx] = newNumbers[index]
        index += 1

    return numbers


def mergeSort(numbers, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(numbers, start, mid)
        mergeSort(numbers, mid + 1, end)
        return merge(numbers, start, mid, end)


numbers = mergeSort(numbers, 0, N - 1)

for i in numbers:
    print(i)
