# Frequency Profiles of Common Words in English

## Overview
This program extracts positional frequency profiles from two corpora representing opposite ends of the language spectrum. Written language is represented by the Harry Potter novels by J. K. Rowling, while the Buckeye Corpus (1999-2000) was used for spoken conversational language.

The program identifies the most frequent words in each corpus and analyses how their frequencies are distributed across sentence or utterance positions.

**Usage information**
After downloading the program, save the project folder in your home directory:

/Users/yourUsername/

When the application is run for the first time, it asks for your username. This is used to construct the file path required to access the Buckeye Corpus files. 

If you enter an incorrect username or save the project folder in the wrong directory, the program will not be able to locate the required .txt files. In this case, it terminates and displays the following message in the terminal:

No readable .txt files were found. The program will stop.


## Technologies
This program is written in Python and uses a small number of libraries for text processing, data handling and visulisation. It is an analysis program with minimal dependencies rather than a complete programming environment. 

**Features**
- Extracts word frequency lists from both corpora
- Identifies the most frequent words in each dataset
- Calculates positional frequency profiles across sentences and utterances
- Creates visulisations of the frequency profiles 
- Produces normalised frequency profiles for comparison between both corpora


## Contents
- main.py (main program file)
- tests.py (tests for preprocessing functions)
- BuckeyeCorpus/ (transcription files)


## Installation (Dependencies)

The program requires Python 3 and Git. 

Check whether Git is installed:
git --version

Check whether Python 3 is installed:
python3 --version


If you need to install Git or Python 3, follow the instructions below.

**Linux**
If Git is not installed:
sudo apt update
sudo apt install git

If Python 3 is not installed:
sudo apt install python3

**Mac**
If either command is not recognised, install the required software using Homebrew or the official installers.

**Windows**
The project can be run through Windows Subsystem for Linux (WSL2). Git is generally included with WSL2, but you can install Python with the following commands:

If Python 3 is not installed:
sudo apt update
sudo apt install python3
