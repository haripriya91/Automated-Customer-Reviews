from pathlib import Path
import json

import pandas as pd
import streamlit as st


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

SUMMARY_DIR = BASE_DIR / "reports" / "summaries_data"

SUMMARY_PATH = SUMMARY_DIR / "category_summary.json"


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Review Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Load category summary
# --------------------------------------------------

with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
    categories = json.load(f)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Amazon Review Analytics")

st.write(
    "Explore sentiment distribution, product performance "
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

total_products = sum(
    category["products_ranked"]
    for category in categories
)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Reviews",
        f"{total_reviews:,}"
    )

with col2:
    st.metric(
        "Categories",
        len(categories)
    )

with col3:
    st.metric(
        "Products Analysed",
        39
    )


st.divider()


# --------------------------------------------------
# Category overview
# --------------------------------------------------

st.subheader("📦 Product Categories")


category_df = pd.DataFrame(
    [
        {
            "Category": category["category"],
            "Reviews": category["reviews_in_category"],
            "Top Products": category["products_ranked"]
        }
        for category in categories
    ]
)


st.dataframe(
    category_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# Reviews by category
# --------------------------------------------------

st.subheader("📈 Reviews by Category")

chart_df = category_df.set_index("Category")

st.bar_chart(
    chart_df["Reviews"]
)

