#### My Data Portfolio: An Open Repository for Showing Professional Data Science Skills
### My Data Toolbox: Language and Program Specific Generic Scripts for Building Projects
## The R Project for Statistical Computing - Code Script by DrewC!

#### Section A: Import Libraries and Datasets and Prepare Data

### Import Libraries and Data

## Open R Terminal
R # open R in VS Code (any terminal)
library(skimr) # Library used for easy summary of data

## Import Hadley Wickham Libraries
library(ggplot2) # ggplot2 is a system for declaratively creating graphics, based on The Grammar of Graphics. You provide the data, tell ggplot2 how to map variables to aesthetics, what graphical primitives to use, and it takes care of the details.
library(dplyr) # dplyr provides a grammar of data manipulation, providing a consistent set of verbs that solve the most common data manipulation challenges.
library(tidyr) # tidyr provides a set of functions that help you get to tidy data. Tidy data is data with a consistent form: in brief, every variable goes in a column, and every column is a variable.
library(readr) # readr provides a fast and friendly way to read rectangular data (like csv, tsv, and fwf). It is designed to flexibly parse many types of data found in the wild, while still cleanly failing when data unexpectedly changes.
library(purrr) # purrr enhances R’s functional programming (FP) toolkit by providing a complete and consistent set of tools for working with functions and vectors. Once you master the basic concepts, purrr allows you to replace many for loops with code that is easier to write and more expressive.
library(tibble) # tibble is a modern re-imagining of the data frame, keeping what time has proven to be effective, and throwing out what it has not. Tibbles are data.frames that are lazy and surly: they do less and complain more forcing you to confront problems earlier, typically leading to cleaner, more expressive code.
library(stringr) # stringr provides a cohesive set of functions designed to make working with strings as easy as possible. It is built on top of stringi, which uses the ICU C library to provide fast, correct implementations of common string manipulations.
library(forcats) # forcats provides a suite of useful tools that solve common problems with factors. R uses factors to handle categorical variables, variables that have a fixed and known set of possible values.
library(tidyverse) # All of the libraries above in one line of code
library(skimr) # Library used for easy summary of data


## Import Machine Learning Libraries
library(randomForest) # Popular random forest package for R
library(randomForestExplainer) # Complimentary to randfomForest package with tools for analysis

## Import Statistics Libraries
library(psych) # Survey analysis library with factor analysis
library(MASS) # Stepwise inclusion model with linear and logistic options
library(pROC) # ROC tests with AUC output
library(ineq) # Gini coefficient and Lorenz curve

## Import Graphical Output Libraries
library(igraph) # Library used for social network analysis
library(ggmap) # Common tool for using GIS data with tidyverse
library(tigris) # Mapping library with geo boundaries preloaded
library(leaflet) # Mapping library that uses intervative features
library(mapview) # Mapping library

## PHC6194 and allocativ
library(RSQLite) # SQLite databases in R
library(RPostgreSQL) # Postgre SQL databases in R
library(rpostgis) # PostGIS with Postgres in R
library(sp) # S4 classes for spatial data in R
library(lme4) # Linear mixed effect modeling in R
library(arm) # Visualizations of linear mixed effect modeling using 'lme4' in R
library(reshape2) # Long/wide conversions from Hadley Wickham
library(plyr) # Data manipulation from Hadley Wickham 
library(ggplot2) # General use plotting library from Hadley Wickham
library(ggmap) # General use mapping library with ggplot API
library(RColorBrewer) # Creates nice looking color palettes especially for thematic maps in R
library(rgdal)
library(rgeos) 
library(maptools) 
library(ggsn)
library(spdep)  
library(DCluster)  
library(gstat) 
library(tigris)  
library(raster)  
library(dismo)  
library(rgeos)
library(sqldf)
library(smacpod)
library(rsatscan)
library(spatstat)
library(randomForest) # Popular random forest package for R
library(randomForestExplainer) # Complimentary to randfomForest package with tools for analysis


