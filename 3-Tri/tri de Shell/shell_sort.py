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
    # Demander à l'utilisateur de saisir les éléments du tableau
    input_str = input("Entrez les éléments du tableau séparés par des espaces: ")
    unsorted_array = [int(num) for num in input_str.split()]


    shell_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
