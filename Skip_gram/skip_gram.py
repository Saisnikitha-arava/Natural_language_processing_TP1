def get_neighbors(corpus, target_word, window_size=2):
    tokens = corpus.lower().split()
    neighbors = []
    
    if target_word.lower() not in tokens:
        return "Word not found."

    idx = tokens.index(target_word.lower())
    start = max(0, idx - window_size)
    end = min(len(tokens), idx + window_size + 1)
    for i in range(start, end):
        if i != idx:
            neighbors.append(tokens[i])
    return neighbors
corpus_text = "The Brown Fox jumps on Lazy Dog"
target = "Fox"
print(f"Neighbors of '{target}':", get_neighbors(corpus_text, target))