## Import Data
setwd("C:/Users/drewc/GitHub/Portfolio") # Set wd to project repository
df_ = read.csv("_data/topic_sub_type.csv") # Import dataset from _data folder
skim(df_) # Descritive statistics, dimensions, and missing values
df_arst = data.frame(USArrests) # Save object as data frame
gdf_XY = readOGR(dsn = '_shape/CENSUS_TIGER_2018_ZCTA', layer = 'cb_2018_us_zcta510_500k') # Import shape file with rgdal package

### Step 2: Prepare Data for Classificaiton

## Resolve missing data
df_ = subset(df_, select = -c(ColA, ColB)) # Remove variables with high missing values
df_ = na.omit(df_yrbs) # Omit rows with NA from Data Frame
XY$SMR[is.na(XY$SMR)] <- 0 # Convert all to NA
sum(is.na(sdf_XY@data$ST)) # Count of NA byu column

## Tidy data types and objects
df_ = df_ %>% mutate_if(is.character, as.numeric) # Change character to numeric values

## Subset data frames for outcomes
df_ = df_[which(df_$ColA == "String" & df_$ColB == TRUE | df_$ColC == 1), ] # Subset for numeric outcome of interest with operators
df_ = subset(df, ColA == 1, select = weight:income) # Subset by coluimn value and take all columns between selected
df_ = select(df_, -c(ColB, ColC, ColD)) # Remove variables similar to the outcome

## Verify Data
glimpse(df_) # Rows, columns, variable types and 10 
summary(df_) # Descriptive statistics on each varibale
skim(df_) # Descritive statistics, dimensions, and missing values
head(df_) # Print mini table with first 6 observations 
tail(df_) # Mini table with last 5 observations
class(df_) # Type of object
dim(df_) # Dimensions of data frame
ncol(df_) # Number of columns
nrow(df_) # Number of rows
str(dat) # Show structure of dataframe

### Section B: Data Manipulation Quick Scripts

## Data Manipulation in Base R 
df_purity_top <- df_[1:10, ] # Save first 10 observations of data frame
df_ = df_[which(df_$ColA == "1" & df_$ColB > 2), ] # based on variable values
df_$ColC[ColA == 1 | ColB == 2] <- 1 ) # Create new column based on conditions
df_qual = subset(df_qual, select = -c(char_qual)) # Remove variables with high missing values
df_arst$UrbanPopG = cut(df_arst$UrbanPop, breaks = quantile(df_arst$UrbanPop, probs = c(0,0.25,0.5,0.75,1)), include.lowest = T) # Create column of quantiles based on column
df_Y = df_meps[c('IPDIS19', 'IPNGT19')] # Select columns of dataframe
df_X = df_meps[, grepl('DX', names(df_meps))] #Select columns from data frame by string value of column name
df_X = na.omit(df_X) # Remove all rows with missing values
names(mtcars)[names(mtcars)=="wt"] <- "weight" # Rename column in base R
gdf_XY@data$ZCTA = as.character(gdf_XY@data$GEOID10) # Convert numeric to character
gdf_XY@data$ZCTA = paste('ZCTA', gdf_XY@data$ZCTA, sep = '') # Add character string to each value in column
df_ = df_[which(df_$ColA == "String" & df_$ColB == TRUE | df_$ColC == 1), ] # Subset for numeric outcome of interest with operators
df_ = subset(df, ColA == 1, select = weight:income) # Subset by coluimn value and take all columns between selected
df_ = select(df_, -c(ColB, ColC, ColD)) # Remove variables similar to the outcome
data = merge(Y, X, by = 0) # Merge by index
us@data = us@data[us@data$GEOID != c('02', '15', '60', '66', '69', '72', '78'), ] # Select by conditions (vector)
USelect2004@data$electid <- rownames(USelect2004@data) # Save index as column to create row of ascending values

df_ = aggregate(df_W2$population, by = list(Species = df_W2$FIPS), FUN = sum) # Group by and sum in base R
FIPS = column_to_rownames(df_Y2, var = 'FIPS')


