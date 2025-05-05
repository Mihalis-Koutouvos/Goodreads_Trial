# Goodreads Trial - Review Parser
**Made by: Mihalis Koutouvos**




## Core Features

- **CSV Upload**: Users upload CSVs with financial data
- **Data Cleaning**: Automatically removes rows with missing or erroneous values


## Project Goals

- Build a robust pipeline for financial CSV processing  
- Automatically clean and validate user-uploaded data  
-


## Requirements

- Python 3.12 
- Required Python/conda packages (see requirements.txt)



## Project Setup:

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your AWS credentials:
   ```bash
   cp .env.example .env
   ```
4. Edit the `.env` file with your AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=your_access_key_here
   AWS_SECRET_ACCESS_KEY=your_secret_key_here
   AWS_REGION=your_aws_region
   S3_BUCKET_NAME=your_bucket_name
   ```
5. Update the configuration variables
