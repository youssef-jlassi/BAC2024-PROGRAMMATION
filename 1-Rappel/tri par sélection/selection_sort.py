def selection_sort(arr):
    n = len(arr)
    
    # Parcourir le tableau
    for i in range(n):
        # Trouver l'indice du plus petit élément non trié
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Échanger l'élément actuel avec le plus petit élément non trié
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemple d'utilisation
if __name__ == "__main__":
    # Demander à l'utilisateur de saisir les éléments du tableau
    input_str = input("Entrez les éléments du tableau séparés par des espaces: ")
    unsorted_array = [int(num) for num in input_str.split()]


    selection_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