## Data Manipulation in tidyverse
df = df %>% mutate_if(is.character, as.numeric) ## Change Characters to Numeric
group = df %>% group_by(ColA, ColB) %>% summarise(sum(ColC)) ## Group data By Columns and Sum
groups = temp %>% group_by(ColA) %>% summarise(mean(ColB)) ## Group By Columns and Average
df = as.data.frame(tib) ## Convert tiblle to Data Frame
join = inner_join(df1, df2, by = "ColA") ## Join By Columns
invert = rownames_to_column(df) ## Invert Rows and Columns
subs = filter(df, ColA == "5") ## Subset by Column Values
str = oecd %>% filter(str_detect(Subject, "Gini")) ## Susbet by column string value
drp = select(wide, c("Country", "2011", "2012", "2013", "2014", "2015")) ## Keep Certain Columns

## Add new column based on conditions
df_yrbs$outcome <- 0 # Add new outcome column and set value to 0
df_yrbs$outcome[df_yrbs$qn26 == 1 | df_yrbs$qn27 == 1] <- 1 # Create new column based on conditions
df_plan = subset(df_yrbs, select = -c(qn26, qn27)) # Remove outcome and variables similar to the outcome
colnames(df)[1] <- "ColA" ## Change Column Names
colnames(df) <- c("ColA", "ColB", "ColC") ## Change Column Names

## Create Column of Averages
years = c("2011", "2012", "2013", "2014", "2015") 
matdrp = select(drp, years) # Create matrix for rowMeans function
mat = data.matrix(matdrp)
avgcol = mutate(drp, avg = rowMeans(mat, na.rm = TRUE))
avgcol

## Quick R
names(mtcars)[names(mtcars)=="wt"] <- "weight" #rename just the "wt" column in mtcars
mydata$agecat[age > 45 & age <= 75] <- "Middle Aged"
myvars <- c("v1", "v2", "v3") # Rename variables in data frame
newdata <- mydata[myvars] # select variables v1, v2, v3
myvars <- paste("v", 1:3, sep="") # Paste string in varaibles name
newdata <- mydata[myvars] # 
newdata <- mydata[c(1,5:10)] # select 1st and 5th thru 10th variables
myvars <- names(mydata) %in% c("v1", "v2", "v3") # exclude variables v1, v2, v3
newdata <- mydata[!myvars] 
newdata <- mydata[c(-3,-5)] # exclude 3rd and 5th variable
mydata$v3 <- mydata$v5 <- NULL # delete variables v3 and v5
newdata <- subset(mydata, age >= 20 | age < 10, select=c(ID, Weight)) # using subset function
mysample <- mydata[sample(1:nrow(mydata), 50, replace=FALSE),] # sample without replacement
newdata <- subset(mydata, sex=="m" & age > 25, select=weight:income) # Subset by coluimn value and take certain columns
newdata <- mydata[1:5,] # first 5 observations
newdata <- mydata[ which(mydata$gender=='F'& mydata$age > 65), ] # based on variable values
newdata <- mydata[ which(gender=='F' & age > 65),] # based on variable values
newdata <- mtcars[order(mpg),] # sort by mpg
newdata <- mtcars[order(mpg, cyl),] # sort by mpg and cyl
newdata <- mtcars[order(mpg, -cyl),] #sort by mpg (ascending) and cyl (descending)
total <- merge(data frameA,data frameB,by="ID") # merge two data frames by ID
total <- merge(data frameA,data frameB,by=c("ID","Country")) # merge two data frames by ID and Country
total <- rbind(data frameA, data frameB) # join two data frames (datasets) vertically, data frames must have the same variables, but they do not have to be in the same order

#### Section M: Conduct Machine Learning to Identify Important Features 

## Create a Training and Validation Sample

## Split into 50-50 sample
sample = sample.int(n = nrow(df_), size = floor(.50*nrow(df_)), replace = F)
train = df_[sample, ]
test = df_[-sample, ]

### Use Random Forests to Identify Main Variables of Interest

## Create a Random Forest
forest = randomForest(formula = outcome ~ feature1 + feature2., data = df_, ntree = 1000, importance = TRUE)

## Tidy Results for Variable Classification
forest = round(importance(forest), 2)
df_forest = as.data.frame(forest)
df_forest = rownames_to_column(df_forest)
colnames(df_forest) <- c("Variable", "Importance", "Purity") # Change column names to easily readible

## Create Importance Variable Lists
df_importance = select(df_rf, -Purity) # Remove variables similar to the outcome
df_importance = arrange(df_importance, desc(Importance)) # Descend by variable in data frame
df_importance = df_importance[1:10, ] # Save first 10 observations of data frame
row.names(df_importance) = df_importance$Variable # Convert Column to row names
df_importance = select(df_importance, -Variable) # Remove variable from data frame

