# Data Portfolio
# Python Toolbox

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation
import datetime # time stamping in Python
import requests # Request objects by url

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'
import numpy as np # Widely used matrix library for numerical processes

### Set working directory
os.chdir("C:/Users/drewc/GitHub") # Set wd to project repository

### Import datasets from csv files
df_ = pd.read_csv("_data/data.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Verify
df_.info() # Get class, memory, and column info: names, data types, obs.
df_.head() # Print first 5 observations
df_.dim() # Print dimensions on data frame
df_.describe() # Run descriptive statistics on all columns

### Write to CSV
df_value.to_csv(r"_data/mungos_np_value.csv") # Clean in excel and select variable

### Write to Text File
text_1 = str(df_nh.shape)
text_file = open("_fig/_results.txt", "w") # Open text file and name with subproject, content, and result suffix
text_file.write("Project Neville\n") # Line of text with space after
text_file.write("NHANES 2005-2006: Undiagnosed Type 2 Diabetes\n") # Line of text with space after
text_file.write("\nTotal Cohort\n") # Line of text with space after
text_file.write(text_1) # write string version of variable above
text_file.write("\n") # Add two lines of blank text at end of every section text
text_file.close() # Close file

### Append to Text File
text_1 = df_rfe.to_string() # Save variable as string value for input below
text_file = open("_fig/_results.txt", "a") # Open text file and name with subproject, content, and result suffix
text_file.write("\nRecursive Feature Elimination\n") # Line of text with space after
text_file.write("\nSelected Features by Cross-Validation\n") # Line of text with space after
text_file.write(text_1) # write string version of variable above
text_file.write("\n") # Add two lines of blank text at end of every section text
text_file.close() # Close file

#################### Break ####################

# Prepare data for analysis

## Data manipulation with pandas
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'
import numpy as np # Widely used matrix library for numerical processes

### Duplicates and Missing Values
df_ = df_.drop_duplicates(subset = "ColA", keep = "first", inplace = True) # Drop all dupliacted values
unique = df["ColA"].unique() # Print Unique Values in Column
df_ = df_.dropna() # Drop all rows with NA values
df.dropna(subset=['name', 'born']) # Define in which columns to look for missing values:
df_ = df_.fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_c19.replace([np.inf, -np.inf], np.nan) # Replace infitite values with na


### Data types and objects
data = {'Features': [features], 'beta': [coef]} # Save model objects asvariable for data frame
df_reg = pd.DataFrame(data) # Save as Pandas dataframe
df["ColA"] = df["ColA"].astype("int64") # Change data type of column in data frame
df["ColB"] = df["ColB"].astype("float64") # Change data type of column in data frame
df["Date"] = df["Date"].astype("datetime64") # Change data type of column in data frame
df_c19["ZIP"] = df_c19["ZIP"].astype("str") # Change data type of column in data frame
df_ = df_.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df = ser.to_frame(ser) # Convert Series to Dataframe
df_acs = df_acs.select_dtypes(exclude = ['int64']) # Drop all data types of certain column

### Modify data frame structure
wide = long.pivot_table(index = "ColA", columns = "ColB", values = "ColC") # Pivot from Long to Wide Format
index = df.reset_index(level = ["ColA", "ColB"]) # Reset Index
df_index = df_risk.set_index("Question") # Set column as index
del df_index.index.name # Delete index name
sort = df.sort_values(by = ["ColA"], ascending = False) # Sort Columns by Value
tran = df.transpose() # Transpose Rows and Columns

### Modify columns in data frame
drop = df.drop(columns = ["ColA", "ColB"]) # Drop Unwanted Columns
drop = bmi.filter(["UndgPD", "WTMEC2YR"]) # Keep only selected columns
df["ColB"] = df["ColA"] # Add single column
name =  df.rename(columns = {"ColA": "A", "ColB": "B"}) # Rename multiple columns in place
df1["ColDiff"] = df1["ColA"] - df1["ColB"] # Create column based on math
df["ColC"] = np.where(df["ColA"] >= 50, "yes", "no") # Create New Column Based on Conditions
df_fun["LastFirst"] = df_fun["Last"] + df_fun["First"] # Create column of two str columns combined
df['Col1']=df['Col1'].str.rjust(10, "0") # add leading zeros of character column using rjust() function
df1['State'] = df1['State'].str.replace(" ","") # Strip all spaces from column in data frame
df_ = df.loc[:, df.columns.str.contains('alp')] # Select columns by string value
df_D4D = df_D4D[df_D4D.ST != "PR"] # Drop rows by condition
df_pca2 = df_pca2.abs() # get absolute value for column or data frame
df = df.reindex(sorted(df.columns), axis=1) # order columns alphabetically
first = df_HUD.pop("ZCTA") # 'pop' column from df
df_HUD.insert(0, "ZCTA", first) # reinsert in index
df_c19["ZCTA"] = "ZCTA" + df_c19["ZIP"] # Add character string to each row in column

### Subset Data frame
df_acs = df_acs[df_acs["ST"] == "FL"] # Subset by character 
df_ = df_[df_.ColA > 5] # Susbet numeric column by condition
df_ = df_[(df_["ColA"] =< 5) or (df_["ColB"] == False)] # Susbet numeric column by multiple conditions
dfdate = df[(df["Date"] > "2002-01-01 0:00") & (df["Date"] < "2002-12-31 23:59")] # Susbet date column by multiple conditions
dfstr = df[df["ColS"].str.contains("string")] # Subset character column by string
dfna = df[df["ColA"].isnull() # Subset by NA Value
df_key = df_join3.loc[0, :] # Save selection of rows with all columns as df

### Merge Join Group in data frame
df_join = pd.merge(df_A, df_B, on = "ColAB", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
stack = pd.concat([df1, df2]) # Combine rows with same columns
df_group = df_filter.groupby(["Source"], as_index = False).sum() # Group data by columns and sum
df_group = df_filter.groupby(["Source"], as_index = False).count() # Group data by columns and count
df_group = df_filter.groupby(["Source"], as_index = False).mean() # Group data by columns and average

### Arithmetic on Data Frame
result = df.sum(axis = 0) # Sum axis = 0 for column, 1 for row
result = df.mean(axis = 1)# Median axis = 0 for column, 1 for row
result = df.median(axis = 1) # Median axis = 0 for column, 1 for row

### Strings and lists
mrfractureproof = fractureproof.append(mr) # Append item to end of list
mrfractureproof = fractureproof.remove() # Insert variables for hand removal

### Verify
df_.info() # Get class, memory, and column info: names, data types, obs.
df_.head() # Print first 5 observations

#################### Break ####################

# Create machine learning prediction models

## Data Preparation with scikit-learn
from sklearn.impute import SimpleImputer # Univariate imputation for missing data
from sklearn.preprocessing import StandardScaler # Standard scaling for easier use of machine learning algorithms

### Drop features with less than 75% data
df_NA = df_sub # Rename data for missing values
df_NA = df_NA.dropna(axis = 1, thresh = 0.75*len(df_NA)) # Drop features less than 75% non-NA count for all columns
NAtot = df_NA.isnull().sum().sum() # Get count of all NA values
NAnot = df_NA.count().sum().sum() # Get count of all nonNA values
NAratio = NAtot / (NAtot + NAnot) # Percent of values with values
Nout = (df_NA["outcome"] == 1).sum() # Get cout of outcome variable
print(NAratio) # Print value
print(Nout) # Print value
df_NA.info() # Get info

### Impute missing values
imp = SimpleImputer(strategy = "median") # Build Imputer model. strategy = "mean" or " median" or "most_frequent" or "constant"
df_imp = pd.DataFrame(imp.fit_transform(df_NA)) # Impute missing data
df_imp.columns = df_NA.columns # Rename columns from new dataset

### Standard Scale Values
df_stsc = df_imp.drop(columns = ["outcome"])  # Remove outcome variable
x = df_stsc.values # Save feature values as x
x = StandardScaler().fit_transform(x) # While applying StandardScaler, each feature of your data should be normally distributed such that it will scale the distribution to a mean of zero and a standard deviation of one.
x.shape # Verify that dimensions are same length
np.mean(x),np.std(x) # whether the normalized data has a mean of zero and a standard deviation of one.
df_stsc2 = pd.DataFrame(x, columns = df_stsc.columns) # convert the normalized features into a tabular format with the help of DataFrame.
df_stsc2["outcome"] = df_imp["outcome"]

### Rename as Neville
df_nev = df_stsc2 # Rename Data

### Verify
df_nev.info() # Get class, memory, and column info: names, data types, obs.
df_nev.head() # Print first 5 observations
df_nev.shape # Print dimensions of data frame

## Principal Component Analysis scikit-learn
from sklearn.decomposition import PCA # Principal compnents analysis from sklearn

### Isolate Data frame for Outcome
df_pca = df_nev[(df_nev["outcome"] == 1)] # Susbet for PD and DM
df_pca = df_pca.drop(columns = ["outcome"]) # Drop outcome variable

### Create PCA model to determine Components
pca = PCA(n_components = Nout) # you will pass the number of components to make PCA model based on Nout
pca.fit(df_pca) # fit to data
df_ev = pd.DataFrame(pca.explained_variance_) # Print explained variance of components
df_ev = df_ev[(df_ev[0] > 10)]
components = len(df_ev.index) # Save count of values for Variabel reduction

### PCA to reduce variables
pca = PCA(n_components = components) # you will pass the number of components to make PCA model
pca.fit_transform(df_pca) # finally call fit_transform on the aggregate data to create PCA results object
df_pca2 = pd.DataFrame(pca.components_, columns = df_pca.columns) # Export eigenvectors to data frame

### Collect list important features
df_pcs3 = df_pcs2[(df_pcs2 > 0)] # Remove all values below or equal to 0
df_pc = pd.DataFrame(df_pcs3.max()) # select maximum value for each feature
df_pc = df_pc.reset_index() # Save index as first column named "index"
df_pc = df_pc.rename(columns = {"index": "Features", 0: "Eigenvectors"}) # Rename columns
df_pc = df_pc.sort_values(by = ["Eigenvectors"], ascending = False) # Sort Columns by Value
df_pc = df_pc[(df_pc["Eigenvectors"] > df_pc["Eigenvectors"].mean())] # Subset by Gini values higher than mean
df_pc = df_pc.dropna() # Drop all rows with NA values, 0 = rows, 1 = columns 

### Verify
df_pc.info() # Get class, memory, and column info: names, data types, obs.
df_pc.head() # Print first 5 observations

## Random Forest with scikit-learn
from sklearn.ensemble import RandomForestClassifier # Random Forest classification component

### Modify for RFC
Y = df_nev["outcome"] # Isolate Outcome variable
features = df_nev.columns.drop(["outcome"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_nev[features] # Save features columns as predictor data frame
forest = RandomForestClassifier(n_estimators = 1000, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

### Fit Forest 
forest.fit(X, Y) # This will take time

### Output importances
gini = forest.feature_importances_ # Output importances of features
l_gini = list(zip(X, gini)) # Create list of variables alongside importance scores 
df_gini = pd.DataFrame(l_gini, columns = ["Features", "Gini"]) # Create data frame of importances with variables and gini column names
df_gini = df_gini.sort_values(by = ["Gini"], ascending = False) # Sort data frame by gini value in desceding order
df_gini = df_gini[(df_gini["Gini"] > df_gini["Gini"].mean())] # Subset by Gini values higher than mean

### Verify
df_gini.info() # Get class, memory, and column info: names, data types, obs.
df_gini.head() # Print first 5 observations

## Recursive feature elimination with scikit-learn
from sklearn.feature_selection import RFECV # Recursive Feature elimination with cross validation

### Setup Predictors and RFE
X = df_rfecv[features] # Save features columns as predictor data frame
Y = df_nev["outcome"] # Use outcome data frame 
Log_RFE = LogisticRegression(max_iter = 100, solver = "liblinear") # Use regression coefficient as estimator
selector = RFECV(estimator = Log_RFE, min_features_to_select = 1) # define selection parameters, in this case all features are selected. See Readme for more ifo

### Fit Recursive Feature Elimination
selected = selector.fit(X, Y) # This will take time

### Output RFE results
ar_rfe = selected.support_ # Save Boolean values as numpy array
l_rfe = list(zip(X, ar_rfe)) # Create list of variables alongside RFE value 
df_rfe = pd.DataFrame(l_rfe, columns = ["Features", "RFE"]) # Create data frame of importances with variables and gini column names
df_rfe = df_rfe[df_rfe.RFE == True] # Select Variables that were True
df_rfe = df_rfe.drop(columns = ["RFE"]) # Drop Unwanted Columns

### Verify
df_rfe.info() # Get class, memory, and column info: names, data types, obs.
df_rfe.head() # Print first 5 observations

## Regression Modeling in scikit-learn
from sklearn.linear_model import LogisticRegression # Used for machine learning with categorical outcome
from sklearn.linear_model import LinearRegression # Used for machine learning with quantitative outcome

### Linear Regression in Scikit Learn
x = df_reg[features] # features as x
y = df_reg["outcome"] # Save outcome variable as y
LR = LinearRegression() # Linear Regression in scikit learn
model = LR.fit(x, y) # Fit model
score = model.score(x, y) # rsq value
coef = model.coef_ # Coefficient models as scipy array
features = df_reg[features].columns # Get columns from features df

#################### Break ####################

# Conduct Statistical Tests

## Basic statistics with Scipy
import scipy.stats as st # Statistics package best for t-test, ChiSq, correlation

### Conduct chisq test
obs = df_chsq["Observed"]
exp = df_chsq["Expected"]
result = st.chisquare(obs, exp) # ChiSq with obs = observed and exp = observed

### Conduct t-test test
a = df_tt["Outcome"][df_tt.Predictor == 0] # Save dependent variable column for population means while subsetting by dependent varible column
b = df_tt["Outcome"][df_tt.Predictor == 1] # Save dependent variable column for population means while subsetting by dependent varible column
result = st.ttest_ind(a, b) # Scipy T-test for independent samples, return will be (t-statisitic, p-value)

### Pearson's correlation
x = df_corr["Predictor"])
y = df_corr["Outcome"])
result = st.pearsonr(x, y)

### Spearman's rank
x = df_corr["Predictor"])
y = df_corr["Outcome"])
result = st.spearmanr(x, y)

### Verify
print(result)
print("Rsq =", (result[0]), "P-Value =", (result[1]))

## Regression models with statsmodels
import statsmodels.api as sm # Statistics package best for regression models for statistical tests
from patsy import dmatrices # Describes statistical models and builds design matrices using R-like formulas

### Linear regression
x = df_reg["predcitor"] # features as x
y = df_reg["outcome"] # Save outcome variable as y
mod = sm.OLS(y, X) # Describe linear model
res = mod.fit() # Fit model
print(res.summary()) # Summarize model

### Linear regression: Multiple predictors
features = df_reg.columns.drop(["predictorA", "predictorB"]) # Drop outcome variable and Geographies to isolate all predictor variable names as features
X = df_reg[features] # features as x
y = df_reg["outcome"] # Save outcome variable as y
mod = sm.OLS(y, X) # Describe linear model
res = mod.fit() # Fit model
print(res.summary()) # Summarize model

### Logisitc regression
X = df_reg["predictor"] # features as x
y = df_reg["outcome"] # Save outcome variable as y
mod = sm.Logit(y, X) # Describe logistic model
res = mod.fit() # Fit model
print(res.summary()) # Summarize model

### Logisitc regression: Multiple predictors
features = df_reg.columns.drop(["predictorA", "predictorB"]) # Drop outcome variable and Geographies to isolate all predictor variable names as features
X = df_reg[features] # features as x
y = df_reg["outcome"] # Save outcome variable as y
mod = sm.Logit(y, X) # Describe logistic model
res = mod.fit() # Fit model
print(res.summary()) # Summarize model

### Logisitc Regression: Multiple and multilevel predictors 
y, X = dmatrices('outcome ~ RiskScore', data = df_train, return_type = 'dataframe') # Use patsy to create dmatrices for easy multiple and multilevel modeling
mod = sm.OLS(y, X) # Describe logistic model
res = mod.fit() # Fit model
print(res.summary()) # Summarize model

### Verify
print(res.params) # Print model coefficients
np.exp(res.params) # Print Odd's Ratio from logistic coefficients

#################### Break ####################

# Create Visual Outputs

## Graphing with matplotlib
import matplotlib.pyplot as plt # Comprehensive graphing package in python

### Line graph
plt.plot(df.ColX, df.ColA, color = "b")
plt.ylabel("Y Value")
plt.xlabel("X Value")
plt.legend()
plt.title("Full Plot Title")

### Line graphs: Two lines cver time
plt.figure(figsize = (30, 20))
plt.grid()
plt.plot(fed.Year, fed.D, color = "b")
plt.plot(fed.Year, fed.R, color = "r")
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.ylabel("Vote Difference (Millions)", fontsize = 32)
plt.legend(["D", "R"], fontsize = 32)
plt.title("Votes for House, Senate, and President 1976-2018", fontsize = 48)
plt.savefig("_fig/house_senate_president_plot.jpeg", bbox_inches = "tight")

### Line graphs: Two lines with different Y Axis
fig, ax1 = plt.subplots()
plt.xticks(rotation = 90)
ax1.plot(df.ColX, df.ColA, color = "b")
ax1.set_ylabel("ColA Value")
ax1.set_xlabel("X Value")
plt.legend()
ax2 = ax1.twinx()
ax2.plot(df2.ColX, df2.ColA, color = "r")
ax2.set_ylabel("Df2 ColA Value")
plt.legend()
fig.suptitle("Full Plot Title", y = 0.95, fontsize = 12)

### Line graph: Multiple lines with log scale
plt.figure(figsize = (16, 8))
plt.plot(df_al1k.Day1k, df_al1k.TotalRate, color = "xkcd:neon blue")
plt.plot(df_br1k.Day1k, df_br1k.TotalRate, color = "r")
plt.plot(df_da1k.Day1k, df_da1k.TotalRate, color = "y")
plt.plot(df_hb1k.Day1k, df_hb1k.TotalRate, color = "m")
plt.plot(df_or1k.Day1k, df_or1k.TotalRate, color = "g")
plt.plot(df_pb1k.Day1k, df_pb1k.TotalRate, color = "tab:orange")
plt.plot(df_pn1k.Day1k, df_pn1k.TotalRate, color = "tab:purple")
plt.plot(df_dv1k.Day1k, df_dv1k.TotalRate, color = "tab:blue")
plt.plot(df_al1k.Day1k, df_al1k.OneDay, color = "0.75")
plt.plot(df_al1k.Day1k, df_al1k.TwoDay, color = "0.75")
plt.plot(df_al1k.Day1k, df_al1k.ThreeDay, color = "0.75")
plt.plot(df_al1k.Day1k, df_al1k.SevenDay, color = "0.75")
plt.plot(df_al1k.Day1k, df_al1k.ThirtyDay, color = "0.75")
plt.ylim(1, 350)
plt.ylabel("Cumulative Cases Rate per 100k")
plt.yscale("log")
plt.xlabel("Day Number")
plt.xticks(np.arange(len(df_al1k.Day1k), step = 5), np.arange(len(df_al1k.Day1k), step = 5), rotation = 90)
plt.legend(["Alachua", "Broward", "Dade", "Hillsborough", "Orange", "Palm Beach", "Pinellas", "Duval"])
plt.title("Florida DOH Confirmed COVID-19 Cases by Day")
plt.savefig("_fig/county_total_rate.jpeg")

### Bar graph
plt.bar(df.ColA, color = "b")
plt.ylabel("Col A Value")
plt.xlabel("Label Values")
plt.legend()
plt.title("Full Plot Title")

### Bar graphs: Multiple X
plt.figure()
x = np.arange(len(df_fl.Day))
plt.bar((x), df_fl.Cases, color = 'xkcd:neon green', width = 0.4)
plt.xticks(np.arange(len(df_fl.Day), step = 5), np.arange(len(df_fl.Day), step = 5), rotation = 90)
plt.ylabel("Daily Cases")
plt.xlabel("Day Number")
plt.legend(["Florida"])
plt.title("Florida DOH Confirmed COVID-19 Cases by Day")
plt.savefig("_fig/florida_daily_count.jpeg", bbox_inches = "tight")

### Bar graphs: Side by side
x = np.arange(len(df.ColX))
plt.figure(figsize = (9, 6))
plt.bar((x - 0.2), df.ColA, color = 'b', width = 0.4, label = "ColA Value")
plt.bar((x + 0.2), df.ColB, color = 'r', width = 0.4, label = "ColB Value")
plt.xticks(np.arange(6), df.x, rotation = 90)
plt.legend()
plt.title("Full Plot Title", y = 0.99, fontsize = 16)
plt.savefig("topic_bar_plot.jpeg", bbox_inches = "tight")

## Bar graphs: Side by Side with Multiple X
plt.figure()
plt.bar((1 - 0.2), df_chsq.loc[0, "Expected"], color = 'b', width = 0.4)
plt.bar((1 + 0.2), df_chsq.loc[0, "Observed"], color = 'r', width = 0.4)
plt.bar((2 - 0.2), df_chsq.loc[1, "Expected"], color = 'b', width = 0.4)
plt.bar((2 + 0.2), df_chsq.loc[1, "Observed"], color = 'r', width = 0.4)
plt.bar((3 - 0.2), df_chsq.loc[2, "Expected"], color = 'b', width = 0.4)
plt.bar((3 + 0.2), df_chsq.loc[2, "Observed"], color = 'r', width = 0.4)
plt.bar((4 - 0.2), df_chsq.loc[3, "Expected"], color = 'b', width = 0.4)
plt.bar((4 + 0.2), df_chsq.loc[3, "Observed"], color = 'r', width = 0.4)
plt.bar((5 - 0.2), df_chsq.loc[4, "Expected"], color = 'b', width = 0.4)
plt.bar((5 + 0.2), df_chsq.loc[4, "Observed"], color = 'r', width = 0.4)
plt.bar((6 - 0.2), df_chsq.loc[5, "Expected"], color = 'b', width = 0.4)
plt.bar((6 + 0.2), df_chsq.loc[5, "Observed"], color = 'r', width = 0.4)
plt.bar((7 - 0.2), df_chsq.loc[6, "Expected"], color = 'b', width = 0.4)
plt.bar((7 + 0.2), df_chsq.loc[6, "Observed"], color = 'r', width = 0.4)
plt.xticks((1, 2, 3, 4, 5, 6, 7), df_chsq["Ownership"], rotation = 90)
plt.legend(["Expected", "Observed"])
plt.title("Expected and Observed Counts of VBP Penalties over 1 Percent by Hospital Type 2019")
plt.savefig("_fig/health_penalty_hospital_bar.jpeg", bbox_inches = "tight")

### Boxplot
plt.scatter(df.ColA)
plt.ylabel("Col A Value")
plt.title("Full Plot Title")

## Boxplots: Side by Side with multiple rows
fig, ax = plt.subplots(ncols = 3, nrows = 3, figsize = (7, 20), sharey = True)
ax[0, 0].boxplot(df1.ColA)
ax[0, 0].set_title("Title 1")
ax[0, 0].set_ylabel("df1 ColABC Value")
ax[0, 1].boxplot(df1.ColB)
ax[0, 1].set_title("Title 2")
ax[0, 2].boxplot(df1.ColC)
ax[0, 2].set_title("Title 3")
ax[1, 0].boxplot(df2.ColA)
ax[1, 0].set_ylabel("df2 ColABC Value")
ax[1, 1].boxplot(df2.ColB)
ax[1, 2].boxplot(df2.ColC)
ax[2, 0].boxplot(df3.ColA)
ax[2, 0].set_ylabel("df3 ColABC Value")
ax[2, 1].boxplot(df3.ColB)
ax[2, 2].boxplot(df3.ColC)
fig.suptitle("Full Plot Title", y = 0.92, fontsize = 16)
fig.savefig("topic_box_plot.jpeg", bbox_inches = "tight")

### Scatterplot
plt.scatter(df.ColX, df.ColA, color = "b")
plt.ylabel("Col A and B Value")
plt.xlabel("X Value")
plt.legend()
plt.title("Full Plot Title")

### Scatterplot: Categorical
plt.scatter((df_np["Penalty"]-0.5), df_np["MSPB"], c = "b")
plt.scatter(df_fp["Penalty"], df_fp["MSPB"], c = "red")
plt.xticks((-0.25, 0.75), ("No Penalty over 1%", "Penalty over 1%"))
plt.legend(["Non-Profit", "For-Profit"])
plt.title("MSPB and VBP Penalties over 1 percent by Hospital Type 2019")
plt.savefig("_fig/health_penalty_hospital_scatter.jpeg", bbox_inches = "tight")

### Pie chart
plt.pie([13218, 1546, 3167, (13 + 71 + 49 + 14)], explode = (0.1, 0, 0, 0), labels = ['Black', 'White', 'Hispanic', 'Other'], colors = ["lightskyblue", "lightcoral", "yellowgreen", "gold"], autopct = "%1.1f%%", shadow = True)
plt.legend(labels = ['Black', 'White', 'Hispanic', 'Other'], loc = "best")
plt.axis("equal")
plt.title("Current Prison Population from Cook County")

### ROC Plot
plt.title('Receiver Operating Characteristic')
plt.plot(fpr_f, tpr_f, 'b', label = 'Full, AUC = %0.2f' % full)
plt.plot(fpr_s, tpr_s, 'g', label = 'Select, AUC = %0.2f' % select)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')

### Verify
plt.show() # Show created plots

## Create maps with geopandas
import geopandas as gp # Simple mapping library for csv shape files with pandas like syntax for creating plots using matplotlib 
import matplotlib.pyplot as plt # Comprehensive graphing package in python

### Import Shape Files
gdf_shape = gp.read_file("maps/topic_geo_shape.shp") # Import shape files from folder with all other files downloaded
gdf_state = gp.read_file("C:/Users/drewc/GitHub/data-for-everyone/data_stories/presidential_votes/_raw/tl_2017_us_state/tl_2017_us_state.shp") # US state shape file saved in my-library

### Geopandas datasets
world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))
us = world[world.name == "United States of America"]

