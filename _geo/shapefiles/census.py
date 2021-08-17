## Shape Step 1: Import Zip Code Shapefile from URL and Extract
ss1 = 'Import Zip Code Geographies from Shapefile' # Step descriptive title
sd1 = 'CENSUS TIGER 2020 Shapefiles by Zip Code' # Step file description
sr1 = 'https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_zcta510_500k.zip' # Step download or reference url
sf1 = 'CENSUS_TIGER_2018_ZCTA' # Step file label

### Get Dataset as Zip file from URL address
file_name, headers = urllib.request.urlretrieve(sr1, directory + '_shape/' + sf1 + '.zip') # Get file from url and save at location
with ZipFile(directory + '_shape/' + sf1 + '.zip', 'r') as zip_1: 
    zip_1.extractall(directory + '_shape/' + sf1) # Extract all the contents of zip file in current directory
os.remove(directory + '_shape/' + sf1 + '.zip') # Delete original Zip folder

sd2 = 'CENSUS TIGER 2020 Shapefiles by County' # Step file description
sr2 = 'https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/tl_2020_us_county.zip' # Step download or reference url
sf2 = 'CENSUS_TIGER_2018_FIPS' # Step file label
