# AI-Powered Customer Lifetime Value (CLV)

An end-to-end data analytics and machine learning project that predicts Customer Lifetime Value (CLV) and segments customers based on their purchasing behavior.
The project combines SQL feature engineering, Python machine learning, and Power BI dashboards to create a complete analytics pipeline.

### Project Objective

Businesses need to understand which customers are most valuable and which customers are likely to generate future revenue.

This project aims to:

Segment customers based on purchasing behavior

Predict future customer value using machine learning

Provide business insights through an interactive Power BI dashboard

### Tech Stack

Languages \& Tools

* Python
* SQL
* PostgreSQL
* Power BI

Python Libraries

* pandas
* scikit-learn
* XGBoost
* numpy
* joblib

## Project Architecture

Raw Transaction Data
↓
SQL Feature Engineering
(rfm\_features.sql)
↓
Customer Behavioral Features
↓
Python Analytics Pipeline
├── Customer Segmentation (K-Means)
├── CLV Model Training (XGBoost)
└── CLV Prediction
↓
Processed Dataset
↓
Power BI Dashboard

## Feature Engineering

|Feature|Description|
|-|-|
|Frequency|Number of purchases made by a customer|
|Recency|Days since the customer's last purchase|
|T|Customer age (time between first purchase and observation period)|
|Monetary|Average purchase value|
|Avg Order Value|Average transaction value|
|Lifetime Days|Duration of customer activity|



### Customer Segmentation

Customers are grouped into behavioral segments using K-Means clustering.

Segments help businesses identify different customer types such as:

* VIP customer
* Loyal customers
* Mid-value customers
* At-risk customers

### Power BI Dashboard

The final dataset is visualized using Power BI to provide business insights.

Key dashboard components include:

KPI Metrics

* Total Customers
* Total Revenue
* Average Order Value
* Average Purchase Frequency

Customer Insights

* Revenue distribution by segment
* Customer distribution across clusters
* Behavioral comparison between segments

AI Insights

* Predicted CLV by segment
* Top customers by predicted CLV
* Future revenue potential

