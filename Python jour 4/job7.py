L = [8, 24, 48, 2, 16]

count_multiples_of_3 = sum(1 for num in L if num % 3 == 0)

print("Le nombre de multiples de 3 dans la liste est:", count_multiples_of_3)