# python-data-organizer
# IMDB Data Automation Pipeline 🎬

A Python-based automation tool designed to process large-scale sentiment data, perform custom analysis, and organize the file system with built-in error handling.

## 🚀 Overview
This project demonstrates a complete data workflow from ingestion to organization. It handles the "IMDB Dataset" by calculating review metrics, filtering specific sentiment criteria, and automating the directory structure for project management.

## 🛠️ Key Features
- **Data Engineering:** Uses `Pandas` to calculate string lengths and filter high-value reviews.
- **Automated File System:** Uses `os` and `shutil` to create project directories and manage file backups.
- **Robust Error Handling:** Implements `try-except` blocks to manage common issues like missing files or permission errors without crashing the script.
- **User Interaction:** Dynamic folder naming based on user input.

## 📂 Logic Flow
1. **Environment Setup:** Checks for existing directories and creates a new project workspace.
2. **Data Transformation:** Reads the IMDB CSV, generates a `review_length` column, and extracts positive reviews with >500 characters.
3. **Archive & Organization:** Generates a cleaned CSV, moves it to the project folder, and creates a timestamped-style backup of the source data.

## 💻 How to Use
1. Ensure `IMDB Dataset.csv` is in the root directory.
2. Run the script: `python your_script_name.py`
3. Enter your desired project name when prompted.

## 🧠 Lessons Learned
- Mastering Python indentation for nested logic.
- Implementing "Safety Nets" using `except Exception as e` to debug real-time issues.
- Coordinating multiple libraries (`pandas`, `os`, `shutil`) to work in a single pipeline.
