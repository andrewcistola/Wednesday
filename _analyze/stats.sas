
* Florida Blue Interview Project
** Andrew S. Cistola, MPH
*** Set Library to Local Folders;
libname DAT "C:\Users\drewc\Dropbox (UFL)\flblue\_data"; * General data folder in repository name;
run;

*** Import CSV from Local Folder;
proc import datafile = "C:\Users\drewc\Dropbox (UFL)\flblue\_data\analytical_file.csv" out = DAT.af dbms = csv replace;
guessingrows = 10000; * Use for sparse data to make sure that SAS reads enouigh rows to find numeric observations, this will take a while;
run;

*** Show first 5 observations of Dataset;
proc print data = DAT.af (OBS = 5);
run;

** Exploratory Data Analysis;

*** Summary statistics of variables;
proc summary data = DAT.af 
n mean stddev min max p25 median p75 print;
class AGE_ACA;
var HP_Paid IP_Visits;
run;

*** One Way ANOVA;
proc glm data = DAT.af
order = INTERNAL;
class AGE_ACA;
model IP_Visits = HP_Paid;
run;

*** Subset Data by variable;
DATA DAT.Marketplace;
   SET DAT.af;
   IF AGE_ACA = "Marketplace";
RUN;

*** Linear Regression Model;
proc glm data = DAT.marketplace; * Used for pearson, plots = show all diagnostic plots;
class ; *categorical explanatory variables with anoptional reference group, ;
model HP_Paid =  AGE Comorbidity PCP_Copay IP_Visits; * model statement is y = x or quant (response) = qual (explanatory) / show solution and parameter estimates;
run;
quit; * This statment will not stop running until quit statement; 

*** Frequency Distribution for one categorical variable;
PROC FREQ DATA = DAT.marketplace; 
TABLES AGE_ACA;
RUN;  

*** Histogram of variable;
PROC SGPLOT DATA = DAT.marketplace; 
HISTOGRAM HP_Paid;
RUN;

*** QQ Plot of variable;
PROC UNIVARIATE DATA = DAT.marketplac; 
VAR HP_Paid;
QQPLOT / NORMAL(MU=EST SIGMA=EST); 
RUN;

*** Scatter plots;
proc sgplot data = DAT.marketplace; 
loess X = IP_Visits Y = HP_Paid / smooth = 0.6 markerattrs = (symbol = squarefilled size = 4PX)
group = AGE_ACA;
run;

*** Subset Data by variable;
DATA DAT.Medicare;
   SET DAT.af;
   IF AGE_ACA = "Medicare";
RUN;

*** Linear Regression Model;
proc glm data = DAT.Medicare; * Used for pearson, plots = show all diagnostic plots;
class ; *categorical explanatory variables with anoptional reference group, ;
model HP_Paid =  AGE Comorbidity ER_Copay IP_Visits; * model statement is y = x or quant (response) = qual (explanatory) / show solution and parameter estimates;
run;
quit; * This statment will not stop running until quit statement; 

*** Frequency Distribution for one categorical variable;
PROC FREQ DATA = DAT.medicare; 
TABLES AGE_ACA;
RUN;  

*** Histogram of variable;
PROC SGPLOT DATA = DAT.medicare; 
HISTOGRAM HP_Paid;
RUN;

*** QQ Plot of variable;
PROC UNIVARIATE DATA = DAT.medicare; 
VAR HP_Paid;
QQPLOT / NORMAL(MU=EST SIGMA=EST); 
RUN;

*** Scatter plots;
proc sgplot data = DAT.medicare; 
loess X = IP_Visits Y = HP_Paid / smooth = 0.6 markerattrs = (symbol = squarefilled size = 4PX)
group = AGE_ACA;
run;

* The End;
