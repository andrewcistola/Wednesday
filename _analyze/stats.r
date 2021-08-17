tables <- dbListTables(con_sqlite)
table <- tables[1]

query = paste(
    'SELECT ', table, '.*
    FROM ', table, 
    ';',
    sep = '') 
df_XY <- dbGetQuery(con_sqlite, query)
head(df_XY)

df_XY$Very_High <- ifelse(df_XY$Severity_Level == 'Very High', 1, 0)
df_XY$High <- ifelse(df_XY$Severity_Level == 'High', 1, 0)
df_XY$Moderate <- ifelse(df_XY$Severity_Level == 'Moderate', 1, 0)
df_XY$Low <- ifelse(df_XY$Severity_Level == 'Low', 1, 0)
df_XY$Very_Low <- ifelse(df_XY$Severity_Level == 'Very Low', 1, 0)
summary(df_XY)

Y = 'Cost'
X = c('ER_Visits', 'Very_High', 'High', 'Moderate', 'Low', 'Very_Low')

OLS_M = 'Ordinary Least Squares Regression Model'
D = df_XY
F = as.formula(paste(Y, ' ~ ', paste(X, collapse = ' + '), sep = ''))
OLS = lm(F, data = D)
summary(OLS)

OLS_A1 =  'OLS Assumption 1: Sampling (Random sample, observations > predictors, predictor is associated with outcome)'
N = nrow(df_XY)
Na = colSums(is.na(df_XY))
COR = 'Spearman Correlation'
SPR = cor(df_XY$Cost, df_XY$ER_Visits, method = 'spearman')

OLS_A2 = 'OLS Assumption 2: Specification (Relationship between predictor and outcome is linear)'
UTT = raintest(OLS) # Utt's Rainbox Test

OLS_A3 = 'OLS Assumption 3:  Normality (Errors are normal with a mean = 0)'
JB = JarqueBeraTest(resid(OLS)) # Jarque Bera Test
AD = AndersonDarlingTest(resid(OLS)) # Anderson-Darling Test
png(paste('_fig/', table, '_QQ_plot.png', sep = ''))
qqnorm(resid(OLS))
qqline(resid(OLS))
dev.off()

OLS_A4 = 'OLS Assumption 4: No Autocorrelation (Error terms are not correlated with each other)'
DW = DurbinWatsonTest(OLS) # Drubin-Watson Test

OLS_A5 = 'OLS Assumption 5: Homoskedasticity (Error is even across observations)'
BP = bptest(OLS) # Breusch-Pagan Test
GQ = gqtest(OLS) # Goldfield Quant Test
png(paste('_fig/', table, '_residuals_plot.png', sep = ''))
plot(resid(OLS))
abline(0,0)
dev.off()

OLS_A6 = 'OLS Assumption 6: No Colinearity (Predictors are not correlated with each other)'
plot = ggplot(subset(melt(round(cor(D[X], use = "pairwise.complete.obs"), 3)), value < 1), 
                aes(Var1, 
                    Var2)) + 
            geom_tile(aes(
                fill = value)) + 
            geom_text(aes(
                label = value),
                size = 1) + 
            scale_fill_gradient2(
                low = low,
                mid = mid,
                high = high) +
            labs(
                title = paste('Correlation Matrix |', table, Y, sep = " "),
                fill = 'predictor\ncorrelation') +
            theme_minimal() +
            theme(
                text = element_text(family = 'Bookman'),
                plot.title = element_text(size = 12),
                panel.grid.major = element_blank(), 
                panel.grid.minor = element_blank(),
                panel.border = element_blank(),
                panel.background = element_blank(),
                axis.title = element_blank(),
                axis.text = element_text(size = 8),
                axis.text.x = element_text(angle = 90))
ggsave(paste('_fig/', table, '_correlation_plot.png', sep = ''), plot = plot) # Save ggplot as jpeg

COL = check_collinearity(OLS) # Check collinearity

GLM = 'Log link [Y = ln(DV)] (aka: Log-Linear) with poisson error (aka: Poisson regression)' 
G = poisson()
POI = glm(F, data = D, family = G) 
summary(POI)

OVD = check_overdispersion(POI) # F-test for overdispersion, if signficiant use negative binomial
ZI = check_zeroinflation(POI) # F-test for zero-inlfated, if observed > predicted use negative binomial