## Create Purity Variable List
df_purity = select(df_rf, -Importance) # Remove variables similar to the outcome
df_purity = arrange(df_purity, desc(Purity)) # Descend by variable in data frame
df_purity = df_purity[1:10, ] # Save first 10 observations of data frame
row.names(df_purity) = df_purity$Variable # Convert column to row names
df_purity = select(df_purity, -Variable) # Remove variable from data frame

## Write Random Forest Output to File
result1 = print(df_importance)
result2 = print(df_purity)
file = file("rf_results.txt")
open(file, "w")
write.table(result1, file, quote = FALSE, sep = "   ")
write(" ", file)
write.table(result2, file, quote = FALSE, sep = "   ")
close(file)

Y = sdf_WXYZ@data['crude']
X = sdf_WXYZ@data[names(subset(df_X, select = -c(ZCTA)))]
F = as.formula(paste(names(Y), ' ~ ', paste(names(X), collapse = ' + '), sep = ''))
for(i in 1:ncol(X)) {
  X[ , i][is.na(X[ , i])] <- median(X[ , i], na.rm = TRUE)
} # Replace missing values with column medians



Y = 'crude'
X = subset(df_X, select = -c(ZCTA))
F = as.formula(paste(Y, ' ~ ', paste(names(X), collapse = ' + '), sep = ''))
forest = randomForest(formula = F, data = sdf_WXYZ@data, ntree = 1000, importance = TRUE)

### Conduct Factor Analysis to Identify Latent Variables

## Subset by group with outcome
df_ = filter(df_, outcome == "1") # Subset for outcome of interest
df_ = select(df_, -outcome) # Remove outcome variable
nrow(df_) # Check number of rows

## Create covariance matrix
mat_fa = as.matrix(df_)
mat_cov = cov(mat_fa)
mat_cov = na.omit(mat_cov)
nrow(mat_cov)

## Perform Scree test
fig_scree = VSS.scree(mat_cov)

## Write Random Forest Output to File
result1 = fig_scree
file = file("fa_results.txt")
open(file, "a")
write(" ", file)
write(result1, file, quote = FALSE)
close(file)



### Section S: Conduct Statisitical Analysis on Data

##

## Hypothesis Tests with Single Independent and Dependent Variables
model_tt = t.test(df$ColA, df$ColB, paired = TRUE) # Paired T-Test for C->C parametric
model_pearson = cor(df$ColA, df$ColX) # Pearson's Rank for Q->Q

## Multiple Regression Models
model_linear = lm(Y~ a + b + c, data = df_) # Create multiple linear regression model
model_logistic = glm(Y~ a + b + c, data = df_) # Create multiple linear regression model

## Model Selection
model_back = stepAIC(model_, direction = "backward") # Stepwise backwards selection on model
model_forw = stepAIC(model_, direction = "forward") # Stepwise forwards selection on model

