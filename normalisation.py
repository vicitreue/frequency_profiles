
def normalised(word_positions, word, total_corpus_count):
    """Normalise word frequencies by total corpus count."""
    max_position = max(word_positions[word].keys())
    for pos in range(1, max_position + 1):
        if pos not in word_positions[word]:
            word_positions[word][pos] = 0
    return {pos: round((count / total_corpus_count) * 1000000) for pos, count in word_positions[word].items()}

def calculate_percentage(word_positions, word):
    """Calculate the percentage of a word's occurrences in each position."""
    percentage = {}
    total_count = sum(word_positions[word].values())
    for pos in range(1, 11):
        percentage[pos] = round((word_positions[word][pos] / total_count) * 100, 2)        
    return percentage