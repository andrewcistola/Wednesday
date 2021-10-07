**SAS Code Portfolio;

**Prep Code: Set Libraries;

libname TL "C:\Users\drewc\GitHub\Portfolio\Toolbox\SAS_Toolbox";
libname DT "C:\Users\drewc\GitHub\Portfolio\Toolbox";
run;

*Sort Variables;

proc sort 
data = TL.Df1;
by ColA; 
run;

*Show Varables in Dataset alphabetically;

proc datasets; 
contents data = ifthen;
run;

*Show first 5 observations of Dataset;

proc print data = PD.ifthen (OBS = 5);
var SEQN DMStat;
run;

*Summary Statistics for Variables;

proc summary data = PD.ifthen Print;
var DMStat;
run;

*Export SAS Dataset to CSV;

proc export data = PD.result dbms = csv
outfile = "E:PreDM\_data\nhanes_dmstatus_raw.csv"
replace;
run;

*Megre Data by Variable;

data SAS.Merge;
merge SAS.Df1 SAS.Df2; 
by ColA;
run;

*Check contents of Dataset;

proc contents data = SAS.Merge;
run;

*Use Coniditons to Create New Variabe;

data SAS.ifthen;
set SAS.merge;
If ColA = 1 then ColB = 1; *1 = Category Format;
Else If ColA = . then ColB = 7; *2 Missing;
run;

*Get frequency of Unique Values in tables;

proc freq data = PD.ifthen2;
tables DMStat DMRisk;
run;

*Set formats;

proc format;                                                                                       
value Status	
	1 = Diagnosed Diabetes                          
	2 = Diagnosed Prediabetes                      
    3 = Undiagnosed Diabetes
	4 = Undiagnosed Prediabetes
	5 = Misdiagnosed
	6 = Healthy
	7 = Unknown;
value Risk 	 	
	1 = At risk
	2 = Not at risk;
value Race
	1 = Mexican American
	2 = Other Hispanic
	3 = NonHispanic White
	4 = NonHispanic Black
	6 = NonHispanic Asian
	7 = Other Race Including Multi Racial;
run;

*Set lables;

data PD.stat;
set PD.ifthen2;
format DMStat Status. DMRisk Risk. RIDRETH3 Race.;
label DMStat = "Diabetes Status" DMRisk = "Population at Risk" RIDRETH3 = "Race and Ethnicity";
run;

*Check contents of Dataset;

proc contents data = PD.stat;
run;
**** PreDM - NHANES Population Counts

**Prediabetes Cost of Prevention Study**
*Merge and sorting the NHANEs Dataset to find population with undiagnosed prediabetes*
*Variables are stored in E:\NHANES\ for easy access for individual projects*
*Saved libraries correspond to years of NHANES

**Prep Code: Set Libraries;

libname NH "E:\NHANES\2015-2016\DATA";
libname PR "E:\PreDM\_temp";
run;

**Step 1: Sort SEQN variables;

proc sort 
data = NH.DEMO_I;
by SEQN; 
run;
proc sort 
data = NH.DIQ_I;
    by SEQN; 
run;


**Step 2: Merge Variables into one dataset;

*Megre Data by Variable;

data PR.Merge;
merge NH.DEMO_I NH.DIQ_I; 
by SEQN;
run;

*Check contents of Dataset;

proc contents data = PR.Merge;
run;

**Step Optional: Create Categorical Variables based on Conditions;

*Use Coniditons to Create New Variabe 1;

data PR.ifthen;
set PR.merge;
If DIQ010 = 1 then DMStat = 1; *1 = Diagnosed Diabetes;
Else If LBXGH = . then DMStat = 7; *7 Unknown;
run;

*Use Coniditons to Create New Variabe Varible 2;

data PR.ifthen2;
set PR.ifthen;
If RIDAGEYR > 40 and RIDAGEYR < 70 and BMXBMI > 25 then DMRisk = 1; *At risk;
Else DMRisk = 2; *Not at risk;
run;

*Get frequency of Unique Values in tables;

proc freq data = PD.ifthen;
tables DMStat DMRisk;
run;


**Step 3: Set formats and labels;

*Set formats;

proc format;                                                                                       
value Race
	1 = Mexican American
	2 = Other Hispanic
	3 = NonHispanic White
	4 = NonHispanic Black
	6 = NonHispanic Asian
	7 = Other Race Including Multi Racial;
run;

*Set lables;

data PR.ready;
set PR.merge;
format RIDRETH3 Race.;
label RIDRETH3 = "Race and Ethnicity";
run;

*Check contents of Dataset;

proc contents data = PR.ready;
run;

**Step 4: Set Weights and Clusters to create population counts;

*Sort Data by strata and cluster;

proc sort data = PR.ready;
by SDMVSTRA SDMVPSU;
run;

*Population count Using SAS, Show results as Table in SAS;

proc surveyfreq data = PR.Ready NOSUMMARY varheader = label;
ods output OneWay = PR.Result;
tables  RIDRETH3; *variables to use in table;
strata  SDMVSTRA; *first stage strata;
cluster SDMVPSU; *first stage cluster;
weight  WTMEC2YR; *survey weight;
run;

**Step Extra: Export Data;

*Export SAS Dataset to CSV;

proc export data = PR.Result dbms = csv
outfile = "E:\PreDM\NHANES\NHANES_popcount_race_raw.csv"
replace;
run;


