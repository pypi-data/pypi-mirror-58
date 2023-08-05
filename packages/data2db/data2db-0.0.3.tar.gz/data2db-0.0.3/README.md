# data2db
Load csv, json or data from any database to any other database easily

## Why data2db?
data2db simplifies data transport between multiple source and target destinations. Currently it is a under-development project. In future more source-target combinations for data would be available.

## Supported Source of data
- MySQL
- MSSQL
- Google BigQuery
- CSV
- JSON

## Target destination Support
- MySQL
- MSSQL
- Google BigQuery
- CSV
- JSON

## Supported Transitions
Source\Destination | MySQL | MSSQL | Google BigQuery | CSV | JSON
-------------------|------|-------|--------------|------|--------
MySQL|:x:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:
MSSQL|:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:
Google BigQuery|:heavy_check_mark:|:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:
CSV|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:|:heavy_check_mark:
JSON|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:
URL|:x:|:x:|:x:|:heavy_check_mark:|:heavy_check_mark:

## Usage

    import data2db
    
    d = data2db()

### Changelog

v0.0.1
- Initial release
