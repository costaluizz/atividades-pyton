disponiveis = ["Dom Casmurro","1984","O Pequeno Principe","A Revolução dos Bichos","O Alquimista"]

print(f"Livros Disponiveis: {disponiveis}")
emprestados =[]
reservados = []

disponiveis.remove("1984")
print(f" Livros Disponiveis: {disponiveis}")

emprestados.append("1984")
print(f"Livros Disponiveis:{emprestados}")

disponiveis.remove("O Alquimista")
print(f"Livros Disponiveis: {disponiveis}")

reservados.append("O Alquimista")
print(f"Livros Disponiveis{reservados}")
print(f"Livros Disponiveis:{emprestados}")
print(f"Livros Disponiveis: {disponiveis}")

reservados.remove("O Alquimista")
print(f"Livros Disponiveis{reservados}")
emprestados.append("O Alquimista")
print(f"Livros Disponiveis:{emprestados}")

emprestados.remove("1984")
print(f"Livros Disponiveis:{emprestados}")

disponiveis.append("1984")
print(f"Livros Disponiveis: {disponiveis}")

disponiveis.sort()
print(f"Livros Disponiveis: {disponiveis}")

emprestados.sort()
print(f"Livros Disponiveis:{emprestados}")

print(len(disponiveis))
print(len(emprestados))
print(len(reservados))