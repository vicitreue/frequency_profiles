import importing_files
import preprocessing
import normalisation
import create_plots
import frequencies
import tests

import kagglehub
PATH = kagglehub.dataset_download("rupanshukapoor/harry-potter-books")

# TODO: save 100 most comon words to a seperate folder with counts



def main():  

    #### TESTS ####
    tests.standardization_test() #1
    tests.preprocessing_test() #2
    #print("Word positions: ", word_positions_dict.get("i"), {}) #3
    #importing_files.load_text_from_local_file("Bachelorarbeit 2026/BuckeyeCorpus") # DEBUG

    ################

    # Loading texts from their respective files
    harry_potter_books = importing_files.load_text_from_file(kagglehub.dataset_download("rupanshukapoor/harry-potter-books"))
    buckeye_transcripts = importing_files.load_text_from_file("/Users/vicitreue/Bachelorarbeit 2026/BuckeyeCorpus")


    # BUCKEYE CORPUS
    all_texts_buckeye = importing_files.join_texts(buckeye_transcripts)

    # Preprocess the text
    cleaned_sentences_conversational = preprocessing.clean_buckeye_transcript(all_texts_buckeye)

    # Word positions 
    word_positions = frequencies.word_positions(cleaned_sentences_conversational)

    normalised_word_positions = {}
    for index, word in enumerate(word_positions):
        word_positions = frequencies.add_zero_frequencies(word, word_positions)
        normalised_word_positions[word] = normalisation.normalised(word_positions, word, 153770)

        # Percentage of occurrences in the first 10 positions for the word
        percentage = normalisation.calculate_percentage(word_positions, word)
        print(f"Percentage of occurrences in the first 10 positions for word '{word}': {percentage}")

        # Create plots for the word positions and normalised word positions
        create_plots.plot_word_positions(word_positions, word, False, "buckeye", index + 1)
        create_plots.plot_word_positions(normalised_word_positions, word, True, "buckeye", index + 1)

    # HARRY POTTER BOOKS
    all_texts_hp = importing_files.join_texts(harry_potter_books)

    # Preprocess the text
    all_texts_hp = preprocessing.remove_footer(all_texts_hp)
    sentences = preprocessing.preprocess(all_texts_hp)

    # Word positions 
    word_positions_dict = frequencies.word_positions(sentences)

    normalised_word_positions_dict = {}
    for index, word in enumerate(word_positions_dict):
        word_positions_dict = frequencies.add_zero_frequencies(word, word_positions_dict)
        normalised_word_positions_dict[word] = normalisation.normalised(word_positions_dict, word, 1105125)

        # Percentage of occurrences in the first 10 positions for the word
        percentage = normalisation.calculate_percentage(word_positions_dict, word)
        print(f"Percentage of occurrences in the first 10 positions for word '{word}': {percentage}")
        
        # Create plots for the word positions and normalised word positions
        create_plots.plot_word_positions(word_positions_dict, word, False, "hp", index + 1)
        create_plots.plot_word_positions(normalised_word_positions_dict, word, True, "hp", index + 1)

if __name__ == "__main__":
    main();