GLM_NB = 'Log link [Y = ln(DV)] (aka: Log-Linear) with gamma error (aka: Negative binomial regression)'
NB = glm.nb(F, data = D)
summary(NB)

df_XY <- dbGetQuery(con_sqlite, query)
HLM = "Hierarchical Linear Model with Random Intercepts"
H = 'Severity_Level'
X = 'ER_Visits'
Y = 'Cost'
F = as.formula(paste(Y, ' ~ (1|', H, ') + ' , paste(X, collapse = ' + '), sep = ''))
RAND = lmer(F, data = D)
summary(RAND)

ANOVA = 'One Way ANOVA for MLE'
MLE = ranova(RAND)
ICC = icc(RAND) # Intra-class correlation coefficient
SING = check_singularity(RAND) # Check Singularity of mixed-effects model

RANK = compare_performance(OLS, POI, NB, RAND)
png(paste('_fig/', table, '_models_plot.png', sep = ''))
plot(compare_performance(OLS, POI, NB, RAND))
dev.off()

sink(file = 'README', append = TRUE, type = 'output')
cat(c('##Statistical Analysis for', table, 'Data\n\n'), file = 'README', append = TRUE)
cat(c('###OLS Model and Assumption Tests\n\n'), file = 'README', append = TRUE)
summary(OLS)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A1, '\n\n', sep = ''), file = 'README', append = TRUE)
cat(c('Number of observations: ', N, '\n'), file = 'README', append = TRUE)
cat(c('Number of missing values: \n'), file = 'README', append = TRUE)
print(Na)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c(COR, ': ', SPEAR, '\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A2, '\n', sep = ''), file = 'README', append = TRUE)
print(UTT)
cat(c('Significant = Non-linearity\n\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A3, '\n', sep = ''), file = 'README', append = TRUE)
cat(paste('!["_fig/', table, '_QQ_plot.png"]\n', sep = ''), file = 'README', append = TRUE)
print(JB)
cat(c('Signficiant = Non-normal\n\n'), file = 'README', append = TRUE)
print(AD)
cat(c('Signficiant = Non-normal\n\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A4, '\n', sep = ''), file = 'README', append = TRUE)
print(DW)
cat(c('Signficiant = Autocorrelation\n\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A5, '\n', sep = ''), file = 'README', append = TRUE)
cat(paste('!["_fig/', table, '_residuals_plot.png"]\n', sep =''), file = 'README', append = TRUE)
print(BP)
cat(c('Signficiant = Homoscedastic\n\n'), file = 'README', append = TRUE)
print(GQ)
cat(c('Significant = Heteroscedastic\n\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(paste('####', OLS_A6, '\n', sep = ''), file = 'README', append = TRUE)
cat(paste('!["_fig/', table, '_correlation_plot.png"]\n', sep = ''), file = 'README', append = TRUE)
print(COL)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c('###Generalized Linear Models\n\n'), file = 'README', append = TRUE)
cat(c(GLM_POI, '\n'), file = 'README', append = TRUE)
summary(POI)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c(OVD, '\n'), file = 'README', append = TRUE)
cat(c(ZI, '\n'), file = 'README', append = TRUE)
cat(c(GLM_NB, '\n'), file = 'README', append = TRUE)
summary(NB)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c('###Hierarchical Linear Models\n\n'), file = 'README', append = TRUE)
cat(c(HLM, '\n\n'), file = 'README', append = TRUE)
summary(RAND)
cat(c(ANOVA, '\n'), file = 'README', append = TRUE)
print(MLE)
cat(c('\n\n'), file = 'README', append = TRUE)
print(ICC)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c('Is model singular? (overly-complex): ', SING, '\n'), file = 'README', append = TRUE)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c('###Model Performance and Comparison\n\n'), file = 'README', append = TRUE)
cat(c('!["_fig/', table, '_performance_plot.png"]\n'), file = 'README', append = TRUE)
print(RANK)
cat(c('\n\n'), file = 'README', append = TRUE)
cat(c('**********\n\n'), file = 'README', append = TRUE)
cat(c('Updated :', Sys.time(), ' by ', user_email, '\n\n'), file = 'README', append = TRUE)
cat(c('Disclaimer: ', project_disclaimer, '\n\n'), file = 'README', append = TRUE)
cat(c('&copy;', user_form, '\n\n'), file = 'README', append = TRUE)
sink()