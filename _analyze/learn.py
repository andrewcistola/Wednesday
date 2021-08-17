query = '''
    SELECT healthDat.*, fl_zip.County
    FROM healthDat 
    LEFT JOIN fl_zip 
    ON healthDat.Zip = fl_zip.Zip
    ;'''
df_Q = pd.read_sql_query(query, con_sqlite)
df_Q['Gender'] = df_Q['Gender'].replace(['female', 'male'], [1, 0])
df_Q['ER_Copay'] = df_Q['ER_Copay'].str.replace('$', '').astype('int')
df_Q['PCP_Copay'] = df_Q['PCP_Copay'].str.replace('$', '').astype('int')
df_Q = df_Q.rename(columns = {'CC_Count': 'Comorbidity'})
df_Q.info()

id = 'PatientID'
cost = 'HP_Paid'
age = 'Age'
sex = 'Gender'
geo = 'Zip'
acuity = 'Comorbidity'
ED = 'ER_Count'
IP = 'IP_Visits'

Util = ['IP_Visits', 'ER_Count']
Copay = ['ER_Copay', 'PCP_Copay']
AA = ['Area_County', 'Area_3Zip', 'Age_10Year', 'Age_ACA', 'Total']

df_A = df_Q

df_A['Total'] = 'All Ages and Areas'

bins_Groups = [0,5,10,15,20,25,35,45,55,65,75,85,100]
labels_Groups = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85up']
df_A['Age_10Year'] = pd.cut(df_A['Age'], bins = bins_Groups, right = False, labels = labels_Groups)

bins_Life = [0,18,26,30,65,100]
labels_Life = ['Pediatric', 'College', 'Young Adult', 'Working Adult', 'Retired Adult']
df_A['Age_Life'] = pd.cut(df_A['Age'], bins = bins_Life, right = False, labels = labels_Life)

def funx(list):
    if list in ['Pediatric', 'College']:
        return "Dependent"
    elif list in ['College', 'Young Adult']:
        return 'Catastrophic'
    elif list in ['College', 'Young Adult', 'Working Adult']:
        return 'Marketplace'
    elif list in ['Retired Adult']:
        return 'Medicare'
    else: return 'NA'
items = df_A['Age_Life'].to_list()
new_list = []
for i in items:
    new_list.append(funx(i))
df_A['Age_ACA'] = new_list
df_A = df_A.drop(columns = 'Age_Life')

df_A = df_A.rename(columns = {'County': 'Area_County'})

df_A['Area_3Zip'] = df_A['Zip'].astype(str).str[:-2].describe()

df_A.info()
with pd.ExcelWriter('_data/learn_result.xlsx') as writer:  
    df_A.to_excel(writer, sheet_name = 'Data')

