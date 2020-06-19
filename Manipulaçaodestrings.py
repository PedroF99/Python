# Mostrar String no ecra
s = "Pedro Ferreira"
print(s)

# Ver o tipo da string
print(type(s))

# Ver o tamanho de uma string.
print(len(s))


# Faz a troca de algu na string por outra coisa 
sub = s.replace("Ferreira", "Filipe")

print(sub)

# Vê se a string começa por pedro
print(s.startswith("Pedro"))

# Vê se a string acaba com ferreira 
print(s.endswith("Ferreira"))

# conta quantas vezes a palavra pedro aparece na string 
print(sub.count("Pedro"))