def implement_skip_gram(corpus, target_word, window_size=1):
    tokens = corpus.lower().split()
    if target_word not in tokens: return "Target not in corpus"
    
    target_idx = tokens.index(target_word)
    start = max(0, target_idx - window_size)
    end = min(len(tokens), target_idx + window_size + 1)
    
    context = [tokens[i] for i in range(start, end) if i != target_idx]
    
    print(f"Input: {target_word}")
    print(f"Target Output (Context): {context}")

implement_skip_gram("word embedding are awesome", "embedding")
