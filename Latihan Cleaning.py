import pandas as pd

df = pd.read_excel(r"C:\Users\user\Downloads\Customer Call List.xlsx")
df

df = df.drop_duplicates()
df

df['Last_Name'] = df['Last_Name'].str.strip("123/._")
df

df = df.drop(columns = 'Not_Useful_Column')
df

df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','', regex = True)
df

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')
df

df[['Street', 'State','Code']] = df['Address'].str.split(',',n=2,expand=True)
df

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')
df

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')
df

df = df.fillna('')
df

for x in df.index:
    if df.loc[x,"Address"] == 'N/a':
        df.drop(x,inplace=True)
df

for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == '':
        df.drop(x,inplace=True)
df

df = df.reset_index(drop=True)
df