## Manipulate Output
df_coef = data.frame(summary(model_$coefficients)
print(df_coef)

## Verify Output
summary(model_)

#### Section G: Create Vissual Displays from Data

### Create Simple charts and plots

## Create bar chart in ggplot
p<-ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity")
p

## Create Line Plot of continuous variables
plot(df$ColX, df$ColA, type = "l", col  = "blue", main = "Plot Title", xlab = "X Value", ylab = "Y value", xlim = c(0, 100), ylim = c(0, 100))

## Create Line Plot with Different Y on Same Plot
plot(df1$ColX, df1$ColA, type = "l", col  = "blue", main = "Plot Title", xlab = "X Value", ylab = "Y value", xlim = c(0, 100), ylim = c(0, 100))
par(new = True)
plot(df2$ColX, df2$ColA, type = "l", col  = "red", xlab = "X Value", ylab = "Y value", xlim = c(0, 100), ylim = c(0, 100))

## Create a scatterplot and overlay with linear regression line
fit = lm(df$ColX ~ df$ColA)
plot(x = df$ColX, y = df$ColA, xlab = "X Value", ylab = "Y Value")
abline(fit, col = "red")

#### Conduct Social Network Analysis

## Create Network plot
matrix <- as.matrix(df) 
g = graph.adjacency(matrix, mode = "undirected", weighted = NULL)
plot(g, rescale = FALSE, vertex.label.cex = 0.5, edge.width = 0.5, mark.col = "blue")
tkplot(g, canvas.width=800, canvas.height=800, vertex.color = "SkyBlue2")

### Create GIS Maps

## Get Miami map
mia = get_map("Miami", zoom = 12, maptype = "roadmap")

## Get FL Census Tract Map
fl = tracts(state = "FL")

## Join Dataframe with Geo Data
geodf = geo_join(geo, df, "GEOID", "GEOID")

## Create Cholorpleth Map
map = leaflet() %>% 
  addPolygons(data = geodf, fillColor = ~pal1(geodf$ColA), fillOpacity = 0.7, weight = 0.2, smoothFactor = 0.2) %>%
  addLegend(pal = colorNumeric("Greens", domain = c(0, 120)), values = geodf$ColA, position = "bottomright", title = "Map Title")
mapshot(map, file = "_fig/topic_map_fig.jpeg")

## Create Heatmap
ggmap(mia) +
  stat_density2d(data = dfgeo, aes(x = lon, y = lat, fill = ..density..), geom = "tile", contour = F, alpha = 0.5) +
  scale_fill_viridis(option = "inferno") +
  labs(title = "Map Title", subtitle = "Subtitle")










### Appendix 2: Writing User Definied Funtions in Base R

## Function in Base R
myfunction <- function(arg1, arg2, ... ){
statements
return(object)
}

## Operators in Base R
if-else
if (cond) expr
if (cond) expr1 else expr2
for
for (var in seq) expr
while
while (cond) expr
switch
switch(expr, ...)
ifelse
ifelse(test,yes,no)


setwd("C:/Users/drewc/GitHub")

df = read.csv("Portfolio/Toolbox/_data/topic_sub_type.csv")
head(df)


#### Change Characters to Numeric

df = df %>% mutate_if(is.character, as.numeric)

#### Group data By Columns and Sum

group = df %>%
  group_by(ColA, ColB) %>%
  summarise(sum(ColC))

#### Group By Columns and Average

groups = temp %>%
  group_by(ColA) %>% summarise(mean(ColB))

#### Convert tiblle to Data Frame

df = as.data.frame(tib) 

#### Change Column Names

colnames(df)[1] <- "ColA"
colnames(df) <- c("ColA", "ColB", "ColC")

#### Join By Columns

join = inner_join(df1, df2, by = "ColA")

#### Invert Rows and Columns

invert = rownames_to_column(df)

#### Subset by Column Values

subs = filter(df, ColA == "5")

#### Susbet by column string value

str = oecd %>% filter(str_detect(Subject, "Gini"))
head(str)

#### Keep Certain Columns

drp = select(wide, c("Country", "2011", "2012", "2013", "2014", "2015"))
head(drp)

#### Create Column of Averages

years = c("2011", "2012", "2013", "2014", "2015") 
matdrp = select(drp, years) # Create matrix for rowMeans function
mat = data.matrix(matdrp)
avgcol = mutate(drp, avg = rowMeans(mat, na.rm = TRUE))
avgcol



The Reshape Package

Hadley Wickham has created a comprehensive package called reshape to massage data. Both an introduction and article are available. There is even a video!

Basically, you "melt" data so that each row is a unique id-variable combination. Then you "cast" the melted data into any shape you would like. Here is a very simple example.

mydata
id 	time 	x1 	x2
1 	1 	5 	6
1 	2 	3 	5
2 	1 	6 	1
2 	2 	2 	4

 

# example of melt function

mdata <- melt(mydata, id=c("id","time"))

newdata
id 	time 	variable 	value
1 	1 	x1 	5
1 	2 	x1 	3
2 	1 	x1 	6
2 	2 	x1 	2
1 	1 	x2 	6
1 	2 	x2 	5
2 	1 	x2 	1
2 	2 	x2 	4

# cast the melted data
# cast(data, formula, function)
subjmeans <- cast(mdata, id~variable, mean)
timemeans <- cast(mdata, time~variable, mean) 


print("THE END")
#### End Script

# PHC 6194 Content

## Scri[pt title
title = 'UF PHC6194 SPR2021' # Input basic title
descriptive = '- Assignment 2 and 3' # Input descriptive title
author = 'Andrew S. Cistola, MPH' # Input author information
GH = 'https://github.com/andrewcistola/PHC6194' # Input GitHub repository
name = 'PHC6194_CLASS_A02_v1-1' # Input generic file name with repo, project, subject, and version
project = 'CLASS/' # Input project file name inside repository
repo = 'PHC6194/' # Input repository filename
user = 'Andrew S. Cistola, MPH; https://github.com/andrewcistola' # Input name and GitHub profile of user
local = '/home/drewc/GitHub/' # Input local path to repository
directory = paste(local, repo, project, sep = "") # Set wd to project repository using variables
day = Sys.Date() # Save dimple date as string
stamp = date() # Save Date and timestamp


setwd(paste(directory, 'WK5/', sep = "")) # Set wd to project repository


## Libraries
library(RPostgreSQL) # Library for using postgre SQL databases in R
library(RPostgreSQL) # Library for using postgre SQL databases in R
library(ggmap) # General use mapping library with ggplot API
install.packages("rpostgis")
library(rpostgis) # Library used in PHC6194
install.packages("sp")
library(sp) # Library used in PHC6194
# sudo apt install libgdal-dev
install.packages("rgdal")
library(rgdal) # Library used in PHC6194
# sudo apt install libgeos-dev
library(ggplot2) # General use plotting library from Hadley Wickham
install.packages("rgeos")
library(rgeos) # Library used in PHC6194
install.packages("maptools")
library(maptools) # Library used in PHC6194
# sudo apt install libudunits2-dev
install.packages("ggsn")
library(ggsn) # Library used in PHC6194
library(plyr) # dplyr provides a grammar of data manipulation, providing a consistent set of verbs that solve the most common data manipulation challenges.

## Manipulation
dat = subset(dat, select = -c(id)) # Remove rownames from datafrmae




## SQL
con_1 = dbConnect(dbDriver("PostgreSQL"), dbname = "phc6194db", host = "localhost", user = "phc6194", password = "vmuser") # create a connection to the postgres database
dbWriteTable(con_1, 'wk5', wk5.dat, row.names = FALSE, append = TRUE) # Export R dataframe to SQL database
dbReadTable(con_1, 'wk5.dat') # Dispaly PostgreSQL table
dbGetQuery(con_1, 'SELECT * FROM wk5 LIMIT 6') # Select first 6 lines from table with PostgreSQL query
dbGetQuery(con_1, "DROP TABLE wk5.dat;") # Delete table in database with PostgreSQL query

# OLS Models
m_ = lmer(quant ~ (1|ID), data = df_XY) # empty model analysis with varying intercept for each individual
m_ = lmer(quant ~ x1 + x2 + (1|ID), data = df_XY) # varying intercept with individual-level predictor

# GLM Models
m_ = glmer(cat ~ X + factor(X_cat) + (1|ID), family = binomial(link = "logit"), data = df_XY) # Logistic regression
m_ = glmer(count ~ X + (1|id), family = poisson(link = "log"), data = df_XY) # Poisson regression

# Mixed Effects
fixef(m_) # Assume fixed-effects
ranef(m_) # Assume random-effects

# Outputs
display(m_) # Summary
coef(m_)[1]) # Coefficients
se.fixef(m_) # Standard errors
exp(fixef(m_)[2]) # Odd's Ratios
exp(fixef(m_)[2] + c(-1.96,1.96) * se.fixef(m_)[2]) # 95% CIs


