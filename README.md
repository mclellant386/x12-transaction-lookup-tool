# Project 01 - X12 Transaction Lookup Tool

## Business Problem

Healthcare organizations process dozens of X12 transaction types every day. Analysts frequently need to identify transaction codes or locate the correct transaction based on a business process, creating unnecessary friction during troubleshooting and operational support.

## Solution

This Python application provides an interactive command-line lookup tool that enables users to search common healthcare X12 transactions by transaction code or keyword.

## Features

- Search by X12 transaction code
- Search by business keyword
- Displays transaction descriptions
- Handles invalid transaction codes gracefully

## Technologies

- Python
- Dictionaries
- Conditional Logic
- Loops
- User Input
- String Matching

## Example

Search by code:

```
837
```

Output:

```
837: Healthcare Claim
```

Search by keyword:

```
remittance
```

Output:

```
835: Electronic Remittance Advice
```
Last Updated: July 2, 2026