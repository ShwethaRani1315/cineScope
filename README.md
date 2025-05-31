# 🎬 CineScope — Your Personal Movie Recommender
CineScope is a Python-based movie recommendation system that helps users discover movies based on their mood, genres, keywords, or release year — with features to save favorites and more!

## 📌 Features
🎭 Mood-based Recommendations – Suggests genres that match your current mood.

🎞️ Genre Filter – Choose from your favorite genres.

🔍 Keyword Search – Find movies by director names or title keywords.

📆 Year Filter – Explore films from a specific release year.

⭐ Save Favorites – Save movie picks to a custom .csv file.

📂 Real-world Dataset Handling – Cleaned raw data with inconsistent formatting, missing values, and genre standardization.

## 🚀 Getting Started

### Prerequisites
Python 3.x installed in your system

### Running CineScope
1. Clone the Repository
git clone https://github.com/your-username/cinescope.git
cd cinescope
2. Install Requirements
pip install pandas
3. Run the Application
python main.py

## 🧠 How It Works
A cleaned movie dataset is loaded into a pandas DataFrame.

Based on user input, the program filters and recommends top-rated movies.

Results can be saved to a CSV file for future reference.

## 🛠️ Tech Stack
Python 3

Pandas

CSV data handling

Modular design with separate .py files for filtering, mood mapping, and saving.

## 🧹 Data Cleaning Highlights
This project intentionally uses a raw movie dataset to simulate real-world data wrangling challenges:

✅ Removed duplicates

✅ Handled missing reviews and director info

✅ Standardized genres for better matching

✅ Converted inconsistent release year formatting

## 📁 Project Structure
cinescope/
│
├── main.py                # User interaction and control flow
├── mood_handler.py        # Mood-to-genre logic + fuzzy matching
├── movie_filter.py        # All filtering functions (genre, keyword, year)
├── save_favorites.py      # Save recommendations to file
├── file_loader.py         # Loads and cleans raw movie dataset
├── data/
    ├── Movies.csv         # Source data (messy)
    ├── Reviews.csv        # Source data (messy)
    ├── CleanMovies.csv    # Cleaned dataset 
├── notebooks/
    ├── EDA.ipynb          # Data Cleaning and Wrangling
└── README.md              # Project documentation

## 🧑‍💻 Author
Shwetha Rani
📫 shwetharani1315@gmail.com