### Geojoin with dataframe
gdf_join = pd.merge(gdf_state, df_poly, on = "State", how = "inner") # Geojoins can use pandas merge as long as geo data is first passed in function

### Select only State and Measure
gdf_filter = gdf_join.filter(["State", "geometry"]) # Keep only selected columns

### Drop AK and HI
gdf_drop = gdf_filter[(gdf_filter.State != "AK") & (gdf_filter.State != "HI")]

### Change projection
map45m = map45.to_crs({'init': 'epsg:4326'}) # Mercateur

### Write geo data frame to shape file
gdf_drop.to_file("_data/health_maps_state_stage.shp") # Export pandas data frame to new shape file in _data

### Choropleth 
map = gdf_shape.plot(column = "ColA", cmap = "Blues", figsize = (16, 10), scheme = "equal_interval", k = 9, legend = True)
map.set_axis_off()
map.set_title("Map Title", fontdict = {'fontsize': 20}, loc = "left")
map.get_legend().set_bbox_to_anchor((.6, .4))
plt.savefig("maps/topic_map__fig.jpeg", dpi = 1000)

### Chloropleth: Multiple Plots
fig, (ax1, ax2) = plt.subplots(ncols = 2)
gdf_join.plot(column = "NP", ax = ax1, categorical = True, legend = False).set_axis_off() 
ax1.set_title("Restricted Scope")
gdf_join.plot(column = "MSPB", cmap = "Blues", ax = ax2, legend = False).set_axis_off()
ax2.set_title("Mean MSPB")
fig.suptitle("Nurse Practicioner Scope and MSPB in 2018")
fig.savefig("_fig/health_np_stae_map.jpeg", bbox_inches = "tight")

