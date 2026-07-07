import os

import matplotlib.pyplot as plt
import seaborn as sns

def plot_word_positions(word_pos_dict: dict[str, dict], word: str, normalized:bool = False, corpusName: str = "", index:int = 0):
    # Plot the distribution of word positions for a specific word (e.g., "i")
    if word not in word_pos_dict:
        print(f"The word '{word}' was not found in the text.")
        return

    normalized_str = "normalized" if normalized else ""

    sorted_positions = dict(sorted(word_pos_dict[word].items()))
    keys = list(sorted_positions.keys())[:60] # limit to top 60 positions for better visualization
    values = [float(sorted_positions[k]) for k in keys]

    # Calulations for debugging and analysis
    total_count = sum(values)
    print(f"---- Total count for word '{word}': {total_count} || first 60 positions")
    
    # Create a bar plot using matplotlib and seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_visible(False)

    ax = sns.barplot(x=keys, y=values, dodge=False, ax=ax, palette='viridis', legend=False)
    ax.set_title(f" ", fontsize=12)
    for bars_group in ax.containers:
        ax.bar_label(bars_group, padding=3, fontsize=6)

    desired_ticks = list(range(4, int(max(values)), 5))
    desired_tick_labels = [pos + 1 for pos in desired_ticks]
    ax.set_xticks(desired_ticks)
    ax.set_xticklabels(desired_tick_labels)
    ax.set_xlim(1, None)

    plt.xlabel("Position in sentence")
    plt.ylabel("Count")

    plt.xlim(0, max(keys) + 1)   # gives space on both left and right
    plt.ylim(0, max(values)*1.1)

    plt.xlim(-0.6, len(keys) + 1)   # gives space on both left and right
    plt.ylim(0, max(values) * 1.1)   # more headroom for the tall labels   

    sns.despine()
    plt.tight_layout()

    # save bar plot to a local folder instead of showing it 
    filename = f"plots/{corpusName}/{index}_{word}_{normalized_str}.png" if normalized else f"plots/{corpusName}/{index}_{word}.png"
    full_path = os.path.abspath(filename)

    try:
        # 1. Create directory
        folder_path = os.path.dirname(full_path)
        os.makedirs(folder_path, exist_ok=True)
    
        # 2. Save plot
        plt.savefig(full_path)
        plt.close() # Frees memory
        print(f"[DEBUG] SUCCESS! File generated at: {full_path}")

    except Exception as e:
        print(f"[DEBUG] CRITICAL ERROR OCCURRED: {e}")


    #plt.show()
