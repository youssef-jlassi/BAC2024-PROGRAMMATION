def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Exemple d'utilisation
if __name__ == "__main__":
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Tableau non trié:", unsorted_array)

    insertion_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
