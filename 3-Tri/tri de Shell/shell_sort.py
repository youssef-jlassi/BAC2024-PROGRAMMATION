def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

# Exemple d'utilisation
if __name__ == "__main__":
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Tableau non trié:", unsorted_array)

    shell_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
