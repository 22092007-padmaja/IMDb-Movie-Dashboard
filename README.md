
# IMDb Top 250 Movies Dashboard

## Project Overview
An interactive movie analytics dashboard built using Python, Pandas, and Streamlit. This project explores IMDb Top 250 movie data and provides insights through visualizations, KPIs, and interactive filters.

## Features

### 1. Dataset Analysis
- Load IMDb movie dataset
- Display first 10 records
- Dataset dimensions
- Column names and data types
- Missing value analysis

### 2. Key Performance Indicators
- Total number of movies
- Average IMDb rating
- Highest IMDb rating
- Total number of votes

### 3. Data Visualizations
- Movies by genre
- IMDb rating distribution
- IMDb rating vs number of votes
- Top 10 movies by worldwide gross

### 4. Interactive Movie Explorer
- Filter movies by genre
- Filter by country of origin
- Select IMDb rating range
- Filter by minimum votes
- Search movies by title
- Sort movies by rating
- Display filtered results

### 5. Movie Preference Form
- Save user preferences using Streamlit Session State
- Select movie title and preferred genre
- Set minimum IMDb rating
- Display matching movie information

## Technologies Used
- Python
- Pandas
- Streamlit
- Matplotlib (if used)
- Data Visualization
- Git and GitHub

## Project Structure

```text
IMDb_Movie_Dashboard/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── ToP 250 movies on imdb in 2026.csv
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd IMDb_Movie_Dashboard
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
 streamlit run app.py
```

## Dataset
The dashboard uses an IMDb Top 250 Movies dataset.

Place the CSV file in the project root directory before running the application.

## Author
Padmaja Chandra
