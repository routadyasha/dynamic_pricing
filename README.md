# Dynamic Pricing Optimization Project

This project demonstrates a dynamic pricing optimization system using web scraping, data cleaning, machine learning, and a Streamlit app for price prediction.

## Project Structure

dynamic-pricing/
├── data/
│ ├── raw/ # Raw scraped data (not tracked by Git)
│ └── processed/ # Cleaned data (not tracked by Git)
├── models/ # Saved ML models (not tracked by Git)
├── scripts/
│ ├── scrape_amazon.py
│ ├── analyze_data.py
│ ├── train_model.py
│ └── test_model.py
├── streamlit_app.py # Streamlit user interface
├── requirements.txt # Python dependencies
└── README.md # This file

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/routadyasha/dynamic_pricing.git
   cd dynamic_pricing

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Scrape data:
python scripts/scrape_amazon.py

5. Clean and analyze data:
python scripts/analyze_data.py

6. Train the model:
python scripts/train_model.py

7. Test the model:
python scripts/test_model.py

8. Run the Streamlit app:
streamlit run streamlit_app.py

Contact
Created by Adyasha Rout