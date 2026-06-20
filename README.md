# Daikibo Telemetry Data Integration

## Overview

This project was completed as part of the Data Analytics Virtual Experience Program.

The objective was to standardize Industrial Internet of Things (IIoT) telemetry data generated in two different JSON formats and convert them into a single unified schema for analytics and reporting.

## Problem Statement

Daikibo Industrials uses multiple IIoT devices that transmit telemetry data in different formats. To enable centralized analysis, both formats must be transformed into a common structure.

## Features

* Convert Telemetry Format 1 to Unified Format
* Convert Telemetry Format 2 to Unified Format
* ISO 8601 Timestamp Conversion to Unix Epoch Milliseconds
* Location Data Normalization
* Automated Unit Testing using Python unittest

## Technologies Used

* Python 3
* JSON
* Datetime Module
* Unittest Framework

## Project Structure

```text
data-1.json
data-2.json
data-result.json
main.py
```

## Running the Project

```bash
python main.py
```

## Sample Output

All unit tests pass successfully:

```text
Ran 3 tests

OK
```

## Skills Demonstrated

* Data Transformation
* ETL Processes
* Data Standardization
* Python Programming
* Unit Testing
* Industrial IoT Analytics