# Statistical Tests in Base R

ttpair = t.test(df$ColA, df$ColB, paired = TRUE) # Paired T-Test
spearman = cor(df$ColA, df$ColXcor, method = 'spearman') # Pearson's correlation

# Regression with Base R

## Multiple Regression Models
model_linear = lm(Y~ a + b + c, data = df_) # Create multiple linear regression model
model_logistic = glm(Y~ a + b + c, data = df_) # Create multiple linear regression model

## Model Selection
model_back = stepAIC(model_, direction = "backward") # Stepwise backwards selection on model
model_forw = stepAIC(model_, direction = "forward") # Stepwise forwards selection on model

## Output
summary(model_) # Model summary
df_ = data.frame(summary(model_$coefficients) # Data frame of coefficients

# Mixed-Effects Regression with 'lmer' library

## Create Models
model_mix = lmer(quant ~ (1|ID), data = df_XY) # empty model analysis with varying intercept for each individual
model_mix = lmer(quant ~ x1 + x2 + (1|ID), data = df_XY) # varying intercept with individual-level predictor
model_mix_log = glmer(cat ~ X + factor(X_cat) + (1|ID), family = binomial(link = "logit"), data = df_XY) # Logistic regression
model_mix_poi = glmer(count ~ X + (1|id), family = poisson(link = "log"), data = df_XY) # Poisson regression

## Apply Effects
fixef(model_mix) # Assume fixed-effects
ranef(model_mix) # Assume random-effects

## Output ParametersS
display(model_mix) # Summary
coef(model_mix)[1]) # Coefficients
se.fixef(model_mix) # Standard errors
exp(fixef(model_mix)[2]) # Odd's Ratios
exp(fixef(model_mix)[2] + c(-1.96,1.96) * se.fixef(model_mix)[2]) # 95% CIs