for A in AA:
#A = Age[1]
    df1 = df_A.filter([id, A]).groupby(by = A).count()
    df1.columns = ['Population']
    df2 = df_A.filter([id, A]).groupby(by = A).count()
    df2.columns = ['Population']
    df3 = df_A.filter([id, A]).groupby(by = A).count()
    df3.columns = ['Population']
    df1['Cost_Total'] = df_A.filter([cost, A]).groupby(by = A).sum()[cost].round().astype('int')
    df2['Cost_Beneficiary'] = df_A.filter([cost, A]).groupby(by = A).mean()[cost].round(2)
    df3['Cost_Cumulative'] = (df_A.filter([cost, A]).groupby(by = A).sum() / df_A[cost].sum() * 100).round(2)
    df1['IP_Visits'] = df_A.filter([IP, A]).groupby(by = A).sum()[IP]
    df2['IP_Avg'] = df_A.filter([IP, A]).groupby(by = A).mean()[IP].round(2)
    df3['IP_Portion'] = (df_A.filter([IP, A]).groupby(by = A).sum() / df_A[IP].sum() * 100).round(2)
    df1['ED_Visits'] = df_A.filter([ED, A]).groupby(by = A).sum()[ED]
    df2['ED_Avg'] = df_A.filter([ED, A]).groupby(by = A).mean()[ED].round(2)
    df3['ED_Portion'] = (df_A.filter([ED, A]).groupby(by = A).sum() / df_A[ED].sum() * 100).round(2)
    CC = df_A.drop(columns = [id, cost, age, sex, geo, acuity] + Util + Copay + Age).columns.to_list()
    for c in CC:
    #c = CC[1]
        df1[c.strip('CC_') + '_Cases'] = df_A[df_A[c] == 1].filter([id, A, c]).groupby(by = A).count()[c]
        df2[c.strip('CC_') + '_Prev'] = (df_A[df_A[c] == 1].filter([id, A, c]).groupby(by = A).count()[c] / df2['Population'] * 1000).round(2)
        df3[c.strip('CC_') + '_Pop'] = (df_A[df_A[c] == 1].filter([id, A, c]).groupby(by = A).count()[c] / df_A[c].sum() * 100).round(2)
    df1 = df1.reset_index()
    df1['Group'] = df1[A].astype('str')
    df1 = df1.drop(columns = A)
    df1 = df1.set_index('Group')
    df1.loc['Gross Total', :] = df1.sum(axis = 0)
    with pd.ExcelWriter('_data/learn_result.xlsx', mode = 'a') as writer:  
        df1.to_excel(writer, sheet_name = A + '_Counts')
    df2 = df2.reset_index()
    df2['Group'] = df2[A].astype('str')
    df2 = df2.drop(columns = A)
    df2 = df2.set_index('Group')
    df2.loc['Adjusted Rate', :] = df2.mean(axis = 0)
    with pd.ExcelWriter('_data/learn_result.xlsx', mode = 'a') as writer:  
        df2.to_excel(writer, sheet_name = A + '_Rates')
    df3 = df3.reset_index()
    df3['Group'] = df3[A].astype('str')
    df3 = df3.drop(columns = A)
    df3 = df3.set_index('Group')
    df3.loc['Group w Highest Prct', :] = df3.idxmax(axis = 0)
    with pd.ExcelWriter('_data/learn_result.xlsx', mode = 'a') as writer:  
        df3.to_excel(writer, sheet_name = A + '_Percents')
    Bin = pd.Series(df_A[A].unique())
    for B in Bin:
    #B = Bin[0]
        df_XY = df_A[df_A[A] == B].drop(columns = Age)
        df_X = df_XY.drop(columns = [cost, geo]).set_index(id)
        df_Y = df_XY.filter([id, cost]).set_index(id)
        X = StandardScaler().fit_transform(df_X.to_numpy())
        Y = StandardScaler().fit_transform(df_Y.to_numpy())
        forest = RandomForestRegressor(n_estimators = 1000, max_depth = 10)
        forest.fit(X, Y)
        pca = PCA(n_components = 'mle')
        pca.fit_transform(df_X)
        recursive = RFECV(estimator = LinearRegression(), min_features_to_select = 5) 
        recursive.fit(X, Y)
        df4 = pd.DataFrame(data = {'Feature': df_X.columns, 
                                        'Importance': forest.feature_importances_,
                                        'Variance': pca.components_[1,:],
                                        'Elimination': recursive.ranking_
                                        })
        df4['Importance'] = df4['Importance'].rank(ascending = False).astype('int')
        df4['Variance'] = df4['Variance'].rank(ascending = False).astype('int')
        df4['Overall'] = ((df4['Variance'] + df4['Importance'] + df4['Elimination']) / 3).rank(ascending = True, method = 'dense').astype('int')
        df4 = df4.sort_values(by = 'Overall', ascending = True)
        with pd.ExcelWriter('_data/learn_result.xlsx', mode = 'a') as writer:  
            df4.to_excel(writer, sheet_name = B)


query = '''
    SELECT healthDat.*, fl_zip.County
    FROM healthDat 
    LEFT JOIN fl_zip 
    ON healthDat.Zip = fl_zip.Zip
    ;'''
df_Q = pd.read_sql_query(query, con_sqlite)
df_Q['Gender'] = df_Q['Gender'].replace(['female', 'male'], [1, 0])
df_Q['ER_Copay'] = df_Q['ER_Copay'].str.replace('$', '').astype('int')
df_Q['PCP_Copay'] = df_Q['PCP_Copay'].str.replace('$', '').astype('int')
df_Q = df_Q.rename(columns = {'CC_Count': 'Comorbidity'})
df_Q.info()

id = 'PatientID'
cost = 'HP_Paid'
age = 'Age'
sex = 'Gender'
geo = 'Zip'
acuity = 'Comorbidity'
ED = 'ER_Count'
IP = 'IP_Visits'

Util = ['IP_Visits', 'ER_Count']
Copay = ['ER_Copay', 'PCP_Copay']
County = ['Metro', 'Miami']

df_C = df_Q