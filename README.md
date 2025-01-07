# Stock Data Visualization and Analysis Project

## Overview
This project allows users to select tickers (stock symbols) and perform data analysis and visualization on the selected stocks. The project pulls real-time stock data from Yahoo Finance using the `yfinance` library. The stock data is then processed and visualized with `matplotlib` and `pandas` for easy interpretation of trends and statistics. 

### Libraries Used:
- **yfinance**: This library is used to fetch stock data from Yahoo Finance.
- **pandas**: Used for handling and analyzing data, including data manipulation and analysis.
- **matplotlib**: Provides the visualization capabilities for creating plots and graphs from the stock data.
- **streamlit**: The front-end for this project. It allows the project to be displayed as an interactive web app.

## Functionality
- **Stock Data Retrieval**: Users can input ticker symbols to fetch stock data for those companies.
- **Data Analysis**: The project provides basic data analysis, such as calculating the stock's moving averages and daily returns.
- **Visualization**: Interactive plots of stock prices, moving averages, and other relevant statistics are generated.
- **User Input**: Users can select multiple tickers and view analysis for those selected stocks.
  
## Setup and Installation
Follow these steps to get the project running:

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/stock-data-visualization.git
```

### 2. Install Dependencies
Make sure you have Python 3.x installed. Then, install the required libraries using pip:
```bash
pip install -r requirements.txt
```

If you do not have `requirements.txt` file, run:
```bash
pip install yfinance pandas matplotlib streamlit
```

### 3. Run the Application
Run the Streamlit app by using the following command:
```bash
streamlit run app.py
```

### 4. Using the Application
- Once the app is running, you'll be able to input stock tickers of your choice.
- You will see live stock data, various statistics, and visualizations for the selected stocks.

## Project Implementation
### 1. **Stock Data Retrieval with yfinance**
The project uses the `yfinance` library to fetch stock data:
```python
import yfinance as yf

ticker = 'AAPL'
stock_data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
```

### 2. **Data Manipulation with pandas**
We use pandas to process the stock data:
```python
import pandas as pd

# Calculate moving averages
stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()
```

### 3. **Visualization with matplotlib**
For visualizing the stock data, we use matplotlib to generate line charts

### 4. **Streamlit Front-End**
Streamlit is used to make the project interactive and user-friendly:

## Acknowledgments
- Thanks to the creators of `yfinance`, `pandas`, `matplotlib`, and `streamlit` for their open-source contributions that made this project possible.
