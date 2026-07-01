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