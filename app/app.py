from pathlib import Path
import joblib
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_pipeline.pkl"

pipe = joblib.load(MODEL_PATH)

# Page configuration
st.set_page_config(
    page_title="Amazon Review Analyzer",
)


# Title
st.title("Amazon Review Analyzer")

st.write(
    "Enter a customer review to predict whether "
    "the sentiment is negative, neutral, or positive."
)


# Review input
review = st.text_area(
    "Enter a customer review",
    placeholder="Write your review here..."
)


# Analyze button
if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        # Prediction
        prediction = pipe.predict([review])[0]

        # Probabilities
        probabilities = pipe.predict_proba([review])[0]

        # Show prediction
        st.subheader("Prediction")

        if prediction == "positive":
            st.success("Positive")

        elif prediction == "negative":
            st.error("Negative")

        else:
            st.warning("Neutral")


        # Show confidence scores
        st.subheader("Confidence Scores")

        for label, probability in zip(
            pipe.classes_,
            probabilities
        ):
            st.write(
                f"**{label.capitalize()}**: "
                f"{probability:.2%}"
            )