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
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Tableau non trié:", unsorted_array)

    selection_sort(unsorted_array)
    print("Tableau trié:", unsorted_array)
