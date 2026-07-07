from collections import defaultdict

# Analyze word positions in sentences
def word_positions(tokenized_sentences: list[list[str]]) -> dict[str, dict]:
    # Store word positions in a dictionary
    word_pos_dict = defaultdict(lambda: defaultdict(int))    
    word_counter: dict[str: int] = {};

    # Iterate through each sentence and count the positions of each word
    for sentence in tokenized_sentences:
        for word_number, word in enumerate(sentence):
            word_pos_dict[word][word_number + 1] += 1 # +1 to make positions 1-indexed
            word_counter[word] = word_counter.get(word, 0) + 1

    print(sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:200]) # print top 100 most common words;
    print(sorted(word_counter.keys(), key=lambda x: word_counter[x], reverse=True)[:200])

    top_words = [word for word, count in sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:200]] #10 most common
    word_pos_dict = {word: word_pos_dict[word] for word in top_words}

    return dict(word_pos_dict);

def add_zero_frequencies(word:str, word_positions: dict[str, dict]) -> dict[str, dict]:
    max_position = max(word_positions[word].keys())
    for pos in range(1, max_position + 1):
        if pos not in word_positions[word]:
            word_positions[word][pos] = 0
    return word_positions;