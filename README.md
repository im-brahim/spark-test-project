# Spark Test Project

This is a simple PySpark-based project that processes NYC yellow taxi trip data, demonstrating basic data transformation and saving the results in Parquet format.

## Project Structure
SPARK-TEST/ 
├── .gitignore 
├── scripts/ 
│   └── test.py
├── data/ 
│   └── yellow_tripdata_2024-01.parquet
├── requirements.txt 
├── README.md

## Prerequisites
- Python 3.10+
- Virtual environment with necessary dependencies installed:
    - PySpark
    - findSpark
    - py4j

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spark-test-project.git
   cd spark-test-project

2. Create a Python virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate          # On Windows

3. Install the required Python packages:

    ```bash
    cd scripts
    pip install -r requirements.txt

4. Run the script:

    ```bash
    python scripts/test.py

## Output:

Processed Parquet file: processed_data/parquet_taxi.parquet
Processed CSV file: processed_data/parquet_taxi.csv
