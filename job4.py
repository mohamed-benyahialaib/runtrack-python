def multiplication_tables(N):
    for i in range(1, N+1):
        print(f"Table de multiplication de {i}:")
        for j in range(1, 11):
            print(f"{i}*{j}={i*j}")
        print()

N=10
multiplication_tables(N)