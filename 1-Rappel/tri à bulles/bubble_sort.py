def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Le drapeau pour optimiser le tri lorsque le tableau est déjà trié
        swapped = False

        # Parcours du tableau de 0 à n-i-1, car les i derniers éléments sont déjà triés
        for j in range(0, n-i-1):
            # Comparaison des éléments adjacents
            if arr[j] > arr[j+1]:
                # Échanger les éléments si l'élément actuel est plus grand que le suivant
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Mettre à jour le drapeau
                swapped = True
        # Si aucun échange n'a été effectué dans cette itération, le tableau est déjà trié
        if not swapped:
            break

if __name__ == "__main__":
    # Demander à l'utilisateur de saisir les éléments du tableau
    input_str = input("Entrez les éléments du tableau séparés par des espaces: ")
    unsorted_array = [int(num) for num in input_str.split()]


    print("Tableau non trié:", unsorted_array)

    bubble_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)