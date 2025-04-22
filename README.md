# 🎙️ Podcast Reviews Analysis

## 📊 Overview
This project analyzes a large-scale podcast review dataset containing 2 million reviews across 100,000 podcasts. The dataset is updated monthly and provides valuable insights into podcast consumption and user preferences.

## 📚 Dataset
The analysis uses the Podcast Reviews dataset from [Kaggle](https://www.kaggle.com/datasets/thoughtvector/podcastreviews/versions/28), which includes:
- Podcast information
- User reviews
- Categories
- Rating data

The data is stored in a SQLite database (`podcast.sqlite`) with the following tables:
- `categories`: Links podcasts to their categories
- `podcasts`: Contains podcast metadata (ID, iTunes info, titles)
- `reviews`: User reviews and ratings
- `runs`: Dataset update tracking information

## ⭐ Key Findings

### 1. Rating Distribution & Trends
- Approximately 87% of podcast ratings are 5-star, with another 3% being 4-star
- Review volume has increased significantly from 2006 to 2023
- Peak review activity occurred during the COVID-19 period (2021-mid 2022)
- Post-pandemic period shows a declining trend in review numbers

### 2. 📈 Category Analysis
- Highest rated podcasts tend to be in relaxing/positive topics:
  - Hobby-related content
  - Self-improvement
  - Fitness
- Lowest rated categories are typically more controversial topics:
  - News
  - Crime
  - Politics
  - Government-related content
- There is a slight to moderate negative correlation (-0.21) between category ratings and review numbers

### 3. ⏰ Temporal Patterns
- Review Activity:
  - Peak review hours: Afternoon to pre-dinner hours
  - Lowest review activity: Morning hours (6:00-11:00)
- Morning Hours Analysis:
  - Significantly lower proportion of positive ratings
  - High-rated podcasts receive fewer reviews
  - Higher proportion of negative-only reviewers are active
  - Statistical analysis confirms these patterns with 95% confidence

### 4. 👥 User Behavior
- Most users give highly positive ratings (4-5 stars)
- Distinct group of users who only give negative ratings (1-2 stars)
- Morning reviewers show different rating patterns compared to other times
- Review patterns suggest different content preferences based on time of day

## 📁 Project Structure

├── project.ipynb # Main analysis notebook
├── helper/ # Helper functions and utilities
├── podcast.sqlite # SQLite database containing the dataset
├── Pipfile # Pipenv dependencies
├── requirements.txt # Python package requirements
└── README.md # Project documentation


## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Seaborn
- DuckDB (for efficient SQL queries on pandas DataFrames)
- SQLite

## 🚀 Setup and Installation

1. Clone the repository
2. Install dependencies using either:
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # OR using Pipenv
   pipenv install
   ```

3. Make sure you have the `podcast.sqlite` database file in your project root directory

## 💡 Usage
The main analysis can be found in `project.ipynb`. The notebook includes:
- Data loading and preprocessing
- Exploratory data analysis
- Visualization of podcast trends
- Review analysis
- Statistical testing and inference

## 🔄 Future Improvements
1. Implement sentiment analysis on review content
2. Develop user clustering based on podcast preferences and rating patterns
3. Define more precise metrics for:
   - Polarized reviews
   - Morning-only reviewers
   - Other temporal patterns

## 📦 Dependencies
Key dependencies include:
- numpy
- pandas
- seaborn
- duckdb
- matplotlib

For a complete list of dependencies, see `Pipfile`.