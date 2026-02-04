# Trader Sentiment Analysis & Predictive Modeling

This project analyzes the relationship between market sentiment (Fear–Greed Index) and trader behavior on Hyperliquid.
It includes:
- Data cleaning & preprocessing
- Sentiment–trade merging
- Performance metrics (PnL, win rate, drawdown proxy)
- Behavior analysis (long–short bias, leverage proxy, trade frequency)
- Strategy recommendations
- Predictive modeling using Random Forest Classifier
- Insights for building sentiment-aware trading systems


## Project Structure

<img width="410" height="315" alt="Screenshot 2026-02-04 at 11 04 34 PM" src="https://github.com/user-attachments/assets/553f4e66-6bed-44cd-88fc-89ed2a02d47c" />

## Setup Instructions
1. Clone the repository

`git clone https://github.com/<your-username>/trader-sentiment-analysis.git
cd trader-sentiment-analysis`

3. Create a virtual environment
- Mac/Linux:

`python3 -m venv venv
source venv/bin/activate`

- Windows:

`python -m venv venv
venv\Scripts\activate`

3. Install dependencies

`pip install -r requirements.txt`

5. Launch Jupyter Notebook

`jupyter notebook`

7. To launch dashboard

`streamlit run app.py`


### How to Run the Notebook Properly

1. Load both datasets
The notebook expects:
- data/fear_greed_index.csv
- data/historical_data.csv
Make sure the files are inside `/data/`

2. Run preprocessing cells
- Parse Timestamp IST correctly
- Convert dates
- Merge sentiment with trade data
- Clean missing / invalid rows

3. Generate analytics
- The notebook contains:
- PnL distribution per sentiment
- Win-rate per sentiment
- Drawdown proxy
- Trade frequency over time
- Long/short ratio
- Leverage proxy (Exposure)
- Account-level behavior features

4. Run predictive modeling
It includes:
- Feature engineering
- Grouped train-test split (to prevent same-account leakage)
- Random Forest classifier
- Confusion matrix & performance summary
- Feature importance plot

5. Streamlit Dashboard
It explores:
- PnL distribution
- Leverage / exposure
- Long–short behavior
- Trade frequency
- Sentiment-based filtering
- Account-level filtering

## Streamlit Dashboard Screenshots
<img width="1675" height="841" alt="Screenshot 2026-02-04 at 11 05 26 PM" src="https://github.com/user-attachments/assets/70fc9628-2f0f-410b-bd4c-a0377ba3f570" />
<img width="1677" height="863" alt="Screenshot 2026-02-04 at 11 06 00 PM" src="https://github.com/user-attachments/assets/4f7530a4-48dd-472d-83ae-44086d230fa8" />

