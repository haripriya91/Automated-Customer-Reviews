
```markdown
# Automated Customer Reviews

An NLP project that analyzes Amazon customer reviews through sentiment
classification, product clustering, and AI-generated category buying guides.

**Live demo:** [Try the sentiment analyzer](https://automated-customer-reviews.streamlit.app/)

## Project overview

Thousands of customer reviews can be difficult to analyze manually. This
project explores ways to turn review text into useful signals: predict its
sentiment, group similar products, and summarize customer feedback into
category-level recommendations.

## Features

- **Sentiment analysis:** Classifies a review as positive, neutral, or negative.
  The Streamlit app also displays a probability for each class.
- **Product clustering:** Uses TF-IDF features and K-Means to group products
  into interpretable meta-categories.
- **Buying guides:** Generates category summaries covering popular products,
  common complaints, and recommendations.

## Method

1. Explore and preprocess the review dataset.
2. Train a sentiment classifier using TF-IDF features and Logistic Regression.
3. Compare K-Means clustering configurations for 4–6 groups and label the
   resulting product categories.
4. Prepare category-level review evidence and generate buying guides with
   Claude.

## Sentiment model results

The final Logistic Regression model achieved **86.00% accuracy** on the held-out
test set. We compared models using macro F1 as well as accuracy because the
dataset is imbalanced: Naive Bayes reached 93.33% accuracy but only 32.19%
macro F1, with an F1-score of zero for both negative and neutral reviews.
Logistic Regression performed much more evenly across sentiment classes.
Linear SVM scored one point higher than Logistic Regression on macro F1 (54.83% vs. 53.97%),but the cross-validation ranges nearly overlap, so Logistic Regression was the model used in the demo.

| Sentiment | Precision | Recall | F1-score | Test samples |
|---|---:|---:|---:|---:|
| Negative | 33% | 59% | 42% | 162 |
| Neutral  | 17% | 43% | 24% | 300 |
| Positive | 98% | 89% | 93% | 6,461 |

### Confusion matrix

Rows are the actual class; columns are the predicted class.

| Actual \ Predicted | Negative | Neutral | Positive |
|---|---:|---:|---:|
| Negative | 96 | 42 | 24 |
| Neutral  | 57 | 129 | 114 |
| Positive | 142 | 590 | 5,729 |

![Sentiment model confusion matrix](reports/figures/cm_final_model.png)

## Product category summaries

The project contains generated buying guides for these categories:

- Amazon Device Accessories & Chargers
- Echo & Kindle Fire Devices
- Echo & Smart Home Devices
- Fire Kids Edition Tablets & Accessories
- Kindle & Fire Devices – Special Offers
- Kindle Fire Tablets – 16GB

See the [reports/summaries](reports/summaries/) directory for the full guides.

## Run the sentiment app locally

```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```

## Project structure

- `app/` — Streamlit sentiment analysis app and dashboard pages
- `data/` — raw and processed review datasets
- `models/` — saved sentiment and clustering models
- `notebooks/` — exploration, preprocessing, modeling, clustering, and summary workflows
- `reports/` — confusion matrix and generated category guides

## Limitations

The test set contains many more positive reviews than neutral or negative ones.
The model’s lower F1-scores for neutral and negative reviews show that the
overall accuracy does not tell the whole story. Treat predictions and
category recommendations as analysis aids, not guarantees.
```