## Create maps with folium
import folium # Mapping library with dynamic 
import json # library for importing and manipuation json files

## Import Json Shape File
map_json = json.load(open("crime/crime_neighborhoods.geojson")) # Save as object
folium.GeoJson(js.load(open("topic_shape.geojson")), name = "shape") # Name map in function

### Get Open Source Map
map_fl = folium.Map(location = [29.6516, -82.3248], tiles = 'OpenStreetMap', zoom_start = 11) # Florida Open Street map
map_stamen = folium.Map(location = [29.6516, -82.3248], tiles = 'Stamen Toner', zoom_start = 11) # Florida black and white street maps
map_terrain = folium.Map(location = [29.6516, -82.3248], tiles = 'Stamen Terrain', zoom_start = 11) # Florida terrain maps

## Get OpenSource Map of Different Places
map_chi = folium.Map(location = [41.644668, -87.540093], zoom_start = 11) # Chicago, IL
map_pdx = folium.Map(location = [45.5244, -122.6699], zoom_start = 13) # Portland, OR

## Add shape to open map
map_shape = folium.features.GeoJson(df_json).add_to(map) # Isolate features from geographic json file and save as data frame

### Add shape to open map: choropleth map
map_chor = choropleth(geo_data = js, data = df, columns = ["GeoID", "ColA"], threshold_scale = [100, 200], key_on = "feature.geoid", fill_color = "Blues", fill_opacity = 0.7, legend_name = "ColA Values").add_to(map) # Folium choropleth map

