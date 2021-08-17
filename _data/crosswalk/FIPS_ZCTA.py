# Import libraries
import os
import pandas as pd
import urllib.request

# Set working directory
path_local = os.getcwd()
os.chdir(path_local)
os.chdir('allocativ')
os.chdir('healthy-neighborhoods')

## Data for Democracy crosswalk
#sr4a = 'https://www.kaggle.com/danofer/zipcodes-county-fips-crosswalk?select=ZIP-COUNTY-FIPS_2017-06.csv'
#os.popen('kaggle datasets download -d danofer/zipcodes-county-fips-crosswalk')
#with ZipFile(directory + sr4 + '.zip', 'r') as zip_1: 
    #zip_1.extractall(directory + '_data/' + sf4) # Extract all the contents of zip file in current directory
df_D4D = pd.read_csv('crosswalk/D4D/ZIP-COUNTY-FIPS_2017-06.csv') # Import dataset saved as csv in _data folder
df_D4D['STCOUNTYFP'] = df_D4D['STCOUNTYFP'].astype("str") # Change data type of column in data frame
df_D4D['STCOUNTYFP'] = df_D4D['STCOUNTYFP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_D4D["FIPS"] = "FIPS"+ df_D4D['STCOUNTYFP'] # Combine string with column
df_D4D["Name"] = df_D4D["COUNTYNAME"] # Add single column
df_D4D["ST"] = df_D4D["STATE"] # Add single column
df_D4D = df_D4D[df_D4D.ST != "PR"] # Remove territories
df_D4D = df_D4D[df_D4D.ST != "GU"] # Remove territories
df_D4D = df_D4D[df_D4D.ST != "VI"] # Remove territories
df_D4D = df_D4D.filter(["FIPS", "ST", "Name", "STCOUNTYFP"]) # Keep only selected columns
df_D4D = df_D4D.drop_duplicates(keep = "first", inplace = False) # Drop all dupliacted values
df_D4D.info() # Get class, memory, and column info: names, data types, obs.
df_D4D.head() # Print first 5 observations

## Housing and Urban Development crosswalk
#sr4b = 'https://www.huduser.gov/portal/datasets/usps_crosswalk.html'
#query_s4 = ("https://" + hud_key) # Save API as query
#df_HUD = pd.read_csv(query_d4) # Create data frame from APi query
df_HUD = pd.read_csv("HUD/ZIP_COUNTY_032020.csv") # Import dataset saved as csv in _data folder
df_HUD['ZIP'] = df_HUD['ZIP'].astype("str") # Change data type of column in data frame
df_HUD['STCOUNTYFP'] = df_HUD['COUNTY'].astype("str") # Change data type of column in data frame
df_HUD['ZIP'] = df_HUD['ZIP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_HUD['STCOUNTYFP'] = df_HUD['STCOUNTYFP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_HUD["ZCTA"] = "ZCTA"+ df_HUD['ZIP'] # Combine string with column
df_HUD["FIPS"] = "FIPS"+ df_HUD['STCOUNTYFP'] # Combine string with column
df_HUD = df_HUD.filter(["FIPS", "ZCTA", "TOT_RATIO", "ZIP"]) # Keep only selected columns
df_HUD = df_HUD.sort_values(by = ["ZCTA", "TOT_RATIO"], ascending = False) # Select Zip codes with max ratio
df_HUD = df_HUD.drop_duplicates(subset = "ZCTA", keep = "first", inplace = False) # Drop all dupliacted values
df_HUD = df_HUD.drop(columns = ["TOT_RATIO"]) # Drop Unwanted Columns
df_HUD.info() # Get class, memory, and column info: names, data types, obs.
df_HUD.head() # Print first 5 observations

## American Community Survey population data
query = ('https://api.census.gov/data/2019/acs/acs5/profile?get=DP02_0001E&for=zip%20code%20tabulation%20area&key=' + key_census) # Save API query
df_ACS = pd.read_json(query) # Pull Data from API (JSON)
df_ACS.columns = df_ACS.iloc[0] # Save first row as column names
df_ACS = df_ACS.iloc[1:] # Remove first row
df_ACS = df_ACS.rename(columns = {'zip code tabulation area':'ZCTA' 
                                                    #,'DP02_0001E':'population', 
                                                    #'DP02_00XX':'pop_25to34', 
                                                    #'DP02_00XX':'pop_35to44',
                                                    #'DP02_00XX':'pop_45to54',
                                                    #'DP02_00XX':'pop_55to64',
                                                    #'DP02_00XX':'pop_65to74',
                                                    #'DP02_00XX':'pop_75to84',
                                                    #'DP02_00XX':'pop_85up'
                                                     })
df_ACS['ZCTA'] = df_ACS['ZCTA'].astype('str') # Change data type of column in data frame
df_ACS['ZCTA'] = 'ZCTA' + df_ACS['ZCTA'] # Add ZCTA label
df_ACS = df_ACS.drop(columns = 'state') # Drop unwanted columns
df_ACS.head() # Verify

## Join HUD, D4D, and ACS population data
df_full = pd.merge(df_HUD, df_D4D, on = "FIPS", how = "left") # Join by column while keeping only items that exist in both, select outer or left for other options
df_full = pd.merge(df_full, df_ACS, on = "ZCTA", how = "left") # Join by column while keeping only items that exist in both, select outer or left for other options
df_full.head() # Verify

## Clean Labels
states = {'ST':  ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MS', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
        'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        } # Create pandas dataframe by hand by creating arrays of same lenght with lables and saving as object
df_label = pd.DataFrame(states, columns = ['ST','State']) # Create data frame in pandas
df_label = pd.merge(df_full, df_label, on = "ST", how = "left") # Join by column while keeping only items that exist in both, select outer or left for other options
df_label["County"] = df_label["Name"] # Add new column based on existing
df_label['Name'] = df_label['Name'].str.replace(" County","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Parish","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" City","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Census Area","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Borough","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" and","") # Strip all spaces from column in data frame
df_label['NAME'] = df_label['Name'].str.upper() # Change column to uppercase
df_label['COUNTY'] = df_label['County'].str.upper() # Change column to uppercase
df_label['STATE'] = df_label['State'].str.upper() # Change column to uppercase
df_label = df_label.reindex(sorted(df_label.columns), axis=1) # order columns alphabetically
df_label =  df_label.rename(columns = {'COUNTY_L':'County', 'NAME_L':'Name', 'STATE_L':'State'}) # Rename multiple columns in place
df_label = df_label.drop_duplicates(subset = ['ZCTA']) # Drop duplicate ZCTA values
df_label['population'] = df_label['population'].fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_label['population'] = df_label'population'].replace(to_replace = 0, value = 1) # Rapleace all unpopulated Zip codes with value of 1
df_label = df_label.dropna(subset = ['ST']) # Define in which columns to look for missing values
df_label.info() # Get class, memory, and column info: names, data types, obs.
df_label.head() # Print first 5 observations

## Write to CSV
df_label.to_csv(path_or_buf = 'crosswalk/FIPS_ZCTA.csv', index = False) # Clean in excel and select variable
df_label.to_sql('FIPS_ZCTA', data_conn, if_exists = 'replace', index = 'ZCTA') # Export to SQL database

## Generate documentation
text_README = open('crosswalk/README.md', 'w') # Write new corresponding text file
text_README.write('#Healthy Neighborhood Project\n') # First level header
text_README.write('##County-Zip Code Crosswalk File\n') # Second level header
text_README.write('###About\n') # Third level header
text_README.write('This directory contains files and code to develop corsswalk files used to join different geographic layers. The crosswalk files contain various lables and IDs used for various sources. Since zip codes and counties do not cleanly overalp, various files available from publicly available sources are used to create a key that can be used to join these two layers as best as possible.') # Formal description of data source.
text_README.write('\n\n') # Add section break
text_README.write('###Contents\n') # Third level header
text_README.write('`D4D`            County and State labels in a single dataset available from "Data for Democracy"<br>\n') # Description of file in directory
text_README.write('`HUD`  	    Data from Dept. of Housing and Urbvan development that shows overlap fo zip codes with counties<br>\n') # Description of file in directory
text_README.write('`ZCTA_FIPS.py`   Python script used to pull data from various sources, clean, and export the FIPS_ZCTA crosswalk file<br>\n') # Description of file in directory
text_README.write('`ZCTA_FIPS.csv`  Crosswalk file that connects zip codes (table ID) with counties and states along with a variety of lables useful in joining with other sources and Census shapefiles<br>\n') # Description of file in directory
text_README.write('\n\n') # Add section break
text_README.write('<break>\n') # Description of file in directory
text_README.write('Updated  ' + stamp + ' by ' + user + '\n') # Description of file in directory
text_README.write('<copywrite> allocativ 2021\n') # Description of file in directory
text_README.close() # Close file