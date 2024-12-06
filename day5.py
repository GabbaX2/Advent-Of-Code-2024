from collections import defaultdict


# Funzione per leggere le regole e gli aggiornamenti
def parse_input(filename):
    rules = []
    updates = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                rules.append(tuple(map(int, line.split("|"))))
            elif line:
                updates.append(list(map(int, line.split(","))))

    # Crea la mappa "prima di" (before)
    before = defaultdict(set)
    for b, a in rules:
        before[a].add(b)
    return updates, before


# Funzione per controllare se un aggiornamento è in ordine
def is_ordered(update, before):
    update_set = set(update)
    for i, page in enumerate(update):
        # Conta quante pagine che devono venire prima sono già presenti nell'update
        required_pages = before[page] & update_set
        if len(required_pages) != i:
            return False
    return True


# Funzione per riordinare un aggiornamento
def reorder(update, before):
    update_set = set(update)
    ordered_update = [0] * len(update)
    for page in update:
        # Determina la posizione corretta contando quante pagine devono venire prima
        position = len(before[page] & update_set)
        ordered_update[position] = page
    return ordered_update


# Parte 1: Somma le pagine centrali degli aggiornamenti validi
def part1(filename):
    updates, before = parse_input(filename)
    midpages_sum = 0
    for update in updates:
        if is_ordered(update, before):
            midpages_sum += update[len(update) // 2]
    return midpages_sum


# Parte 2: Correggi e somma le pagine centrali degli aggiornamenti non validi
def part2(filename):
    updates, before = parse_input(filename)
    midpages_sum = 0
    for update in updates:
        if not is_ordered(update, before):
            ordered_update = reorder(update, before)
            midpages_sum += ordered_update[len(update) // 2]
    return midpages_sum


# Esegui le due parti
if __name__ == "__main__":
    # print("Parte 1 (Esempio):", part1("day5.txt"))
    print("Parte 1:", part1("day5.txt"))
    # print("Parte 2 (Esempio):", part2("day5.txt"))
    print("Parte 2:", part2("day5.txt"))
