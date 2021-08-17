# Define Variables from lists
titles = [''], # Dataset title
pubs = [''], # Dataset publisher
links = [''], # Dataset link
dicts = [''], # Dataset dictionary link
metas = [''], # Dataset metadata link
labels = [''], # Dataset file label
paths = [''], # Path to dataset directory
querys = [''], # Save API as query
geoids = [''], # Column name used in dataset to represent GEOID label
keeps = [''], # String value in all columns of interest
layers = [''], # Column label for geographic layer used for observations (ZCTA or FIPS)
conns = [''], # Connection to SQL database
locals = [''] # Local path to allocativ repository

# Define Variables from data library
df_library = pd.read_csv('_data/_public/library.csv')
titles = df_library['title'] # Dataset title
pub = df_library['pub'], # Dataset publisher
link = df_library['link'], # Dataset link
dict = df_library['dict'], # Dataset dictionary link
meta = df_library['meta'], # Dataset metadata link
label = df_library['label'], # Dataset file label
path = df_library['path'], # Path to dataset directory
query = df_library['query'], # Save API as query
geoid = df_library['geoid'], # Column name used in dataset to represent GEOID label
keep = df_library['keep'], # String value in all columns of interest
layer = df_library['layer'], # Column label for geographic layer used for observations (ZCTA or FIPS)
conn = df_library['conn'], # Connection to SQL database
local = df_library['local'] # Local path to allocativ repository

for title, pub, link, dict, meta, label, path, query, geoid, keep, layer, conn, local 
    in titles, pubs, links, dicts, metas, labels, paths, querys, geoids, keeps, layers, conns, locals:
        API(
            title = title, # Dataset title
            pub = pub, # Dataset publisher
            link = link, # Dataset link
            dict = dict, # Dataset dictionary link
            meta = meta, # Dataset metadata link
            label = label, # Dataset file label
            path = path, # Path to dataset directory
            query = query, # Save API as query
            geoid = geoid, # Column name used in dataset to represent GEOID label
            keep = keep, # String value in all columns of interest
            layer = layer, # Column label for geographic layer used for observations (ZCTA or FIPS)
            conn = conn, # Connection to SQL database
            local = local # Local path to allocativ repository
            )

for title, pub, link, dict, meta, label, path, query, geoid, keep, layer, conn, local 
    in titles, pubs, links, dicts, metas, labels, paths, querys, geoids, keeps, layers, conns, locals:
        URL(
            title = title, # Dataset title
            pub = pub, # Dataset publisher
            link = link, # Dataset link
            dict = dict, # Dataset dictionary link
            meta = meta, # Dataset metadata link
            label = label, # Dataset file label
            path = path, # Path to dataset directory
            query = query, # Save API as query
            geoid = geoid, # Column name used in dataset to represent GEOID label
            keep = keep, # String value in all columns of interest
            layer = layer, # Column label for geographic layer used for observations (ZCTA or FIPS)
            conn = conn, # Connection to SQL database
            local = local # Local path to allocativ repository
            )