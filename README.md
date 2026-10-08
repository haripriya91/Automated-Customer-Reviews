# 🛍️ Automated Customer Review Analysis System

An end-to-end Natural Language Processing (NLP) project that automatically analyzes Amazon customer reviews to extract valuable insights. The system performs sentiment classification, product category clustering, generative AI review summarization, visualization and provides a deployable sentiment analysis web application.

🚀 **Live Demo:** [https://automated-customer-reviews.streamlit.app/](https://automated-customer-reviews.streamlit.app/)

## 📌 Project Overview

Online shopping platforms contain thousands of customer reviews, making it difficult for consumers and businesses to manually analyze feedback. This project leverages modern NLP and Generative AI techniques to transform large amounts of customer review data into useful insights about customer sentiment, product categories, complaints, and overall product performance.

## 🏗️ Project Architecture

```text
                         Amazon Reviews Dataset
                                  │
                                  ▼
                         Data Preprocessing
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
             Task 1: Sentiment          Task 2: Clustering
                 Analysis              Product Categories
                    │                           │
                    └─────────────┬─────────────┘
                                  ▼
                       Review Insight Extraction
                                  │
                                  ▼
                    Task 3: Generative AI
                       Review Summarization
                                  │
                                  ▼
                       Buying Guide Articles
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
             Task 4: Streamlit           Visualizations
               Web Application
                    │
                    ▼
             Real-Time Sentiment
                Prediction
```


## 📊 Primary Dataset
**Amazon Product Reviews**
- Source: Kaggle
- File Used: `1429_1.csv`
- Size: ~34,000 reviews 

## ✨ Main Features

* **Sentiment Analysis** – Classify customer reviews into  Positive, Neutral, or Negative.
* **Product Category Clustering** – Group similar products into meaningful meta-categories using TF-IDF features and K-means.
* **AI-Powered Review Summarization** – Generate category-level summary articles.
* **Web Application Deployment** – Provide an accessible interface for sentiment prediction.
* **Bonus - Visualization** - Visualize important patterns and insights from the review dataset.


## Sentiment Analysis Results

The final Logistic Regression model achieved 86.0% accuracy and a macro F1-score of 0.53. Although the accuracy is relatively high, the macro F1-score highlights the difficulty of correctly identifying the minority negative and neutral classes.

| Sentiment | Precision | Recall | F1-Score | Support |
| --------- | --------: | -----: | -------: | ------: |
| Negative  |       33% |    59% |      42% |     162 |
| Neutral   |       17% |    43% |      24% |     300 |
| Positive  |       98% |    89% |      93% |   6,461 |


## Confusion Matrix
The model performs strongly on positive reviews, while performance on negative and neutral reviews is considerably weaker due to the strong class imbalance.
<a href="reports/figures/cm_final_model.png" target="_blank">View Confusion Matrix</a> 


## Product Category Clustering
The second task uses unsupervised learning to group similar products into product meta-categories.
Since the original dataset contains many individual products, clustering helps organize them into broader categories. 

## Approach
- Prepare product-level information.
- Convert product information into numerical representations.
- Apply clustering using K-means.
- Determine an appropriate number of clusters.
- Assign each product to a cluster.
- Analyze the products within each cluster.
- Give meaningful names to the resulting clusters. 

### Clustering Results

The clustering process grouped individual products into broader product meta-categories based on their textual/product information.
The resulting clusters were manually analyzed and assigned meaningful category names based on the products contained withineach cluster.


## 🤖 AI-Powered Review Summarization & Buying Guides
 
Product insights extracted from clustered reviews are sent to the Claude API to generate concise recommendation-style summaries. Each summary highlights key products, customer sentiment, common complaints, and notable review trends, helping users quickly understand product categories without reading thousands of reviews.

See the [reports/summaries/](reports/summaries/) directory for the full guides.


## 🛠️ Technologies Used
 
| Category | Tools & Technologies |
|-----------|---------------------|
| **Programming Language** | Python |
| **Data Processing** | Pandas, NumPy |
| **Natural Language Processing** | Scikit-learn, TF-IDF, Text Vectorization, N-gram Analysis, Sentiment Analysis |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-Learn |
| **Generative AI** | Claude API is used to generate category-level summary |
| **Deployment** | Streamlit |


## Run the Sentiment App Locally

Install the required dependencies:

```bash
pip install -r app/requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app/app.py
```

## Project Structure

```text
Automated-Customer-Reviews/
│
├── app/
│   ├── app.py
│   └── pages/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── reports/
│   ├── figures/
│   └── summaries/
│
├── requirements.txt
└── README.md
```

* `app/` — Streamlit sentiment analysis app and dashboard pages
* `data/` — raw and processed review datasets
* `models/` — saved sentiment and clustering models
* `notebooks/` — exploration, preprocessing, modeling, clustering, and summary workflows
* `reports/` — confusion matrix and generated category buying guides

## Limitations

The test set contains substantially more positive reviews than neutral or negative reviews.
The lower F1-scores for neutral and negative reviews show that overall accuracy does not tell the whole story. The model can identify positive reviews reliably, but distinguishing neutral and negative reviews remains more challenging.
Similarly, the generated category buying guides depend on the quality and coverage of the underlying review data and should therefore be treated as **analysis aids rather than definitive purchasing recommendations**. 

# Authors
**Haripriya Pushpamangalam Kesavan,**
**Anita Kiran** 

---
 
# License
 
This project was developed for educational and research purposes.
