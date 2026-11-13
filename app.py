
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
st.title("IMDb Top 250 Movies Dashboard")
st.subheader("Movie Analytics and Data Exploration")
df = pd.read_csv("ToP 250 movies on imdb in 2026.csv")
st.success("Dataset loaded successfully!")
# Initialize session state
if "user_preferences" not in st.session_state:
    st.session_state.user_preferences = {
        "movie_title": "",
        "genre": "",
        "min_rating": 0.0
    }
st.header("Dataset Preview")
st.dataframe(df.head(10))
st.header("Dataset Information")
st.write("Total Rows:", df.shape[0])
st.write("Total Columns:", df.shape[1])
st.write("Column Names:", df.columns.tolist())
st.write("Data Types:")
st.write(df.dtypes)
st.header("Missing Values")
st.write(df.isnull().sum())
st.header("Movie Analytics Dashboard")
total_movies = df.shape[0]
average_rating = df["averageRating"].mean()
highest_rating = df["averageRating"].max()
total_votes = df["numVotes"].sum()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Movies", total_movies)
col2.metric("Average Rating", round(average_rating, 2))
col3.metric("Highest Rating", highest_rating)
col4.metric("Total Votes", f"{total_votes:,}")
st.header("Dataset Columns")
st.write(df.columns.tolist())
genre_count = df["genres"].str.split(",").explode()
genre_count = genre_count.value_counts()
st.bar_chart(genre_count)
st.header("Data Visualization")

st.subheader("1. Genre-wise Movie Count")
genre_count = df["genres"].dropna().str.split(",").explode()
genre_count = genre_count.value_counts()
st.bar_chart(genre_count)  


st.subheader("2. IMDb Rating Distribution")
rating_data = pd.to_numeric(
    df["averageRating"], errors="coerce"
).dropna()
fig, ax = plt.subplots()
ax.hist(rating_data, bins=10)
ax.set_title("IMDb Rating Distribution")
ax.set_xlabel("IMDb Rating")
ax.set_ylabel("Number of Movies")
st.pyplot(fig)

plt.close(fig)

st.subheader("3. IMDb Rating vs Number of Votes")
scatter_data = df[["averageRating", "numVotes"]].dropna()
st.scatter_chart(
    scatter_data,
    x="averageRating",
    y="numVotes"
)
st.subheader("4. Top 10 Movies by Worldwide Gross")
top_movies = df.sort_values(
    by="grossWorldwide",
    ascending=False
).head(10)
st.bar_chart(
    top_movies,
    x="primaryTitle",
    y="grossWorldwide"
)

# Question 4: Dashboard Layout

st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])

# TAB 1: Genre Analysis
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)


# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )


# Question 4: Dashboard Layout

st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])

# TAB 1: Genre Analysis
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)


# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )


st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])

# TAB 1: Genre Analysis
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)


# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )



# Question 4: Dashboard Layout

st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])

# TAB 1: Genre Analysis
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)


# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )


st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)


# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )
st.header("Movie Data Visualizations")

# Create three tabs
tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])
with tab1:

    st.subheader("Genre-wise Movie Count")

    genre_count = df["genres"].dropna().str.split(",").explode()

    genre_count = genre_count.value_counts()

    st.bar_chart(genre_count)
# TAB 2: Rating Analysis
with tab2:

    st.subheader("IMDb Rating Distribution")

    rating_data = pd.to_numeric(
        df["averageRating"], errors="coerce"
    ).dropna()

    rating_bins = pd.cut(rating_data, bins=10)

    rating_count = rating_bins.value_counts().sort_index()

    rating_count.index = rating_count.index.astype(str)

    st.bar_chart(rating_count)

    st.divider()

    st.subheader("IMDb Rating vs Number of Votes")

    scatter_data = df[
        ["averageRating", "numVotes"]
    ].dropna()

    st.scatter_chart(
        scatter_data,
        x="averageRating",
        y="numVotes"
    )
with tab3:
    st.subheader("Top 10 Movies by Worldwide Gross")

    top_movies = df.sort_values(
        by="grossWorldwide",
        ascending=False
    ).head(10)

    st.bar_chart(
        top_movies,
        x="primaryTitle",
        y="grossWorldwide"
    )
with st.expander("View Dataset Information"):

    st.write("Total Movies:", df.shape[0])

    st.write("Total Columns:", df.shape[1])

    st.write("Column Names:", df.columns.tolist())

    st.write("Available Movie Information:")

    st.write(df.dtypes)
st.divider()
col4.metric("Total Votes", f"{total_votes:,}")

st.divider()

st.header("Movie Data Visualizations")
st.info("Explore IMDb movie statistics using the tabs below.")
st.subheader("Available Dataset Columns")
st.write(df.columns.tolist())

