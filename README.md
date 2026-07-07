# Project 02 - Healthcare EDI Report Automation

## Business Problem

Healthcare EDI operations teams process large volumes of transaction data exchanged between healthcare organizations, payers, providers, and trading partners.

Operational teams need an efficient way to identify rejected transactions, determine which files contain errors, analyze common rejection reasons, and produce reports that support troubleshooting and daily processing workflows.

Manually reviewing transaction-level data and creating operational reports can be time-consuming and difficult to scale.

## Solution

This project simulates an automated healthcare EDI operations reporting pipeline using Python.

The workflow begins with generated transaction-level data that represents processing results returned by a payer, clearinghouse, or trading partner after healthcare EDI batch files have been processed.

Python then reads the inbound processing report, analyzes accepted and rejected transaction outcomes, determines which files processed successfully and which contain rejections, aggregates rejection reasons, and generates a formatted Excel workbook for operational review.

The final workbook provides both high-level processing metrics for stakeholders and transaction-level details that analysts can use to investigate rejected transactions and affected batch files.

## Pipeline Workflow

Generate Simulated Transaction Data
(Represents an inbound processing report or transaction-level results
returned by a payer, clearinghouse, or trading partner)
        ↓
CSV Transaction Report
(Represents the operational source data received for analysis)
        ↓
Analyze Transaction Results
(Represents automated processing of transaction outcomes)
        ↓
Identify File-Level Processing Status
(Determine which batch files processed cleanly and which require investigation)
        ↓
Aggregate Rejection Reasons
(Identify common processing failures and impacted files)
        ↓
Generate Excel Operational Report
(Transform analysis results into a stakeholder-ready reporting deliverable)
        ↓
Dashboard + Summary + Raw Transactions + Rejection Details
(Provide executive metrics and transaction-level detail for investigation)

## Features

- Generates randomized healthcare EDI transaction processing data
- Simulates batch processing of X12 837 healthcare claim transactions
- Tracks accepted and rejected transactions
- Classifies files as fully accepted or containing rejections
- Counts rejection occurrences by file
- Aggregates rejection reasons using status codes and messages
- Provides rejection details for individual EDI files
- Calculates transaction acceptance rate
- Generates a multi-sheet Excel operational report
- Highlights rejected transactions for easier investigation
- Adds filtering and frozen headers to transaction-level data
- Automatically adjusts Excel column widths
- Creates an operational dashboard with processing metrics
- Generates charts for accepted vs. rejected transactions and top rejection reasons
- Runs the complete reporting workflow through a single pipeline script
- Stops pipeline execution if a processing stage fails

## Project Structure

```text
Project_02_Healthcare_EDI_Report_Automation/
│
├── 01_generate_report.py
├── 02_analyze_report.py
├── 03_create_excel_report.py
├── 04_run_pipeline.py
├── edi_transaction_report.csv
├── edi_processing_report.xlsx
└── README.md
```

## Pipeline Components

### 01_generate_report.py

### 01_generate_report.py

Generates simulated transaction-level healthcare EDI processing results.

Within the project workflow, this script represents an external payer, clearinghouse, or trading partner system returning processing results after receiving and evaluating X12 837 healthcare claim batch files.

The generated CSV serves as the inbound operational processing report consumed by the downstream analysis and reporting scripts.

### 02_analyze_report.py

Reads the generated transaction report and performs operational analysis.

The script:

- Counts total, accepted, and rejected transactions
- Determines whether each EDI file was fully accepted
- Identifies files containing one or more rejected transactions
- Counts rejections by file
- Aggregates rejection reasons
- Provides rejection details for each affected file

### 03_create_excel_report.py

Transforms the transaction data and analysis results into a formatted Excel workbook.

The workbook contains:

- Dashboard
- Processing Summary
- Raw Transactions
- Rejection Details

The report includes formatting, filters, frozen panes, rejected transaction highlighting, operational metrics, and dashboard charts.

### 04_run_pipeline.py

Runs the complete reporting workflow.

```text
Generate Data
    ↓
Analyze Results
    ↓
Create Excel Report
```

Each processing stage runs sequentially. If a stage fails, the pipeline stops and displays the corresponding error.

## Example Pipeline Output

```text
Starting EDI reporting pipeline...
---------------------------------

Running 01_generate_report.py...
Report generated: edi_transaction_report.csv

Running 02_analyze_report.py...

EDI Daily Processing Summary
============================

Total Transactions: 100
Accepted: 94
Rejected: 6

Fully Accepted Files
--------------------

837_CENTENE_BATCH003.edi
837_CENTENE_BATCH005.edi

Files with Rejections
---------------------

837_CENTENE_BATCH001.edi - 2 rejections
837_CENTENE_BATCH002.edi - 1 rejection
837_CENTENE_BATCH004.edi - 3 rejections

Rejection Summary
-----------------

R101 - Invalid member ID: 1
R202 - Missing required segment: 5

Running 03_create_excel_report.py...

Excel report created: edi_processing_report.xlsx

Pipeline complete.
```

## Technologies and Python Concepts

- Python
- CSV processing
- Dictionaries
- Nested dictionaries
- Lists and tuples
- Loops and conditional logic
- File handling
- pathlib
- subprocess
- Error handling using process return codes
- Data aggregation
- ETL concepts
- Excel report automation
- openpyxl
- Excel formatting
- Excel charts and dashboard creation

## Skills Demonstrated

- Healthcare EDI operations knowledge
- X12 transaction processing concepts
- Batch file monitoring
- Transaction-level data analysis
- File-level validation
- Rejection analysis
- Operational reporting
- Data aggregation
- ETL workflow development
- Excel report automation
- Python scripting
- Multi-step workflow automation
- Basic pipeline orchestration

## Future Enhancements

- Add additional healthcare X12 transaction types such as 835, 270/271, and 276/277
- Add trading partner and payer-level processing summaries
- Calculate rejection rates by payer and transaction type
- Add processing-time monitoring and performance metrics
- Add configurable rejection thresholds
- Generate alerts when rejection thresholds are exceeded
- Archive historical processing reports for trend analysis
- Add automated tests for transaction processing and reporting logic
- Support processing multiple inbound CSV files
- Replace simulated transaction data with external API or database input

## Running the Project

Run the complete pipeline from the project directory:

```bash
python3 04_run_pipeline.py
```

The pipeline generates:

```text
edi_transaction_report.csv
edi_processing_report.xlsx
```

Last Updated: July 7, 2026