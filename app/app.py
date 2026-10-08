from pathlib import Path
import joblib
import streamlit as st


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Amazon Review Analyzer",
    page_icon="🛒",
    layout="centered"
)


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_pipeline.pkl"

pipe = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.header("🛒 Amazon Review Analyzer")

st.write(
    "AI-powered sentiment analysis of Amazon customer reviews."
)


# --------------------------------------------------
# Review input
# --------------------------------------------------

review = st.text_area(
    "Enter your review",
    placeholder="Write your Amazon review here...",
    height=120
)


# --------------------------------------------------
# Analyze
# --------------------------------------------------

if st.button(
    "🔍 Analyze Sentiment",
    use_container_width=True
):

    if not review.strip():

        st.warning("Please enter a review.")

    else:

        prediction = pipe.predict([review])[0]
        probabilities = pipe.predict_proba([review])[0]

        predicted_index = list(pipe.classes_).index(prediction)

        confidence = probabilities[predicted_index]


        # --------------------------------------------------
        # Result
        # --------------------------------------------------

        st.divider()

        st.subheader("🔍 Analysis Result")

        if prediction == "positive":

            st.success(
                f"😊 Positive — {confidence:.1%} probability"
            )

        elif prediction == "negative":

            st.error(
                f"😞 Negative — {confidence:.1%} probability"
            )

        else:

            st.warning(
                f"😐 Neutral — {confidence:.1%} probability"
            )


        # --------------------------------------------------
        # Prediction probabilities
        # --------------------------------------------------

        st.subheader("📊 Prediction Probabilities")

        cols = st.columns(len(pipe.classes_))

        for col, label, probability in zip(
            cols,
            pipe.classes_,
            probabilities
        ):

            with col:

                if label == "positive":
                    emoji = "😊"

                elif label == "negative":
                    emoji = "😞"

                else:
                    emoji = "😐"


                st.metric(
                    label=f"{emoji} {label.capitalize()}",
                    value=f"{probability:.1%}"
                )

                st.progress(float(probability))


# --------------------------------------------------
# Dashboard link
# --------------------------------------------------

st.divider()

st.info(
    "📊 Want to explore the complete Amazon review dataset?"
)

st.page_link(
    "pages/2_Review_Dashboard.py",
    label="Open Review Analytics Dashboard →",
    icon="📊"
)