from collections import defaultdict

import frequencies
import preprocessing

def standardization_test():
    # Test the preprocessing function with a sample text
    sample_text = "Harry’s bag isn’t on his back… but don't tell him. It’s his – fault and I couldn’t be bothered. I’m Ron's father."
    expected_output = "harry bag is not on his back... but do not tell him. it is his - fault and I could not be bothered. i am ron father."
    normalized = preprocessing.normalized_text(sample_text)
    assert preprocessing.expand_contractions(normalized) == expected_output, "Standardization test failed!"
    print("Standardization test passed!")

def preprocessing_test():
    # Test the preprocessing function with a sample text
    sample_text = ' "there\'s more in the frying pan, sweetums," said Aunt Petunia, turning misty eyes on her massive son. "We must build you up while we\'ve got the chance. ... I don\'t like the sound of that school food. ...'
    expected_output = [['there', 'is', 'more', 'in', 'the', 'frying', 'pan', 'sweetums', 'said', 'aunt', 'petunia', 'turning', 'misty', 'eyes', 'on', 'her', 'massive', 'son'], ['we', 'must', 'build', 'you', 'up', 'while', 'we', 'have', 'got', 'the', 'chance'], ['i', 'do', 'not', 'like', 'the', 'sound', 'of', 'that', 'school', 'food']]
    assert preprocessing.preprocess(sample_text) == expected_output, "Preprocessing test failed!"
    print("Preprocessing test passed!")

def word_positions_test():
    # Test the word_positions function with a sample tokenized sentences
    sample_tokenized_sentences = [['i', 'love', 'python'], ['python', 'is', 'great'], ['i', 'love', 'coding']]
    expected_output = {
        'i': {1: 2},
        'love': {2: 2},
        'python': {1: 1, 3: 1},
        'is': {2: 1},
        'great': {3: 1},
        'coding': {3: 1}
    }

    print("Word positions test: ", frequencies.word_positions(sample_tokenized_sentences))
    assert frequencies.word_positions(sample_tokenized_sentences) == expected_output, "Word positions test failed!"
    print("Word positions test passed!")