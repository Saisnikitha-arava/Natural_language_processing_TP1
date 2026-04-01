def implement_cbow(corpus, context_words):
    tokens = corpus.lower().split()
    print(f"Input Context: {context_words}")
    for i, word in enumerate(tokens):
       
        surroundings = []
        if i > 0: surroundings.append(tokens[i-1])
        if i < len(tokens)-1: surroundings.append(tokens[i+1])
        
        if all(item in context_words for item in surroundings) and word not in context_words:
            print(f"Predicted Output: {word}")
            return word


corpus_2 = "Word embeddings are dense vector representations of words"
context = ["word", "are"] 
implement_cbow(corpus_2, context)
