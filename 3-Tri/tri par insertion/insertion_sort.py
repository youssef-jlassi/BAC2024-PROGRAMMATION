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
    # Demander à l'utilisateur de saisir les éléments du tableau
    input_str = input("Entrez les éléments du tableau séparés par des espaces: ")
    unsorted_array = [int(num) for num in input_str.split()]


    insertion_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
