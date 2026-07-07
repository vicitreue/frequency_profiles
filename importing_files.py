import os

def load_text_from_file(file_path: str) -> dict[str: str]:
    # Load text from a file and return it as a list of strings
    books = {};

    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        books[file] = f.read()

                except Exception as e:
                    print(f"Failed to read {file}: {e}")    
    if not books:
        print("No readable .txt files were found. The program will stop.")
        raise SystemExit(1)     
    return books;

def join_texts(texts: dict[str: str]) -> str:
    # Join the texts into a single string
    return "\n".join(texts.values())



# load text from a file in folder "Bachelorarbeit 2026/BuckeyeCorpus" and return it as a list of strings
def load_text_from_local_file(file_path: str) -> dict[str: str]:
    transcripts = {};
    files = os.listdir(file_path)

    for file in files:
        print(f"Found file: {file}") # DEBUG
        if file.endswith(".txt"):
            file_path_with_file = f"{file_path}/{file}"
            #print(f"Attempting to read file: {file_path}") # DEBUG

            try:
                with open(file_path_with_file, "r", encoding="utf-8") as f:
                    transcripts[file] = f.read()

            except Exception as e:
                print(f"Failed to read {file}: {e}")       
    return transcripts;