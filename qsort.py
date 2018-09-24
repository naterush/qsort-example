import math

def QSort(A, lo, hi):
    print("Called QSort")
    if hi <= lo:
        return
    else:
        pivotIndex = int(math.floor((lo + hi) / 2))
        loc = Partition(A, lo, hi, pivotIndex)
        k = QSort(A, lo, loc - 1)
        j = QSort(A, loc + 1, hi)


def Partition(A, lo, hi, pIndex):
    pivot = A[pIndex]
    swap(A, pIndex, hi)
    left = lo
    right = hi - 1
    while left <= right:
        if A[left] <= pivot:
            left = left + 1
        else:
            swap(A, left, right)
            right = right - 1
    swap(A, left, hi)
    return left

def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp



if __name__ == "__main__":
    # problem (i)
    A = [1, 3, 2, 4, 5, 7, 6, 8, 9]
    print("Running i:")
    QSort(A, 0, len(A) - 1)
    print("\n")

    # problem (ii)
    A = [2, 6, 9, 5, 1, 3, 4, 7, 8]
    print("Running ii:")
    QSort(A, 0, len(A) - 1)
    print("\n")

    # problem (iii)
    A = [7, 6, 8, 4, 9, 3, 5, 2, 1]
    print("Running iii:")
    QSort(A, 0, len(A) - 1)
