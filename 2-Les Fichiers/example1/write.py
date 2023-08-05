content = """Ceci est un nouveau fichier créé en Python.
Nous allons écrire ce contenu dans le fichier."""

with open("new_file.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Le contenu a été écrit dans le fichier 'new_file.txt'.")

