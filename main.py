import importing_files
import preprocessing
import normalisation
import create_plots
import frequencies
import tests

import kagglehub
PATH = kagglehub.dataset_download("rupanshukapoor/harry-potter-books")


def main():  

    #### TESTS ####
    tests.standardization_test() #1
    tests.preprocessing_test() #2
    tests.word_positions_test() #3
    ################

    # file path /Users/USERNAME/Semantic of Words/BuckeyeCorpus
    username = input("Enter your username: ")

    # Loading texts from their respective files
    harry_potter_books = importing_files.load_text_from_file(kagglehub.dataset_download("rupanshukapoor/harry-potter-books"))
    buckeye_transcripts = importing_files.load_text_from_file(f"/Users/{username}/Semantics of Words/BuckeyeCorpus")

    ## BUCKEYE CORPUS ##
    all_texts_buckeye = importing_files.join_texts(buckeye_transcripts)

    # Preprocess the text
    cleaned_sentences_conversational = preprocessing.clean_buckeye_transcript(all_texts_buckeye)

    # Word positions 
    word_positions = frequencies.word_positions(cleaned_sentences_conversational)
    frequencies.saveFrequencies({word: sum(positions.values()) for word, positions in word_positions.items()}, "buckeye")

    # Normalise word positions and create plots for the top 10 words and specific words of interest
    normalised_word_positions = {}
    for index, word in enumerate(word_positions):

        # Add zero frequencies for missing positions and normalise the word positions
        word_positions = frequencies.add_zero_frequencies(word, word_positions)
        normalised_word_positions[word] = normalisation.normalised(word_positions, word, 153770)

        # Create plots for the word positions and normalised word positions
        if index < 10 or word in ["people", "things", "time", "year", "stuff", "person", "school", "kids", "years", "life", "thing", "parents", "mom", "home", "work", "way", "family", "money", "children", "house"]:
            
            # Percentage of occurrences for the word
            percentage = normalisation.calculate_percentage(word_positions, word)
            print(f"Percentage of occurrences for '{word}': {percentage}")
            
            # Create plots for the word positions and normalised word positions
            create_plots.plot_word_positions(word_positions, word, False, "buckeye", index + 1)
            create_plots.plot_word_positions(normalised_word_positions, word, True, "buckeye", index + 1)
    ## END ## (Buckeye Corpus)


    ## HARRY POTTER BOOKS ##
    all_texts_hp = importing_files.join_texts(harry_potter_books)

    # Preprocess the text
    all_texts_hp = preprocessing.remove_footer(all_texts_hp)
    sentences = preprocessing.preprocess(all_texts_hp)

    # Word positions 
    word_positions_dict = frequencies.word_positions(sentences)
    frequencies.saveFrequencies({word: sum(positions.values()) for word, positions in word_positions_dict.items()}, "hp")

    normalised_word_positions_dict = {}
    for index, word in enumerate(word_positions_dict):
        word_positions_dict = frequencies.add_zero_frequencies(word, word_positions_dict)
        normalised_word_positions_dict[word] = normalisation.normalised(word_positions_dict, word, 1105125)

        # Percentage of occurrences for the word
        percentage = normalisation.calculate_percentage(word_positions_dict, word)
        print(f"Percentage of occurrences for '{word}': {percentage}")
        
        # Create plots for the word positions and normalised word positions
        if index < 10 or word in ["ron", "hermione", "dumbledore", "hagrid", "snape", "malfoy", "voldemort", "sirius", "lupin", "potter", "ginny", "george", "fred", "weasley", "hogwarts", "time", "face", "voice", "room", "eyes", "way", "hand", "feet", "fire", "death", "professor", "wand", "people", "moment", "table"]:
            create_plots.plot_word_positions(word_positions_dict, word, False, "hp", index + 1)
            create_plots.plot_word_positions(normalised_word_positions_dict, word, True, "hp", index + 1)
    
    ## END ## (Harry Potter books)

if __name__ == "__main__":
    main();