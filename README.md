# Crypto Insights Dashboard

A full-stack data project that fetches, stores, transforms, and visualizes real-time cryptocurrency market data. This dashboard offers insights into market trends using live API data and interactive visualizations.

## Features

- **Live Price & Market Pair Analysis**\
  Track the relationship between cryptocurrency prices and number of market pairs.

- **Market Cap Distribution**\
  Interactive pie chart showcasing market capitalization of top cryptocurrencies.

- **USD Quote Changes**\
  Monitor 7-day and 30-day percentage price changes of each coin.

- **Price Fluctuation Trends**\
  Visualize price movements across different timeframes.

- **Automatic Data Refresh**\
  The database is updated **every 10 minutes** with the latest data from the API using **GitHub Actions**.

## Tech Stack

| Layer         | Tool/Tech                                                            |
| ------------- | -------------------------------------------------------------------- |
| Data Source   | [CoinMarketCap API](https://coinmarketcap.com/api/documentation/v1/) |
| Data Handling | Python, Pandas                                                       |
| Database      | PostgreSQL (Supabase-hosted)                                         |
| Visualization | Metabase                                                             |
| Deployment    | GitHub Actions, Local/Cloud                                          |

## How It Works

1. **Data Ingestion**\
   Data is fetched from the CoinMarketCap API every 10 minutes using a scheduled script triggered by **GitHub Actions**.

2. **Data Transformation**\
   Using `pandas`, the raw JSON data is cleaned and structured into tabular form.

3. **Data Storage**\
   Transformed data is pushed into a PostgreSQL database hosted on [Supabase](https://supabase.com/).

4. **Visualization**\
   Metabase connects to the cloud database to generate dynamic and interactive dashboards that reflect the latest data.

## Sample Dashboard Preview

![Crypto Dashboard](https://raw.githubusercontent.com/harshkumar087/crypto-cloud/main/Metabase%20-%20Crypto_cloud_dash-5.png)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/harshkumar087/crypto-cloud.git
cd crypto-cloud
```

### 2. Set Up Environment

Create a `.env` file and store your API key and DB credentials:

```env
API_KEY=your_key_here
SUPA_URL=your_supabase_db_url
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Script

```bash
python fetch_crypto.py
```

### 5. Visualize in Metabase

- Connect Metabase to your Supabase database.
- Import or build dashboards using the available tables.

## Notes

- This project uses **GitHub Actions** to automatically run the script every 10 minutes, ensuring up-to-date data in the database.
- API usage is subject to rate limits — consider handling request failures gracefully.
- Supabase provides easy database hosting with built-in API endpoints.

## License

This project is licensed under the MIT License.

