data_list = os.listdir('_data/private/')
for data in data_list:
    df = pd.read_csv('_data/private/' + data)
    data_label = data.rstrip('.csv')
    df.to_sql(data_label, con_sqlite, index = False)
    df_2 = pd.read_sql_query('SELECT ' + data_label + '.* FROM ' + data_label + ';', con_sqlite)
    if df.equals(df_2) is True:
        print('Data file', data, 'imported successfully as table', data_label)
    buffer = io.StringIO()
    df.info(buf = buffer)
    pd.set_option('display.max_columns', None)
    data_text = open('_docs/' + data_label + '.txt', 'w')
    data_text.write(data + ' Documentation\n\n')
    data_text.write(buffer.getvalue() + '\n\n')
    data_text.write('Table name in `_data/project.db`: ' + data_label + '\n\n')
    data_text.write(str(df.describe()) + '\n\n')
    data_text.write('Updated: ' + stamp)
    data_text.close()
    df = []
    df_2 = []