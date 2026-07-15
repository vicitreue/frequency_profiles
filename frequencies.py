from collections import defaultdict
import os

def word_positions(tokenized_sentences: list[list[str]]) -> dict[str, dict]:
    """Analyze the positions of words in tokenized sentences and return a dictionary of word positions."""

    # Store word positions in a dictionary
    word_pos_dict = defaultdict(lambda: defaultdict(int))    
    word_counter: dict[str: int] = {};

    # Iterate through each sentence and count the positions of each word
    for sentence in tokenized_sentences:
        for word_number, word in enumerate(sentence):
            word_pos_dict[word][word_number + 1] += 1 # +1 to make positions 1-indexed
            word_counter[word] = word_counter.get(word, 0) + 1

    # Debugging: Print the top 200 most frequent words and their counts
    print(sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:200])
    print(sorted(word_counter.keys(), key=lambda x: word_counter[x], reverse=True)[:200])

    # Filter the word_pos_dict to only include the top 200 most frequent words
    top_words = [word for word, count in sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:200]] #10 most common
    word_pos_dict = {word: word_pos_dict[word] for word in top_words}

    return dict(word_pos_dict);

def add_zero_frequencies(word:str, word_positions: dict[str, dict]) -> dict[str, dict]:
    max_position = max(word_positions[word].keys())
    for pos in range(1, max_position + 1):
        if pos not in word_positions[word]:
            word_positions[word][pos] = 0
    return word_positions;


def saveFrequencies(frequencies: dict[str, int], corpusName: str):
    """Save the frequencies of words to a text file in the "mostfrequentwords" directory."""

    filename = f"mostfrequentwords/list_{corpusName}.txt"
    full_path = os.path.abspath(filename)

    try:
        # Create directory
        folder_path = os.path.dirname(full_path)
        os.makedirs(folder_path, exist_ok=True)

        # Save txt file with frequencies
        with open(full_path, "w", encoding="utf-8") as f:
            for word, count in frequencies.items():
                f.write(f"{word}: {count}\n")

    except Exception as e:
        print(f"[DEBUG] CRITICAL ERROR OCCURRED: {e}")