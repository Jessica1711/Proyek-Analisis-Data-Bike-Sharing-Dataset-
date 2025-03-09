!pip install streamlit babel
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

from google.colab import drive
drive.mount('/content/drive')
day_df = pd.read_csv('/content/drive/MyDrive/Proyek Analisis Data/day.csv', delimiter=",")
day_df.head()
hour_df = pd.read_csv('/content/drive/MyDrive/Proyek Analisis Data/hour.csv', delimiter=",")
hour_df.head()
