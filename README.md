# Geospatial Data Converter: DD to DMS (Batch Processor)

This project is a Python-based utility that automates the conversion of geographic coordinates from Decimal Degrees (DD) to Degrees, Minutes, and Seconds (DMS). Unlike standard converters, this tool performs batch processing on Excel datasets and outputs the DMS components into individual columns for granular spatial analysis.

## About the Project
This project marks a milestone in my journey of relearning Python fundamentals—applying core programming concepts to solve practical problems in Geodetic Engineering and GIS.
In professional GIS workflows, coordinates are often provided in decimal format, but many legacy systems, legal documents, and field GPS units require DMS. Building this tool allowed me to practice:
- File I/O: Reading and writing .xlsx files with openpyxl.
- Data Frames: Manipulating tabular data using pandas.
- Math Logic: Implementing remainders and coordinate pole (N/S/E/W) logic.

## Feature
- Batch Processing: Uses pandas to handle large Excel datasets (e.g., oil palm plantation coordinates).
- Component Splitting: Breaks coordinates into four distinct parts (Degree, Minute, Second, and Pole) for both Latitude and Longitude.
- Data Integrity: Implements absolute value logic and rounding to ensure professional geodetic precision.
- Modularity: Features a separate calculation engine (dd2dms.py) to keep the data processing logic clean and reusable.

## How to Use
1. Run the script: python latlong.py 
2. Change the file's name to your Excel dataset.
3. Change the column's name.
4. Get your new updated dataset.

## Example
**From** 
<img width="668" height="448" alt="image" src="https://github.com/user-attachments/assets/038e9017-9c28-46f9-b64e-4fba608602dc" />


**To**
<img width="1133" height="447" alt="image" src="https://github.com/user-attachments/assets/3c6fc3ad-fec3-4291-bd38-62751470e008" />