st.subheader("Sample Movie Data")
st.write(df.head(5))
st.header("Interactive Movie Explorer")

# Create a copy of the dataset
filtered_df = df.copy()

# Get all available genres
all_genres = sorted(set(
    genre.strip()
    for value in df["genres"].dropna()
    for genre in str(value).split(",")
))
selected_genre = st.selectbox(
    "Select Genre",
    ["All"] + all_genres
)

# Apply genre filter
if selected_genre != "All":
    filtered_df = filtered_df[
        filtered_df["genres"].fillna("").str.contains(
            selected_genre, case=False, regex=False
        )
    ]

st.write("Movies after Genre Filter:", len(filtered_df))
st.dataframe(filtered_df)
all_countries = sorted(
    set(
        country.strip()
        for value in df["countriesOfOrigin"].dropna()
        for country in str(value).split(",")
    )
)
selected_countries = st.multiselect(
    "Select Countries",
    all_countries
)
if selected_countries:
    filtered_df = filtered_df[
        filtered_df["countriesOfOrigin"].fillna("").apply(
            lambda x: any(
                country in [c.strip() for c in str(x).split(",")]
                for country in selected_countries
            )
        )
    ]

st.write("Movies after Country Filter:", len(filtered_df))
min_rating = float(df["averageRating"].min())
max_rating = float(df["averageRating"].max())

selected_rating = st.slider(
    "Select IMDb Rating Range",
    min_value=min_rating,
    max_value=max_rating,
    value=(min_rating, max_rating),
    step=0.1
)
filtered_df = filtered_df[
    (filtered_df["averageRating"] >= selected_rating[0]) &
    (filtered_df["averageRating"] <= selected_rating[1])
]

st.write("Movies after Rating Filter:", len(filtered_df))
# Minimum votes input
min_votes = st.number_input(
    "Enter Minimum Number of Votes",
    min_value=0,
    value=0,
    step=1000
)

filtered_df = filtered_df[
    filtered_df["numVotes"] >= min_votes
]
st.write("Movies after Votes Filter:", len(filtered_df))
# Movie title search
search_title = st.text_input(
    "Search Movie by Title"
)

# Apply title filter
if search_title:
    filtered_df = filtered_df[
        filtered_df["primaryTitle"].str.contains(
            search_title,
            case=False,
            na=False
        )
    ]

st.write("Movies after Title Search:", len(filtered_df))
# Sorting option
sort_order = st.radio(
    "Sort Movies by Rating",
    ["Ascending", "Descending"],
    horizontal=True
)
if sort_order == "Ascending":
    filtered_df = filtered_df.sort_values(
        by="averageRating",
        ascending=True
    )
else:
    filtered_df = filtered_df.sort_values(
        by="averageRating",
        ascending=False
    )

st.write("Movies after Sorting:", len(filtered_df))
st.subheader("Filtered Movie Results")

st.success(f"Total Movies Found: {len(filtered_df)}")
st.dataframe(filtered_df, use_container_width=True)
if st.button("Reset Filters"):
    st.rerun()
st.header("Movie Preference Form")
with st.form("movie_preference_form"):

    movie_title = st.text_input("Enter Movie Title")

    preferred_genre = st.selectbox(
        "Select Preferred Genre",
        all_genres
    )

    minimum_rating = st.slider(
        "Select Minimum Rating",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

    submit = st.form_submit_button("Submit Preferences")

    if submit:
        st.session_state.user_preferences = {
            "movie_title": movie_title,
            "genre": preferred_genre,
            "min_rating": minimum_rating
        }

        st.success("Your preferences have been saved!")
# Display selected movie information
st.subheader("Selected Movie Information")

preferences = st.session_state.user_preferences

if preferences["movie_title"]:

    movie_data = df[
        df["primaryTitle"].str.contains(
            preferences["movie_title"],
            case=False,
            na=False
        )
        &
        (df["genres"].fillna("").str.contains(
            preferences["genre"],
            case=False,
            regex=False
        ))
        &
        (df["averageRating"] >= preferences["min_rating"])
    ]

    if not movie_data.empty:

        st.success("Matching movies found!")

        st.dataframe(
            movie_data[
                ["primaryTitle", "genres", "averageRating", "numVotes"]
            ],
            use_container_width=True
        )

    else:
        st.info("No movies match your selected preferences.")

else:
    st.info("Please submit your movie preferences to see the results.")
st.subheader("Saved User Preferences")

st.write(
    "Movie Title:",
    st.session_state.user_preferences["movie_title"]
)

st.write(
    "Preferred Genre:",
    st.session_state.user_preferences["genre"]
)

st.write(
    "Minimum Rating:",
    st.session_state.user_preferences["min_rating"]
)