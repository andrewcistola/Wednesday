gmaps = googlemaps.Client(key = key_google)
locations = df['coords']
address = []
for coords in locations:
    full = gmaps.reverse_geocode(coords)
    address.append(full)
df['address'] = address