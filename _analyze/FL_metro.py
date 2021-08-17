def funx(list):
    if list in ['Duval']:
        return 'Jacksonville'
    elif list in ['Leon']:
        return 'Tallahassee'
    elif list in ['Alachua']:
        return 'Gainesville'
    elif list in ['Orange']:
        return 'Orlando'
    elif list in ['Miami-Dade']:
        return 'Miami'
    elif list in ['Hillsborough']:
        return 'Tampa Bay'
    elif list in ['Lee']:
        return 'Ft. Myers'
    elif list in ['Palm Beach']:
        return 'Palm Beach'
    elif list in ['Broward']:
        return 'Ft. Lauderdale'
    elif list in ['Pinellas']:
        return 'St. Petersburg'
    elif list in ['Monroe']:
        return 'Key West'
    elif list in ['Bay']:
        return 'Panama City Beach'
    else: 
        return 'Non-metro'
items = df_C['County'].to_list()
new_list = []
for i in items:
    new_list.append(funx(i))
df_C['Metro'] = new_list

def funx(list):
    if list in ['Miami-Dade'] or ['Palm Beach'] or ['Broward']:
        return 'Miami'
    else: 
        return 'Everywhere Else'
items = df_C['County'].to_list()
new_list = []
for i in items:
    new_list.append(funx(i))
df_C['Miami'] = new_list