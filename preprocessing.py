import re
import nltk

nltk.download('punkt_tab')
nltk.download('universal_tagset')

# Expand common English contractions in the text
CONTRACTIONS_DICT = {    
    "don't": "do not",
    "dont": "do not",      # in case apostrophe was already missing
    "can't": "can not",
    "cannot": "can not",
    "won't": "will not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "doesn't": "does not",
    "didn't": "did not",
    "couldn't": "could not",
    "shouldn't": "should not",
    "wouldn't": "would not",
    "mightn't": "might not",
    "mustn't": "must not",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "let's": "let us",
    "i'm": "i am",
    "you're": "you are",
    "we're": "we are",
    "they're": "they are",
    "I've": "I have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "i'll": "i will",
    "I'm": "I am",
    "I'll": "I will",
    "you'll": "you will",
    "he'll": "he will",
    "she'll": "she will",
    "it'll": "it will",
    "we'll": "we will",
    "they'll": "they will", 
    "there's": "there is",
    "who's" : "who is",
    "what's" : "what is",
    "where's" : "where is",
    "when's" : "when is",
    "why's" : "why is",
    "i've": "i have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "yknow": "you know",
    "that's": "that is"
    # add more as needed...
}

# Common character names 
NAMES = {
    "harry",
    "ron",
    "hermione",
    "dumbledore",
    "hagrid",
    "snape",
    "weasley",
    "potter",
    "draco",
    "malfoy",
    "sirius",
    "voldemort",
    "luna",
    "george",
    "ginny",
    "lupin"
    # add more as needed...
}

# Common filler words in conversational speech
FILLER_WORDS = {
    'um', 'uh', 'umm', 'uhh', 'hmm', 'mmhmm', 'mm-hmm', 'mhm', 'ahh',
    'erm', 'ah', 'eh', 'lordy', 'yeah', 'yep', 'okay', 'ok', 'mm', 'err',
    'uhuh', 'umhum', 'uh-huh', 'huh', 'hmmm', 'mmmmm', 'uhmmm', 'oh',
    'um-hum', 'uh-hum', 'mm-hum', 'ehh', 'uhm', 'ummm', 'uhhh', 'ohh'
}

####

def normalized_text(raw_text: str) -> str:
    """Normalize the text by replacing special characters."""
    text = re.sub(r'[“”]', "'", raw_text) # left and right double quotation marks
    text = re.sub(r'[‘’]', "'", raw_text) # left and right single quotation marks 
    text = re.sub(r'[—–…]', lambda m: {'—': '-', '–': '-', '…': '...'}[m.group()], text) # em dash, en dash, ellipsis
    return text;

def expand_contractions(text: str) -> str:
    """Removes double quotes before splitting sentences into word tokens. Expands common English contractions in the text."""

    # Remove double quotes to avoid issues with tokenization
    text = re.sub(r"\"", "", text)
    
    # Split the text into words for contraction expansion
    words = text.split()

    # Expand contractions and handle special cases
    expanded = []
    for i, word in enumerate(words):
        w_low = word.lower()
        if (i + 1 < len(words)) and (w_low in CONTRACTIONS_DICT):

            # Special handling for he's / she's / it's => 'is' or 'has'
            if w_low in {"he's", "she's", "it's"}:
                next_word = nltk.word_tokenize(words[i + 1])
                tag = nltk.pos_tag(next_word, tagset='universal') 
                is_verb = (tag[0][1] == "VERB")
                not_ing_verb = not next_word[0].endswith("ing") 
                if is_verb and not_ing_verb: #verb: HAS
                    expanded.append(w_low.replace("'s", " has"))
                else:
                    expanded.append(CONTRACTIONS_DICT[w_low])
            else:
                expanded.append(CONTRACTIONS_DICT[w_low])

        elif (w_low.endswith("’s") or w_low.endswith("'s")) and w_low[:-2] in NAMES:
            expanded.append(w_low[:-2])  # Remove 's
        else:
            expanded.append(word)

    return " ".join(expanded);

def remove_footer(text:str) -> str:
    """Remove footer text "Page | (...) - J.K. Rowling"."""
    return re.sub(r"(?im)^page\s*\|.*$", "", text)

def preprocess(raw_text) -> list[list[str]]:
    """Preprocess the raw text by normalizing, expanding contractions, removing footers, and tokenizing into sentences and words."""

    # Normalize the text and expand contractions
    text = normalized_text(raw_text)
    text = expand_contractions(text)

    # Remove footer and unwanted characters
    text = remove_footer(text)
    text = re.sub(r"[‘’]", "", text)
    text = re.sub(r'[“”]', "", text) 
    text = re.sub(r"[']", "", text)

    # Use NLTK to split text into setences
    sentences = nltk.sent_tokenize(text, language='english')
    
    sentences_cleaned = []
    total_word_counter = 0

    # Clean sentences
    for sentence in sentences:
        # Remove punctuation and extra whitespace
        tokenized_sentence = re.sub(r"[^A-Za-z0-9\s]+", "", sentence)
        tokenized_sentence = re.sub(r"\s+", " ", tokenized_sentence).lower().split() 

        # Only add non-empty sentences
        if tokenized_sentence: 
            total_word_counter += len(tokenized_sentence)
            sentences_cleaned.append(tokenized_sentence)

            # Examples of long sentences that exceed 100 words (for thesis discussion purposes)
            if len(tokenized_sentence) > 100:
                print(f"Sentence Length: {len(tokenized_sentence)} || {' '.join(tokenized_sentence)}")

    print(f"Total word count after cleaning: {total_word_counter}")


    # List of tokenized sentences
    return sentences_cleaned;


def clean_buckeye_transcript(raw_text: str) -> list[list[str]]:
    """Clean the Buckeye Corpus transcript by normalising, expanding contractions, removing filler words, and splitting into sentences and words."""

    # Normalize the text and expand contractions
    text = normalized_text(raw_text)
    text = expand_contractions(text)

    # Remove filler words
    text = ' '.join([w for w in text.split() if w.lower() not in FILLER_WORDS]) 

    # Split on <SIL> tags
    utterances:list[str] = re.split(r'<SIL\s*>', text, flags=re.IGNORECASE)

    cleaned_utterances = []
    total_word_counter = 0

    # Clean each utterance
    for utt in utterances:
        # Remove all remaining tags (<VOCNOISE>, <IVER>, <UNKNOWN>, <EXCLUDE-name>, etc.)
        utt = re.sub(r'<[^>]+>', ' ', utt)

        # Remove punctuation and extra whitespace
        utt = re.sub(r"[^A-Za-z0-9\s]+", "", utt) 
        utt = re.sub(r"\s+", " ", utt).lower().split() 

        # Only add non-empty utterances
        if utt: 
            total_word_counter += len(utt)
            cleaned_utterances.append(utt)

    print(f"Total word count after cleaning (Buckeye): {total_word_counter}")
    return cleaned_utterances