
import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
SUMMARY_DIR = BASE_DIR / "reports" / "summaries_data"


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Review Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Load JSON summary files
# --------------------------------------------------

def load_json(filename):
    file_path = SUMMARY_DIR / filename

    if not file_path.exists():
        st.error(f"Summary file not found: {file_path}")
        st.stop()

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_dataframe(filename):
    return pd.DataFrame(load_json(filename))


categories = load_json("category_summary.json")
sentiment = load_dataframe("sentiment_distribution.json")
ratings = load_dataframe("category_ratings.json")
by_category = load_dataframe("sentiment_by_category.json")


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Amazon Review Analytics")

st.write(
    "Explore sentiment distribution, product performance, "
    "and customer feedback across Amazon product categories."
)

st.divider()


# --------------------------------------------------
# Overall statistics
# --------------------------------------------------

total_reviews = sum(
    category["reviews_in_category"]
    for category in categories
)

total_products = 39  # Total unique products in the dataset

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Reviews", f"{total_reviews:,}")

with col2:
    st.metric("Categories", len(categories))

with col3:
    st.metric("Products Analysed", total_products)

st.divider()


# --------------------------------------------------
# Product category overview
# --------------------------------------------------

st.subheader("📦 Product Categories")

category_df = pd.DataFrame([
    {
        "Category": category["category"],
        "Reviews": category["reviews_in_category"],
        "Top Products": category["products_ranked"]
    }
    for category in categories
])

st.dataframe(
    category_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# Reviews by category
# --------------------------------------------------

st.subheader("📈 Reviews by Category")

fig = px.bar(
    category_df.sort_values("Reviews", ascending=True),
    x="Reviews",
    y="Category",
    orientation="h",
    title="Number of Reviews per Category",
    text="Reviews"
)

fig.update_layout(yaxis_title=None, xaxis_title="Number of Reviews")
st.plotly_chart(fig, use_container_width=True)


st.divider()


# --------------------------------------------------
# Overall sentiment distribution
# --------------------------------------------------

st.subheader("💬 Overall Sentiment Distribution")

fig = px.pie(
    sentiment,
    names="sentiment",
    values="count",
    hole=0.45,
    title="Positive, Neutral and Negative Reviews"
)

fig.update_traces(textinfo="percent+label")
st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# Average rating by category
# --------------------------------------------------

st.subheader("⭐ Average Rating by Category")

fig = px.bar(
    ratings.sort_values("avg_rating", ascending=True),
    x="avg_rating",
    y="meta_category",
    orientation="h",
    range_x=[0, 5],
    text="avg_rating",
    title="Average Customer Rating per Category",
    labels={
        "avg_rating": "Average Rating (out of 5)",
        "category": "Category"
    }
)

st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# Sentiment distribution by category
# --------------------------------------------------

st.subheader("📊 Sentiment by Category")

fig = px.bar(
    by_category,
    x="meta_category",
    y="percentage",
    color="sentiment",
    barmode="stack",
    title="Sentiment Composition within Each Category",
    labels={
        "category": "Category",
        "percentage": "Percentage of Reviews",
        "sentiment": "Sentiment"
    },
    hover_data={"percentage": ":.1f"}
)

fig.update_layout(
    yaxis_title="Percentage of Reviews",
    xaxis_title="Category",
    yaxis_range=[0, 100]
)

st.plotly_chart(fig, use_container_width=True)

