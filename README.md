# 🛍️ Automated Customer Review Analysis System

An end-to-end Natural Language Processing (NLP) project that automatically analyzes Amazon customer reviews to extract valuable insights. The system performs sentiment classification, product category clustering, generative AI review summarization, visualization and provides a deployable sentiment analysis web application.


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


## 🧠 Model

**Class-weight-tuned Logistic Regression with TF-IDF**: Classifies customer reviews as positive, neutral, or negative using text features and class weighting to address imbalanced data. 
Reason to choose this approach: We selected Class-weight-tuned Logistic Regression with TF-IDF because it achieved the highest test macro F1-score (56.18%), improving the detection of minority sentiment classes. Class weighting helps address the dataset’s imbalance, while TF-IDF converts review text into numerical features for sentiment classification.
Multinomial Naive Bayes was rejected because it failed to identify negative and neutral reviews, while Linear SVM achieved a strong macro F1 score and cross-validation performance but required additional calibration to provide class probabilities.

**K-means Clustering**: Groups similar products into broader categories based on their textual features.
Reason for choosing K-means: We chose K-means Clustering to group similar products into meaningful categories without predefined labels.

**Claude API**: Generates concise, category-level review summaries and AI-powered buying guides from extracted customer insights.
Reason for choosing Claude API: We tested pretrained Hugging Face models (Qwen and FLAN), but their summaries did not meet our quality expectations. We therefore chose the Claude API for more satisfactory, coherent, and informative review summaries. 


## Sentiment Analysis Results

The final class-weight-tuned Logistic Regression model achieved 90.13% accuracy and a macro F1-score of 0.56. Class weighting improved the detection of negative and neutral reviews while maintaining strong performance on positive reviews. However, identifying neutral sentiment remains challenging.

| Sentiment | Precision | Recall | F1-Score | Support |
| --------- | --------: | -----: | -------: | ------: |
| Negative  |       41% |    52% |      46% |     162 |
| Neutral   |       22% |    35% |      27% |     300 |
| Positive  |       97% |    94% |      95% |   6,461 |


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

## Deployment

Deployed with Streamlid 

🚀 **Live Demo:** [https://automated-customer-reviews.streamlit.app/](https://automated-customer-reviews.streamlit.app/)

### How to run the project locally

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


## Limitations

The test set contains substantially more positive reviews than neutral or negative reviews.
The lower F1-scores for neutral and negative reviews show that overall accuracy does not tell the whole story. The model can identify positive reviews reliably, but distinguishing neutral and negative reviews remains more challenging.
Similarly, the generated category buying guides depend on the quality and coverage of the underlying review data and should therefore be treated as **analysis aids rather than definitive purchasing recommendations**. 


## References


# Authors
**Haripriya Pushpamangalam Kesavan,**
**Anita Kiran** 
 
# License
 This project was developed for educational and research purposes.
