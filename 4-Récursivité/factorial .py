def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Exemple d'utilisation
if __name__ == "__main__":
    num = 3
    result = factorial(num)
    print(f"Le factoriel de {num} est : {result}")
