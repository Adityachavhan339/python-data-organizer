import os
import pandas as pd
import shutil

print("--- Starting Data Analysis Pipeline ---")

# Phase 1: Folder Setup
folder_name = input("Please enter Name For Project Folder: ")

if os.path.exists(folder_name):
    print(f"Note: Folder '{folder_name}' already exists. Using existing folder.")
else:
    try:
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")
    except Exception as e:
        print(f"Critical Error creating folder: {e}")

# Phase 2: Data Processing
try:
    print("Reading IMDB Dataset...")
    data = pd.read_csv("IMDB Dataset.csv")
    
    # Your Logic
    data["review_length"] = data["review"].str.len()
    positive_500_words = data[(data["sentiment"] == "positive") & (data["review_length"] > 500)]
    
    print("Filtering complete. Saving new updated data file...")
    
    # Phase 3: File Organization (Only runs if Phase 2 succeeds)
    output_name = "IMDB_Positive_Long_Reviews.csv"
    positive_500_words.to_csv(output_name, index=False)
    
    shutil.move(output_name, folder_name)
    
    if not os.path.exists("Backup_IMDB"):
        os.mkdir("Backup_IMDB")
    shutil.copy("IMDB Dataset.csv", "Backup_IMDB")
    
    print(f"Operation Completed Successfully! Files saved in: {folder_name}")

except FileNotFoundError:
    print("Error: Could not find 'IMDB Dataset.csv'. Please ensure it is in this folder.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
