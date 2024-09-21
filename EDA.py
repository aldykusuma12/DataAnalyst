import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\user\Downloads\world_population.csv")
df

pd.set_option('display.float_format', lambda x: '%.2f' % x)
#buat nambahin 0 dibelakang koma (%.2f) = 2 angka dibalkang koma
df

df.info()

df.select_dtypes(include='object')
#buat ngeliat data dengan tipe object

df.describe()

df.isnull().sum()
#untuk tau berapa banyak yang ada 0

df.nunique()
#buat tau ada berapa data yang unik dimasing2 kolom

df.sort_values(by="2022 Population", ascending=False).head(10)
#sebenernya bisa lebih mudah by nya diganti sam rank aja

df.corr(numeric_only=True)
#harus pake numeric_only, soalnya kalo ngga yang string juga ikut ke correlation

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.rcParams['figure.figsize']=(20,7)
#sns buat nunjukin heatmapnya dari data correlation, terus yang plt buat nyesuain sizenya

df[df['Continent'].str.contains('Oceania')]
#pake df[] didepannya, soalnya nnti hasilnya false/true

df2 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)
df2
#jangan lupa numeric_only karena yang stringnya ikut ke itung, df2 tandanya bikin tabel baru

df2.plot.bar(title = 'Population in the Continent', figsize=(13,5))

df3 = df2.transpose()
df3

df3.plot.barh(title = 'Population in the Continent', figsize=(13,5))

df2.plot.box()
