col1 = []
col2 = []

with open("day1.txt") as f:
    for lines in f:
        val = lines.split()
        col1.append(int(val[0]))
        col2.append(int(val[1]))

# print(f'col1: {col1} and col2: {col2}')

# PARTE 1

col1.sort()
col2.sort()

result = []

for i in range(len(col1)):
    if col1[i] > col2[i]:
        result.append(col1[i] - col2[i])
    else:
        result.append(col2[i] - col1[i])

print(f'risultati confronto: {result}')

ans = sum(result)
print(f'the answer of this challenge is: {ans}!')

# PARTE 2
counter = 0

res2 = []

for i in range(len(col1)):
    if col1[i] == col2[i]:
        counter += 1
        res2.append(col1[i] * counter)
    else:
        pass
        
# PARTE 2
counter = 0

res2 = []

for val in col1:
    count_in_col2 = col2.count(val)  # Conta le occorrenze in col2
    if count_in_col2 > 0:
        res2.append(val * count_in_col2)  # Moltiplica l'elemento per il numero di occorrenze

print(res2)

finalRes = sum(res2)
print(f'risultato finale: {finalRes}!')