### Create Map in '_fig' folder with User Defined Variables and base R plot()
sdf = sdf_WXYZ # SpatialPolygonDataFrame object
state = 'FL' # State abbreviation for map focus
col_state = sdf_WXYZ@data$ST # Column where state lables are located
rate = 'crude' # Column label for outcome of interest
col_rate = sdf_WXYZ@data$crude # Column in SpatialPolygonDataFrame where outcome is located
scale = c(0, 0.2, 0.4, 0.6, 0.8, 1) # Percentile breaks
breaks = quantile(col_rate, probs = scale, na.rm = TRUE, type = 8, names = FALSE) # Calculate color scale based on percentile breaks
color = 'Greens' # Color scheme
n_color = length(breaks) # Number of color breaks calculated by length of breaks from variable above
library(sp) # S4 classes for spatial data in R
library(RColorBrewer) # Creates nice looking color palettes especially for thematic maps in R
sub = subset(sdf, col_state == state) # Subset spatial data frame by variable above
map = spplot(sub, rate, at = breaks, edge.col = FALSE, col.regions = brewer.pal(n_color, color)) # Create chloropleth by variables above
png(paste('_fig/', state, '_', rate, '_', 'map.png', sep = '')) # Open png file to write plot
plot(map) # Plot chloropleth map object defined above
dev.off() # Close file


us@proj4string <- CRS("+init=epsg:4326") # Change SRID to 4326
us@proj4string # Check SRID
us@data = us@data[us@data$GEOID != c('02', '15', '60', '66', '69', '72', '78'), ] # Subset based on vector
us = as(us, 'Spatial') # Convert sp to sf object (spatial data frame)
us = over(centroidelect, us) # Overlay centroids of small geography (arg1) onto larger polygons (arg2). This will create a new dataframe with columns of agr2 with rows of arg1

low = 'blue3' # Standard map colorscheme
mid = 'lightyellow' # Standard map colorscheme
high = 'red3' # Standard map colorscheme
na = 'white' # Standard map colorscheme
breaks = 9 # Standard map colorscheme
scheme = 'trad'

low = 'dodgerblue3' # Standard map colorscheme
mid = 'seashell' # Standard map colorscheme
high = 'tomato3' # Standard map colorscheme
na = 'white' # Standard map colorscheme
breaks = 9 # Standard map colorscheme
scheme = 'soft'

low = 'turquoise3' # Standard map colorscheme
mid = 'ivory' # Standard map colorscheme
high = 'deeppink3' # Standard map colorscheme
na = 'white' # Standard map colorscheme
breaks = 9 # Standard map colorscheme
scheme = 'bright'

low = 'chartreuse3' # Standard map colorscheme
mid = 'azure' # Standard map colorscheme
high = 'magenta3' # Standard map colorscheme
na = 'white' # Standard map colorscheme
breaks = 9 # Standard map colorscheme
scheme = 'alternate'