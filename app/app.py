import gradio as gr
import joblib

pipe = joblib.load("../models/sentiment_pipeline.pkl")


def predict_sentiment(review):
    prediction = pipe.predict([review])[0]
    probabilities = pipe.predict_proba([review])[0]
    result = {
        label: float(probability)
        for label, probability in zip(
            pipe.classes_,
            probabilities
        )
    }
    return result


demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(
        label="Enter a customer review",
        placeholder="Write your review here..."
    ),
    outputs=gr.Label(label="Sentiment"),
    title="Amazon Review Sentiment Analyzer"
)

demo.launch()