### Add shape to open map: heat map
from folium.plugins import HeatMap # Tool for creating heatmaps in folium
heat = [[row["Lat"], row["Lon"]] for index, row in df.iterrows()] # For loop to create heat marking
map_heat = HeatMap(heat).add_to(map) # Create Heatmap from heat marking with folium function 

### Add markers to open map: icon
folium.Marker(location = [45.5244, -122.6699], popup = value, color = "blue").add_to(map) # For loop for creation of markers

### Add markers to open map: circle
folium.Circle(radius = 100, location=[45.5244, -122.6699], popup = 'The Waterfront', color = 'crimson', fill = False).add_to(map) # Folium circle marker

### Add markers to open map: clickable
folium.Marker([45.3288, -121.6625], popup='<i>Mt. Hood Meadows</i>', tooltip = 'Click me!').add_to(map) # Folium icon markers with click option

### Add markers to open map: url links
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
vis1 = json.loads(requests.get(f'{url}/vis1.json').text)
vis2 = json.loads(requests.get(f'{url}/vis2.json').text)
vis3 = json.loads(requests.get(f'{url}/vis3.json').text)
folium.Marker(location = [47.3489, -124.708], popup = folium.Popup(max_width=450).add_child(folium.Vega(vis1, width=450, height=250))).add_to(map)

### Add markers to open map: data frame column values
for lat, lon, value in zip(df_["Lat"], df_["Lon"], df_["Value"]):
     fol.Marker(location = [lat, lon], popup = value, color = "blue").add_to(map) # For loop for creation of markers

### Verify
map # Automatically show map in jupyter notebooks

### Write to HTML
map.save("_fig/crime_chi_map.html") # Save map as html file