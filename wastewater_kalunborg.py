import io
import os
import pandas as pd
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("used_water_pollution_data/Renseanl_g (Spildevand)_20240905_172427_Kalundborg.csv", sep=";", encoding='utf-8') #encoding='ISO-8859-1'
df = pd.DataFrame(data)
#print(df.head())
#print(df.columns)
df_sorted = df.sort_values(by='Dato')
data_frame = df_sorted[['Dato','Dataejer','Målested navn', 'Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed' ]]
#print(data_frame)
unique = data_frame['Målested navn'].unique()
#
## Create separate DataFrames for each unique date
separate_dataframes = {}
count = 0
cnt_avg = 0

for val in unique:
    df_filtered = data_frame[data_frame['Målested navn'] == val]
    separate_dataframes[val] = df_filtered
    count +=1
print("amount of places are: "+str(count))
print(unique)

for val, df in separate_dataframes.items():
    print(f"\nData for {val}:")
    frame = ['Dato','Målested navn','Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed']
    df_2 = df[frame].copy()
    df_2['Resultat'] = df_2['Resultat'].str.replace(',', '.')
    df_2['Resultat'] = pd.to_numeric(df_2['Resultat'], errors='coerce')
    df_grouped = df_2.groupby('Stofparameter').agg({'Resultat': 'mean'})
    #print(df_grouped)

    # Exclude items
    df_2 = df_2[df_2['Stofparameter'] != 'pH']
    df_2 = df_2[df_2['Stofparameter'] != 'pH-målingstemperatur']
    df_2 = df_2[df_2['Stofparameter'] != 'Suspenderede stoffer']


    Stofparameter = df_2['Stofparameter']
    Resultat = df_2['Resultat']
    idx = df_2.groupby('Stofparameter')['Resultat'].idxmax()
    df_max = df_2.loc[idx, ['Målested navn', 'Stofparameter', 'Resultat', 'Enhed']]

    print(df_max)


   #--------------------------plot----------------------------------
    with pd.ExcelWriter('ORNUM Slam afvandet.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        df_max.to_excel(writer, sheet_name='Sheet2', index=False)
    if val == 'ORNUM Slam afvandet':
        plt.figure(figsize=(10, 6))
        plots = sns.barplot(x=Stofparameter, y=Resultat,  gap=0.1, hue=Stofparameter, legend=False, errorbar=None)
        for bar in plots.patches:
            plots.annotate(format(bar.get_height(), '.2f'),
                           (bar.get_x() + bar.get_width() / 2,
                            bar.get_height()), ha='center', va='center',
                           size=6, xytext=(0, 8),
                           textcoords='offset points')

        plt.title(f"Contaminants in sawege, {val}, for August 2024")
        plt.xlabel('Compounds')
        plt.ylabel('Concentration, mg/Kg')
        plt.xticks(rotation=25, ha="right")  # Rotate x-axis labels if needed
        plt.tight_layout()  # Adjust layout to fit labels

        plt.savefig(f'contamination_{val}.png')

        plt.show()