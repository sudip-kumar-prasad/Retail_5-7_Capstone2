# Global Superstore Data Dictionary

This document provides a comprehensive description of the columns available in the processed dataset (`data/processed/superstore_cleaned.csv`), which is the primary source of truth for the ETL pipeline and all Tableau dashboards.

## Dataset Structure

| Column Name | Data Type | Description |
|---|---|---|
| **Category** | String | High-level category of the product (e.g., Furniture, Technology). |
| **City** | String | City where the customer is located. |
| **Country** | String | Country where the customer is located. |
| **Customer.ID** | String | Unique identifier assigned to each customer. |
| **Customer.Name** | String | Full name of the customer. |
| **Discount** | Float | Discount percentage applied to the sale (e.g., 0.2 represents 20%). |
| **Market** | String | Global market region where the sale occurred (e.g., APAC, EU, US). |
| **记录数** | Integer | A static record count placeholder (Chinese characters indicating 'record count', usually 1). |
| **Order.Date** | Datetime | The exact date when the customer placed the order. |
| **Order.ID** | String | Unique identifier for a specific order transaction. |
| **Order.Priority** | String | The priority level of the order (e.g., Critical, High, Medium, Low). |
| **Product.ID** | String | Unique identifier for the product sold. |
| **Product.Name** | String | The full descriptive name of the product. |
| **Profit** | Float | The total profit (in USD) generated from the transaction. Can be negative. |
| **Quantity** | Integer | Number of units of the product purchased in the transaction. |
| **Region** | String | Specific geographic region corresponding to the market. |
| **Row.ID** | Integer | Unique identifier for the specific row in the dataset. |
| **Sales** | Float | Total revenue (in USD) generated from the transaction before profit calculation. |
| **Segment** | String | Customer segment category (e.g., Consumer, Corporate, Home Office). |
| **Ship.Date** | Datetime | The exact date when the order was shipped to the customer. |
| **Ship.Mode** | String | The shipping method selected (e.g., Standard Class, First Class, Same Day). |
| **Shipping.Cost** | Float | The cost (in USD) to ship the order. |
| **State** | String | State or province where the customer is located. |
| **Sub.Category** | String | Specific sub-classification of the product category. |
| **Year** | Integer | Year the order was placed. |
| **Market2** | String | An alternative or secondary geographical market grouping. |
| **weeknum** | Integer | The week number of the year during which the order was placed. |

## Engineered Features (Added during ETL Pipeline)

These columns were calculated or derived within the Python cleaning pipeline (`capstone_analysis.ipynb` / `etl_pipeline.py`) to assist with deeper data exploration.

| Column Name | Data Type | Description |
|---|---|---|
| **Month** | Integer | Numeric representation of the month the order was placed (1-12). |
| **Month_Name** | String | Text representation of the month the order was placed (January-December). |
| **Day** | Integer | Numeric day of the month the order was placed (1-31). |
| **Shipping_Days** | Integer | Calculated duration in days between the `Order.Date` and the `Ship.Date`. |
| **Profit_Margin_%** | Float | The profit margin calculated as a percentage: `(Profit / Sales) * 100`. |
