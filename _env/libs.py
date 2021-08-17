import os # Operating system navigation
import platform # Get OS in consistent format
import io # Input output control
import urllib.request # Donwload by URL link
from pathlib import Path
from datetime import datetime # Date and time stamps
from datetime import date # Date stamps
import sqlite3 # SQLite database manager
import urllib.request # Url requests with file download functions
from zipfile import ZipFile # Compressed and archive manager in python
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'
import numpy as np # Widely used matrix library for numerical processes
import scipy.stats as st # Statistics package best for t-test, ChiSq, correlation
import statsmodels.api as sm # Statistics package best for regression models
import matplotlib.pyplot as plt # Comprehensive graphing package in python
import geopandas as gp # Simple mapping library for csv shape files with pandas like syntax for creating plots using matplotlib 
from sklearn.preprocessing import StandardScaler # Standard scaling for easier use of machine learning algorithms
from sklearn.impute import SimpleImputer # Univariate imputation for missing data
from sklearn.decomposition import PCA # Principal compnents analysis from sklearn
from sklearn.ensemble import RandomForestRegressor # Random Forest regression component
from sklearn.feature_selection import RFECV # Recursive Feature elimination with cross validation
from sklearn.svm import LinearSVC # Linear Support Vector Classification from sklearn
from sklearn.svm import LinearSVR # Linear Support Vector Regression from sklearn
from sklearn.linear_model import LinearRegression # Used for machine learning with quantitative outcome
from sklearn.linear_model import LogisticRegression # Used for machine learning with quantitative outcome
from sklearn.model_selection import train_test_split # train test split function for validation
from sklearn.metrics import roc_curve # Reciever operator curve
from keras.models import Sequential # Uses a simple method for building layers in MLPs
from keras.models import Model # Uses a more complex method for building layers in deeper networks
from keras.layers import Dense # Used for creating dense fully connected layers
from keras.layers import Input # Used for designating input layers
from sklearn.metrics import auc # Area under the curve
import pysal as ps # Spatial data science modeling tools in python
from mgwr.gwr import GWR, MGWR # Geographic weighted regression modeling tools
from mgwr.sel_bw import Sel_BW # Bandwidth selection for GWR
import googlemaps # Google maps python wrapper
import openpyxl # A Python library to read/write Excel 2010 xlsx/xlsm files