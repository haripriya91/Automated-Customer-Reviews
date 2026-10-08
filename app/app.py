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
# Example reviews
# --------------------------------------------------

st.subheader("💡 Try an example review")

col1, col2, col3 = st.columns(3)

if "review_text" not in st.session_state:
    st.session_state.review_text = ""


with col1:

    if st.button(
        "😊 Positive",
        use_container_width=True
    ):

        st.session_state.review_text = (
            "The sound quality is excellent for the price. "
            "Setup was easy and the battery lasts much longer "
            "than I expected. Very happy with this purchase."
        )


with col2:

    if st.button(
        "😞 Negative",
        use_container_width=True
    ):

        st.session_state.review_text = (
            "I was disappointed with the quality. "
            "The device stopped working after only a few days "
            "and customer support did not provide a useful solution."
        )


with col3:

    if st.button(
        "😐 Neutral",
        use_container_width=True
    ):

        st.session_state.review_text = (
            "The product arrived on time and works as described, but the performance is just okay given the price."
            "I honestly expected better. While it handles basic tasks fine, the overall experience feels sluggish and the build quality feels a bit cheap and plasticky."
            "It's a decent middle-of-the-road option if you are on a strict budget, but if you are looking for longevity or seamless performance, it might be worth spending a bit more on a higher-end alternative."
        )


# --------------------------------------------------
# Review input
# --------------------------------------------------

review = st.text_area(
    "Enter your review",
    placeholder="Write your Amazon review here...",
    height=120,
    key="review_text"
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

        st.subheader("📊 Confidence scores")

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