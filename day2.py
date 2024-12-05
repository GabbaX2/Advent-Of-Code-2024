data = []


with open("day2.txt") as f:
    for line in f:
        data.append([int(x) for x in line.strip().split()])

# PARTE 1

def check_row(result):
    return all(1 <= x <= 3 for x in result)

def is_monotonic(row):
    return row == sorted(row) or row == sorted(row, reverse=True)

valid_rows_count = 0  


for row in data:
    if not is_monotonic(row):
        print(f"Riga non valida (non monotona): {row}")
        continue  
    
    result = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    if check_row(result):
        valid_rows_count += 1 

# print(f"Numero di righe valide: {valid_rows_count}")
        
# PARTE 2

def find_element_to_remove(row):
    row_no_duplicates = list(dict.fromkeys(row))
    
    for i in range(len(row_no_duplicates)):
        modified_row = row_no_duplicates[:i] + row_no_duplicates[i+1:]
        if is_monotonic(modified_row):
            return modified_row, row_no_duplicates[i] 
    return None


corrected_rows = []
valid_rows_count = 0

for row in data:
    if not is_monotonic(row): 
        result = find_element_to_remove(row)
        if result is not None:
            corrected_row, removed_element = result
            corrected_rows.append((row, corrected_row, removed_element))
        else:
            corrected_rows.append((row, None, None)) 
    else:
        valid_rows_count += 1

for original, corrected, removed in corrected_rows:
    if corrected:
        print(f"Riga originale: {original} -> Riga corretta: {corrected} (rimosso: {removed})")
    else:
        print(f"Riga originale: {original} non può essere corretta.")
