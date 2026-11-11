def unigram_probability(corpus: str, word: str) -> float:
    
    words = corpus.split()
    dic = {}

    for w in words:
        if w not in dic:
            dic[w] = 1
        else:
            dic[w] += 1

    return round(dic[word] / len(words), 4)