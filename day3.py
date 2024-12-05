import re

def clean_data(data: str) -> dict[int, tuple]:
    """
    Cleans and organizes input data into a structured format.
    """
    # Unisce tutte le righe rimuovendo spazi e newline
    compact_data = "".join(line.strip() for line in data.splitlines())
    # Restituisce i dati in un dizionario per diverse parti dell'analisi
    return {1: (compact_data,), 2: (compact_data,)}

def calculate_product_sum(data: str) -> int:
    """
    Extracts 'mul(x, y)' patterns and calculates the sum of their products.
    """
    # Trova tutte le occorrenze di 'mul(x, y)' usando espressioni regolari
    matches = re.findall(r"mul\((\d+),(\d+)\)", data)
    # Converte i valori in interi e calcola il prodotto, sommando il tutto
    return sum(int(x) * int(y) for x, y in matches)

def filter_and_process(memory: str) -> int:
    """
    Filters the memory by keeping only segments before 'don't()' within each 'do()'.
    """
    # Divide i segmenti basati su 'do()' e processa ognuno separatamente
    filtered_segments = []
    for segment in memory.split("do()"):
        # Aggiungi il contenuto prima di 'don't()' se presente
        if "don't()" in segment:
            filtered_segments.append(segment.split("don't()")[0])
    # Concatena i segmenti filtrati e calcola la somma dei prodotti
    return calculate_product_sum("".join(filtered_segments))

# Lettura del file di input
with open("day3.txt") as file:
    raw_data = file.read()

# PARTE 1 - Somma dei prodotti
structured_data = clean_data(raw_data)
product_sum = calculate_product_sum(structured_data[1][0])
print(f"Parte 1 - Somma dei prodotti: {product_sum}")

# PARTE 2 - Memoria filtrata
filtered_result = filter_and_process(structured_data[2][0])
print(f"Parte 2 - Risultato memoria filtrata: {filtered_result}")