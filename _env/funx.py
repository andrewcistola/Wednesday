# Define Function
def API( # Generic Query, clean, export
    title, # Dataset title
    pub, # Dataset publisher
    link, # Dataset link
    dict, # Dataset dictionary link
    meta, # Dataset metadata link
    label, # Dataset file label
    path, # Path to dataset directory
    query, # Save API as query
    geoid, # Column name used in dataset to represent GEOID label
    keep, # String value in all columns of interest
    layer, # Column label for geographic layer used for observations (ZCTA or FIPS)
    conn, # Connection to SQL database
    local # Local path to allocativ repository
    ):    
        df = pd.read_csv(query) # Create data frame from APi query
        df.to_csv(path_or_buf = path + 'raw.csv', index = layer) # Export to csv
        df.loc[:, df.columns.str.contains(keep | geoid)] # Select columns by string value
        df[layer] = layer + df[geoid].astype("str").str.rjust(5, "0") # Add leading zeros of character column using rjust() function
        df.drop(columns = geoid) # Drop original geoid column
        df.to_sql(label, conn, if_exists = 'replace', index = layer) # Export dataframe to SQL database
        df.to_csv(path_or_buf = path + 'stage.csv', index = layer) # Export to csv
        urllib.request.urlretrieve(dict, path + 'dict.pdf') # Get file from url and save at location
        urllib.request.urlretrieve(meta, path + 'meta.xml') # Get file from url and save at location
        README = open(path + 'README', 'w') # Write new corresponding text file
        README.write('This data was collected from the ' + title + ' published by the ' + pub + ' publically available at ' + link + '.') # Formal description of data source.
        README.write('\n\n') # Add section break
        README.write('raw       Data originally accessed in raw form without manipulation\n') # Description of file in directory
        README.write('stage	    Data exported as comma delimited file ready for analysis\n') # Description of file in directory
        README.write('meta	    Metadata associated with file including description, reference, access link, and dictionary source\n') # Description of file in directory
        README.write('API  	    Python script used to pull data from API and clean\n') # Description of file in directory
        README.write('dict      Data dictionary downloaded directly from source along with raw data\n') # Description of file in directory
        README.write('\n\n') # Add section break
        README.write('Updated  ' + stamp + '\n') # Description of file in directory
        README.write('User     ' + user + '\n') # Description of file in directory
        README.close() # Close file

# Define Function
def URL( # Generic download flatfile from URL
    title, # Dataset title
    pub, # Dataset publisher
    link, # Dataset link
    dict, # Dataset dictionary link
    meta, # Dataset metadata link
    label, # Dataset file label
    path, # Path to dataset directory
    geoid, # Column name used in dataset to represent GEOID label
    keep, # String value in all columns of interest
    layer, # Column label for geographic layer used for observations (ZCTA or FIPS)
    conn, # Connection to SQL database
    local # Local path to allocativ repository
    ):
        urllib.request.urlretrieve(link, path + label + '.zip') # Get file from url and save at location
        with ZipFile(path + label + '.zip', 'r') as zip_file: 
            zip_file.extractall(path + label) # Extract all the contents of zip file in current directory
        os.remove(path + label + '.zip') # Delete original Zip folder
        df = pd.read_csv(path + label + '.csv') # Create data frame from APi query
        df.loc[:, df.columns.str.contains(keep | geoid)] # Select columns by string value
        df[layer] = layer + df[geoid].astype("str").str.rjust(5, "0") # Add leading zeros of character column using rjust() function
        df.drop(columns = geoid) # Drop original geoid column
        df.to_sql(label, conn, if_exists = 'replace', index = layer) # Export dataframe to SQL database
        df.to_csv(path_or_buf = path + 'stage.csv', index = layer) # Export to csv
        urllib.request.urlretrieve(dict, path + 'dict.pdf') # Get file from url and save at location
        urllib.request.urlretrieve(meta, path + 'meta.xml') # Get file from url and save at location
        README = open(path + 'README', 'w') # Write new corresponding text file
        README.write('This data was collected from the ' + title + ' published by the ' + pub + ' publically available at ' + link + '.') # Formal description of data source.
        README.write('\n\n') # Add section break
        README.write('raw       Data originally accessed in raw form without manipulation\n') # Description of file in directory
        README.write('stage	    Data exported as comma delimited file ready for analysis\n') # Description of file in directory
        README.write('meta	    Metadata associated with file including description, reference, access link, and dictionary source\n') # Description of file in directory
        README.write('API  	    Python script used to pull data from API and clean\n') # Description of file in directory
        README.write('dict      Data dictionary downloaded directly from source along with raw data\n') # Description of file in directory
        README.write('\n\n') # Add section break
        README.write('Updated  ' + stamp + '\n') # Description of file in directory
        README.write('User     ' + user + '\n') # Description of file in directory
        README.close() # Close file

# Define Function
def Public_Library( # Generic download flatfile from URL
    title, # Dataset title
    pub, # Dataset publisher
    link, # Dataset link
    dict, # Dataset dictionary link
    meta, # Dataset metadata link
    label, # Dataset file label
    path, # Path to dataset directory
    geoid, # Column name used in dataset to represent GEOID label
    keep, # String value in all columns of interest
    layer, # Column label for geographic layer used for observations (ZCTA or FIPS)
    conn, # Connection to SQL database
    local # Local path to allocativ repository
    ):
        if access == 'API':
            df = pd.read_csv(query) # Create data frame from APi query
            df.to_csv(path_or_buf = path + 'raw.csv', index = layer) # Export to csv
        if access == 'URL':
            urllib.request.urlretrieve(link, path + label + '.zip') # Get file from url and save at location
            with ZipFile(path + label + '.zip', 'r') as zip_file: 
                zip_file.extractall(path + label) # Extract all the contents of zip file in current directory
            os.remove(path + label + '.zip') # Delete original Zip folder
            df = pd.read_csv(path + label + '.csv') # Create data frame from APi query
        df.loc[:, df.columns.str.contains(keep | geoid)] # Select columns by string value
        df[layer] = layer + df[geoid].astype("str").str.rjust(5, "0") # Add leading zeros of character column using rjust() function
        df.drop(columns = geoid) # Drop original geoid column
        df.to_sql(label, conn, if_exists = 'replace', index = layer) # Export dataframe to SQL database
        df.to_csv(path_or_buf = path + 'stage.csv', index = layer) # Export to csv
        urllib.request.urlretrieve(dict, path + 'dict.pdf') # Get file from url and save at location
        urllib.request.urlretrieve(meta, path + 'meta.xml') # Get file from url and save at location
        README = open(path + 'README', 'w') # Write new corresponding text file
        README.write('This data was collected from the ' + title + ' published by the ' + pub + ' publically available at ' + link + '.') # Formal description of data source.
        README.write('\n\n') # Add section break
        README.write('raw       Data originally accessed in raw form without manipulation\n') # Description of file in directory
        README.write('stage	    Data exported as comma delimited file ready for analysis\n') # Description of file in directory
        README.write('meta	    Metadata associated with file including description, reference, access link, and dictionary source\n') # Description of file in directory
        README.write('pull      Python script used to pull data from API/URL and clean\n') # Description of file in directory
        README.write('dict      Data dictionary downloaded directly from source along with raw data\n') # Description of file in directory
        README.write('\n\n') # Add section break
        README.write('Updated  ' + stamp + '\n') # Description of file in directory
        README.write('User     ' + user + '\n') # Description of file in directory
        README.close() # Close file