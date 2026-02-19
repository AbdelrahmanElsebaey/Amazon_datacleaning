# Amazon Sales Data Cleaning Project
------------------------------------

## Overview
This project demonstrates a complete data cleaning pipeline on a simulated Amazon sales dataset.  
The dataset contains realistic e-commerce sales data, including product information, prices, discounts, quantity sold, revenue, and ratings.

The main goal of this project is to **identify and fix data quality issues** to prepare the dataset for analysis or further processing.

---

## Dataset
- Source: https://www.kaggle.com/datasets/aliiihussain/amazon-sales-dataset
- Size: 50,000 rows, 3.97 MB
- Columns include:
  - 'order_date', 'product_name', 'price', 'discount_percent', 'discounted_price', 'quantity_sold', 'total_revenue', 'review_count', 'rating', etc.

---

## Data Cleaning Steps
1. **Load Data**  
   - Imported the dataset using Pandas with 'parse_dates' for 'order_date'.

2. **Check for Nulls**
   - Verified that there are no missing values.

3. **Check and Remove Duplicates**
   - Found no duplicates, but dropped any that exist for safety.

4. **Inconsistent Texts**
   - Standardized string columns: removed extra spaces, converted to lowercase, removed hidden characters (tabs/newlines).

5. **Check for Impossible Values**
   - 'discount_percent' should be between 0-100  
   - 'quantity_sold' and 'review_count' cannot be negative  
   - Prices and revenues were checked for consistency

6. **Logical Validations**
   - Ensured `discounted_price <= price`  
   - Verified `quantity_sold * discounted_price = total_revenue`  
   - Checked ratings are in range 1–5  
   - Checked 'order_date' is not in the future

7. **Save Cleaned Data**
   - Saved final cleaned dataset to 'cleaned_data/final_amazon_sales_dataset_clean.csv'

---

## Results
- Dataset is now **consistent, clean, and ready for analysis**.
- All checks for nulls, duplicates, impossible values, and logical errors passed.

---

## Tools & Libraries
- Python 3.x
- Pandas
- Datetime

---

## Notes
- Even though the dataset had no nulls or duplicates initially, all cleaning steps are **defensive**, ensuring the pipeline works for future updates to the dataset.
- This project demonstrates some **data engineering practices**, including validation, cleaning, and reproducibility.

## How to Run
1. Clone the repo
2. Place the dataset in the 'raw_data/' folder
3. Run 'cleaning.py'


