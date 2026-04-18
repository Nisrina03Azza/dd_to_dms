import pandas as pd
import dd2dms
import openpyxl

df = pd.read_excel('sawit_wgs84.xlsx')

# Create new columns for DMS values
df['lat_degree'] = None
df['lat_minute'] = None
df['lat_second'] = None
df['lat_pole'] = None
df['long_degree'] = None
df['long_minute'] = None
df['long_second'] = None
df['long_pole'] = None


# Process each row in the DataFrame and convert the decimal degree to DMS
for index, row in df.iterrows():
    # Use .at to put the converted value into the specific row/column
    df.at[index,'lat_degree'] = dd2dms.get_degree(row['y'])
    df.at[index,'lat_minute'] = dd2dms.get_minutes(row['y'])
    df.at[index,'lat_second'] = dd2dms.get_second(row['y'])
    df.at[index,'lat_pole'] = dd2dms.get_latpole(row['y'])
    df.at[index,'long_degree'] = dd2dms.get_degree(row['x'])
    df.at[index,'long_minute'] = dd2dms.get_minutes(row['x'])
    df.at[index,'long_second'] = dd2dms.get_second(row['x'])
    df.at[index,'long_pole'] = dd2dms.get_longpole(row['x'])
    
# Save the updated DataFrame to a new Excel file
df.to_excel('sawit_wgs84_dms.xlsx', index=False)
print('Conversion complete! Check your new Excel file.')