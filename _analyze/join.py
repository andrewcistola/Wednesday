query = '''
    SELECT healthDat.*, fl_zip.*
    FROM healthDat 
    LEFT JOIN fl_zip 
    ON healthDat.Zip = fl_zip.Zip
    ;'''
df_Q = pd.read_sql_query(query, con_sqlite)
df_Q.info()