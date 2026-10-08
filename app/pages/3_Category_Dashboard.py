from pathlib import Path
import json
import pandas as pd
import streamlit as st


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

SUMMARY_DIR = BASE_DIR / "reports" / "summaries_data"
GUIDE_DIR = BASE_DIR / "reports" / "summaries"


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Category Analysis",
    page_icon="🔎",
    layout="wide"
)


# --------------------------------------------------
# Load category summary/index
# --------------------------------------------------

SUMMARY_PATH = SUMMARY_DIR / "category_summary.json"

if not SUMMARY_PATH.exists():
    st.error(
        "category_summary.json was not found. "
        "Please run the category analysis notebook first."
    )
    st.stop()

with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
    categories = json.load(f)


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.title("🔎 Category Analysis")

st.write(
    "Explore sentiment, product performance, customer feedback "
    "and AI-generated insights for each product category."
)


# --------------------------------------------------
# Category selector
# --------------------------------------------------

selected_category = st.selectbox(
    "Select a product category",
    [category["category"] for category in categories]
)


# Find selected category in summary index
selected_summary = next(
    category
    for category in categories
    if category["category"] == selected_category
)


# --------------------------------------------------
# Load detailed category JSON
# --------------------------------------------------

detail_path = SUMMARY_DIR / selected_summary["detail_file"]

if not detail_path.exists():
    st.error(
        f"Category data file not found: {detail_path.name}"
    )
    st.stop()

with open(detail_path, "r", encoding="utf-8") as f:
    category_data = json.load(f)


# --------------------------------------------------
# Category overview
# --------------------------------------------------

st.divider()

st.subheader(f"📦 {selected_category}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Reviews",
        f'{category_data["reviews_in_category"]:,}'
    )

with col2:
    st.metric(
        "Products Ranked",
        category_data["products_ranked"]
    )

with col3:
    st.metric(
        "Reviews without Product Name",
        f'{category_data["pct_reviews_without_product_name"]:.1f}%'
    )


# --------------------------------------------------
# Data warning
# --------------------------------------------------

if category_data.get("data_warning"):
    st.warning(category_data["data_warning"])


# --------------------------------------------------
# Sentiment Distribution
# --------------------------------------------------

st.divider()

st.subheader("📊 Sentiment Distribution")

products = category_data.get("products", [])

if products:

    sentiment_totals = {
        "Positive": 0,
        "Neutral": 0,
        "Negative": 0
    }

    for product in products:

        review_count = product["review_count"]

        sentiment_totals["Positive"] += (
            review_count * product["positive_pct"] / 100
        )

        sentiment_totals["Neutral"] += (
            review_count * product["neutral_pct"] / 100
        )

        sentiment_totals["Negative"] += (
            review_count * product["negative_pct"] / 100
        )

    sentiment_df = pd.DataFrame(
        {
            "Sentiment": sentiment_totals.keys(),
            "Reviews": sentiment_totals.values()
        }
    )

    sentiment_df = sentiment_df.set_index("Sentiment")

    st.bar_chart(sentiment_df)

else:
    st.info("No product sentiment data available.")


# --------------------------------------------------
# Top Products
# --------------------------------------------------

st.divider()

st.subheader("🏆 Top Products")

if products:

    product_df = pd.DataFrame(
        [
            {
                "Product": product["name"],
                "Reviews": product["review_count"],
                "Rating": product["average_rating"],
                "Positive": f'{product["positive_pct"]:.1f}%',
                "Neutral": f'{product["neutral_pct"]:.1f}%',
                "Negative": f'{product["negative_pct"]:.1f}%'
            }
            for product in products
        ]
    )

    st.dataframe(
        product_df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No product data available.")


# --------------------------------------------------
# Most reviewed product
# --------------------------------------------------

most_reviewed = category_data.get("most_reviewed_product")

if most_reviewed:

    st.subheader("⭐ Most Reviewed Product")

    st.write(
        f"**{most_reviewed['name']}**"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Review Count",
            f'{most_reviewed["review_count"]:,}'
        )

    with col2:
        st.metric(
            "Average Rating",
            f'{most_reviewed["average_rating"]:.2f} ⭐'
        )


# --------------------------------------------------
# Product sentiment comparison
# --------------------------------------------------

if products:

    st.divider()

    st.subheader("📈 Product Sentiment Comparison")

    comparison_df = pd.DataFrame(
        [
            {
                "Product": product["name"],
                "Positive": product["positive_pct"],
                "Neutral": product["neutral_pct"],
                "Negative": product["negative_pct"]
            }
            for product in products
        ]
    )

    comparison_df = comparison_df.set_index("Product")

    st.bar_chart(comparison_df)


# --------------------------------------------------
# AI-generated category guide
# --------------------------------------------------

st.divider()

st.subheader("AI-Generated Category Insights")

# Convert category name to the same filename format
import re

slug = re.sub(
    r"[^a-z0-9]+",
    "_",
    selected_category.lower()
).strip("_")

guide_path = GUIDE_DIR / f"{slug}.md"


if guide_path.exists():

    guide_text = guide_path.read_text(
        encoding="utf-8"
    )

    st.markdown(guide_text)

else:

    st.info(
        "AI-generated category summary is not available "
        "for this category yet."
    )


# --------------------------------------------------
# Customer Feedback
# --------------------------------------------------

st.divider()

st.subheader("💬 Customer Feedback")

if products:

    for product in products:

        with st.expander(
            f"📦 {product['name']}"
        ):

            st.write(
                f"**Average rating:** "
                f'{product["average_rating"]:.2f} ⭐'
            )

            st.write(
                f"**Reviews:** "
                f'{product["review_count"]:,}'
            )

            # Positive examples
            positive_reviews = product.get(
                "sample_of_positive_reviews",
                []
            )

            if positive_reviews:

                st.markdown(
                    "**😊 Positive Review Examples**"
                )

                for review in positive_reviews[:3]:
                    st.write(f"• {review}")

            # Low-rated examples
            low_rated_reviews = product.get(
                "sample_of_low_rated_reviews",
                []
            )

            if low_rated_reviews:

                st.markdown(
                    "**⚠️ Low-Rated Review Examples**"
                )

                for review in low_rated_reviews[:3]:
                    st.write(f"• {review}")



