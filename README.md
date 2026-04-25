# SEC EDGAR Financial Data Pipeline and Stock Analysis 

## Overview

ETL pipeline that bulk downloads 10 years (1.82GB) of SEC EDGAR zip file data from 2014Q1 to 2023Q3. Data is uploaded onto the host, then unzipped into a new folder and filtered before going into MySQL. The data is taken from MySQL and put back into Python to perform business calculations, finding spikes in R&D spending across 4570 companies. The spikes are found by taking the average amount spent on R&D over three quarters. If they spent more, the date that they spent more and the percentage increase over the average are stored and delivered. 

##Thesis for Stock Analysis

1. Revenue is stable or growing. 

2. Net income dropped because of R&D

3. R&D is unusual—it spiked significantly. 

4. Stock movement after the filing 

5. PE is reasonable.

As of right now I have completed step three. 

## Data Source

SEC EDGAR Financial Statement Data Sets (2014 Q1 - 2023 Q4)

https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets-archive

## Tools Used

- Python (pandas, zipfile, requests, sqlalchemy)

- MySQL

## Pipeline Steps

1. Bulk download 40 quarterly ZIP files from SEC EDGAR

2. Extract and rename num.txt and sub.txt from each zip.

3. Filter for R&D, Net Income, and Revenue 

4. Clean and type-convert data

5. Load into MySQL—financial_data and metadata tables

## How to Run

1. Create a MySQL database called aggregated_stock_data.

2. Create tables using schema in queries_edgar.sql

3. Fill in your MySQL credentials in the script.

4. Run edgbatch_DL&EXT_SQL.py
