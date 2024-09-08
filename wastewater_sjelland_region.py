# script to treat data from csv, as example here was taken file with 1700 rows
# you can print out max value of contaminants into console, sort data according to places, build plot according to
# places, save information into separated files. Just comment/uncomment correspondent block of code to launch it
# data have a little bit misleading information about micro- and mili- units of kilograms



import io
import os
from scipy.interpolate import make_interp_spline
import numpy as np
import pandas as pd
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt

#asign wariables
separate_dataframes = {}
unique_compounds_dict = {}
count = 0
cnt_avg = 0
cnt = 0

#                           STEP ONE. Observe Sjaelland region. Wastewater data collected presumably from the sump facilities.
#                           Scrips bellow can sort out and print out data with max values of each component from data set



#--------------------------------------declare and open data set for Sjelland region----------------------------------------------------
#                                      comment/uncomment file path to file to check capital area or province

data = pd.read_csv("used_water_pollution_data/Renseanl_g (Spildevand)_20240905_200515_Sjelland.csv", sep=";", encoding='utf-8')
#data = pd.read_csv("used_water_pollution_data/Renseanl_g(Spildevand)_20240904_153305Hovetstaden.csv", sep=";", encoding='utf-8')

df = pd.DataFrame(data)
#print(df)

df_sorted = df.sort_values(by='Dato')
data_frame = df_sorted[['Dato','Dataejer','Målested navn', 'Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed' ]]
unique = data_frame['Målested navn'].unique()


#-------------------------------------write, print out a list of plases where samples have been taken--------------------------------------


#for val in unique:
#    df_filtered = data_frame[data_frame['Målested navn'] == val]
#    separate_dataframes[val] = df_filtered
#    count += 1

#print("amount of places are: " + str(count))
#print(unique)


##-----------------------------------print out a list of compounds and its maximum through all data set-------------------------------------

#unique_compounds = data_frame['Stofparameter'].unique()
#for i in unique_compounds:
#    cnt+=1
#    df_compounds_filtered = data_frame[data_frame['Stofparameter'] == i]      # if dict set is needed
#    unique_compounds_dict[i] = df_compounds_filtered                          # we may create it here and pass value
#
#    filtered_data = df.loc[df['Stofparameter'] == i].copy()
#    filtered_columns = filtered_data[['Målested navn','Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed']]
#    filtered_data['Resultat'] = filtered_data['Resultat'].str.replace(',', '.')
#    filtered_data['Resultat'] = pd.to_numeric(filtered_data['Resultat'], errors='coerce')
#    max_rfiltered = filtered_data.loc[filtered_data['Resultat'].idxmax()]
#    print(max_rfiltered[['Målested navn','Stofparameter','Resultat','Enhed']])
#    print(f"{cnt} -------------------------------------------------------------- ")

#print("amount of componds is: "+ str(cnt))
#print(unique_compounds)
#
#-------------------------------------------------------list of measured compound names in dataset -------------------------------------------------------

# Temperatur' 'Suspenderede stoffer' 'Kemisk iltforbrug' 'Ammoniak+ammonium-N' 'Perfluornonansulfonsyre (sum forgrenet og lineær)' 'Nitrogen, total N' 'Bundfald eft. 2 tim.'
# 'Perfluornonansyre (sum forgrenet og lineær)' 'Perfluordecansulfonsyre (sum forgrenet og lineær)' 'Bly' 'Perfluorundecansulfonsyre (sum forgrenet og lineær)'
# 'Perfluoroctansyre (sum forgrenet og lineær)' 'Nikkel' '6:2 Fluortelomersulfonsyre (sum forgrenet og lineær)' 'Perfluorheptansyre (sum forgrenet og lineær)'
# 'Perfluorpentansyre (sum forgrenet og lineær)' 'Sum af PFAS, 22 stoffer' 'Cadmium' 'pH' 'pH-målingstemperatur' 'Perfluorundecansyre (sum forgrenet og lineær)' 'Glødetab, total'
# 'Phosphor, total-P' 'Nitrit+nitrat-N' 'BI5 modificeret\xa0' 'Zink' 'Perfluoroctansulfonamid (sum forgrenet og lineær)' 'Perfluorbutansulfonsyre (sum forgrenet og lineær)'
# 'Perfluordecansyre (sum forgrenet og lineær)' 'Kobber' 'PFAS (sum af PFOA, PFOS, PFNA og PFHxS)' 'BI5' 'Tørstof,total' 'Perfluorbutansyre (sum forgrenet og lineær)'
# 'Perfluortridecansyre (sum forgrenet og lineær)' 'Perfluorhexansyre (sum forgrenet og lineær)' 'Chrom' 'Perfluordodecansulfonsyre (sum forgrenet og lineær)'
# 'Perfluordodecansyre (sum forgrenet og lineær)' 'Kviksølv' 'Perfluorheptansulfonsyre (sum forgrenet og lineær)' 'Perfluorhexansulfonsyre (sum forgrenet og lineær)'
# 'Perfluortridecansulfonsyre (sum forgrenet og lineær)' 'Perfluorpentansulfonsyre (sum forgrenet og lineær)' 'Perfluoroctansulfonsyre (sum forgrenet og lineær)' 'Barium' 'Nitrat-N'
# 'Kemiske iltforbrug, modificeret' 'C10-C40 kulbrintefraktion' 'C5-C10 kulbrintefraktion' 'Acenaphthylen' 'C25-C40 kulbrintefraktion' 'Benz(a)pyren' 'C5-C40 kulbrintefraktion' 'C10-C25 kulbrintefraktion'
# 'PAH (sum af 16)' 'Indeno(1,2,3-cd)pyren' 'Pyren' 'Benzen' 'Naphthalen' 'Antracen' 'm+p-Xylen' 'Cyanid, total' 'Fluoranthen' 'Toluen' 'Tin' 'Fluoren' 'Arsen' 'Benzo(b+j+k)fluranthen' 'Tributyltin'
# 'Dibenz(a,h)anthracen' 'Ethylbenzen' 'Acenaphthen' 'o-Xylen' 'Benz(ghi)perylen' 'Benz(a)anthracen' 'Chrysen' 'Oxygenmætning' 'Phenanthren' 'Nonylphenol +nonylphenolmono- og diethoxylater'
# 'Nonylphenol-monoethoxylater (NP1EO)' 'Chlorid' 'Nonylphenol-diethoxylater (NP2EO)' 'PAH (sum af 9)' 'Nonylphenoler' 'Lineære alkylbenzensulfonater' 'Di(2-ethylhexyl)phthalat' 'Sulfat'
# '2,3,4,6-Tetrachlorphenol' '2,4+2,5-Dichlorphenol' '3-Chlorphenol' '3,4-Dichlorphenol' '4-Chlorphenol' 'Mechlorprop' '2-Chlorphenol' 'MCPA' '2-(4-Chlorphenoxy)propionsyre' '2-(2-Chlor-6-methylphenoxy)propionsyre'
# '4,6-Dichlor-2-methylphenol' '3,5-Dichlorphenol' 'Dichlorprop' '2,4-Dichlorphenoxyeddikesyre' 'Molybden' '2,4,6-Trichlorphenol' 'Phenol-indeks' '2-(2-Chlorphenoxy)propionsyre' '4-Chlor-2-methylphenol'
# '6-Chlor-2-methylphenol' '2,6-Dichlorphenol' '2-Chlorphenoxy-eddikesyre' '2-(2,6-dichlorphenoxy)propionsyre' 'Pentachlorphenol' '(2,4,5,-Trichlorphenoxy)-eddikesyre' '2,4,5-Trichlorphenol'
# '2,3-Dichlorphenol' '4-Chlorphenoxyeddikesyre' '4-Chlor-3-methylphenol' 'Total organisk kulstof' 'Magnesium' 'Kalium' 'Fedt' 'Olie og fedt' 'Olie' '1H,1H,2H,2H-Perfluoroctanol (sum forgrenet og lineær)'
# 'Bisphenol A' 'Perfluortetradecansyre (sum forgrenet og lineær)' 'Vanadium' 'Selen' 'Kobolt' '1H,1H,2H,2H-Perfluordecanol (sum forgrenet og lineær)' 'Chrom, hexavalent' 'Perfluorhexadecansyre (sum forgrenet og lineær)'
# 'Konduktivitet' 'Bor' 'Monobutyltin' 'Anioniske detergenter' 'Perfluor([5-methoxy-1,3-dioxolan-4-yl]oxy)eddikesyre' 'HFPO-DA (GenX)' 'Kjeldahl-N' 'Dodecafluor-3H-4,8-dioxanonanoat (sum forgrenet og lineær)'
# 'Perfluoroctadecansyre (sum forgrenet og lineær)' 'Chrom, trivalent' 'Nitrat' 'Nitrit' 'Orthophosphat-P'
#

#------------------------------------- sort and split data into separated frames according to places (locations) ----------------------------------------

#for val, df in separate_dataframes.items():
#    print(f"\nData for {val}:")
#    frame = ['Dato', 'Målested navn', 'Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed']
#    df_2 = df[frame].copy()
#    df_2['Resultat'] = df_2['Resultat'].str.replace(',', '.')
#    df_2['Resultat'] = pd.to_numeric(df_2['Resultat'], errors='coerce')
#    df_grouped = df_2.groupby('Stofparameter').agg({'Resultat': 'mean'})
#    #print(df_grouped)
#
#    df_2 = df_2[df_2['Stofparameter'] != 'pH']
#    df_2 = df_2[df_2['Stofparameter'] != 'pH-målingstemperatur']
#    df_2 = df_2[df_2['Stofparameter'] != 'Suspenderede stoffer']
#
#    df_2.loc[(df_2['Enhed'] == 'µg/kg TS') | (df_2['Enhed'] == 'µg/kg P'), 'Resultat'] *= 0.001
#    df_2.loc[(df_2['Enhed'] == 'µg/kg') | (df_2['Enhed'] == 'µg/l') , 'Resultat'] *= 0.001
#
#    Stofparameter = df_2['Stofparameter']
#    Resultat = df_2['Resultat']
#    idx = df_2.groupby('Stofparameter')['Resultat'].idxmax()
#    df_max = df_2.loc[idx, ['Målested navn', 'Stofparameter', 'Resultat', 'Enhed']]
#
#    print(df_max)
# #----------------------------------------- save data into files according to places -------------------------------------------------------
#
#    #with pd.ExcelWriter(f'{val}.xlsx', engine='openpyxl') as writer:
#    #    df.to_excel(writer, sheet_name='Sheet1', index=False)
#    #    df_max.to_excel(writer, sheet_name='Sheet2', index=False)
#
# #------------------------------------------------------- build plot and save it into root directory ------------------------------------------

#    if val == 'Bjergmarken I slam':
#         plt.figure(figsize=(10, 6))
#         plots = sns.barplot(x=Stofparameter, y=Resultat, gap=0.1, hue=Stofparameter, legend=False, errorbar=None)
#         for bar in plots.patches:
#             plots.annotate(format(bar.get_height(), '.2f'),
#                            (bar.get_x() + bar.get_width() / 2,
#                             bar.get_height()), ha='center', va='center',
#                            size=6, xytext=(0, 8),
#                            textcoords='offset points')
#
#         plt.title(f"Contaminants, {val}, for August 2024")
#         plt.xlabel('Compounds')
#         plt.ylabel('Concentration, mg/kg')
#         plt.xticks(rotation=25, ha="right")
#         plt.tight_layout()
#
#         plt.savefig(f'contamination_{val}.png')
#
#         plt.show()


#                                       STEP TWO. Investigation of location with retried max data from the script above

# Suspected object was chosen Roskilde sump facility, as in contains a variety of heavy metals and has taken a max rates 
# from the script above.
# Obviously we can check any other objects, which we are willing to


#---------------------------------------declare and open data set for Roskilde area--------------------------------------------='utf-8')

data2 = pd.read_csv("used_water_pollution_data/Renseanl_g (Spildevand)_20240906_140827_Bjergmarken.csv", sep=";", encoding='utf-8')
df_r = pd.DataFrame(data2)

df_r['Dato'] = pd.to_datetime(df_r['Dato'], format='%d-%m-%Y', errors='coerce')

df_r_sorted = df_r.sort_values(by='Dato')

data_frame_r = df_r_sorted[['Dato', 'Målested navn', 'Stofparameter', 'Resultat-attribut', 'Resultat', 'Enhed']].copy()

unique_ = data_frame_r['Stofparameter'].unique()

data_frame_r['Resultat'] = data_frame_r['Resultat'].str.replace(',', '.')
data_frame_r['Resultat'] = pd.to_numeric(data_frame_r['Resultat'], errors='coerce')
data_frame_r.loc[(data_frame_r['Enhed'] == 'µg/kg TS') | (data_frame_r['Enhed'] == 'µg/kg P'), 'Resultat'] *= 0.001
data_frame_r.loc[(data_frame_r['Enhed'] == 'µg/kg') | (data_frame_r['Enhed'] == 'µg/l') , 'Resultat'] *= 0.001

#-------------------coment/uncoment to hide/show info in wastewater-----------------------------


#data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'mg/kg TS']
#data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'µg/kg TS']
#data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'mg/kg P']
#y_title = 'mg/L'
#atr = 'wastewater'


#-------------------coment/uncoment to hide/show rates in sludge under wastewater-----------------

data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'µg/l']
data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'µg/kg']
data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'mg/l']
data_frame_r = data_frame_r[data_frame_r['Enhed'] != 'mg/kg']
y_title = 'mg/Kg'
atr = 'sludge'

df_r_grouped = data_frame_r.groupby('Stofparameter').agg({'Resultat': 'mean'})

elements = ['Cadmium', 'Chrom', 'Bly', 'Kviksølv', 'Arsen', 'Nikkel', 'Kobber', 'Zink', 'Uran', 'Kobolt', 'Selen']

#----------------------ordinary ploting of each plot------------------------------------
#for i in elements:
#    frame = data_frame_r[data_frame_r['Stofparameter'] == i][['Dato', 'Resultat', 'Enhed']]
#    print(f"--------------{i}---------------------")
#    print(frame)
#
#
#    concentration_sorted = data_frame_r[data_frame_r['Stofparameter'] == i]#.sort_values(by='Dato')
#    year_sorted = concentration_sorted['Dato']
#    concentration_sorted_values = concentration_sorted['Resultat']
#    #-------------------------- plotting for each i value --------------------------------------------
#    plt.figure(figsize=(10, 6))
#    plots = sns.barplot(x=year_sorted, y=concentration_sorted_values, hue=year_sorted, errorbar=None)
#    # Annotate bars with values
#    for bar in plots.patches:
#        plots.annotate(format(bar.get_height(), '.4f'),
#                       (bar.get_x() + bar.get_width() / 2,
#                        bar.get_height()), ha='center', va='center',
#                        size=5, xytext=(0, 8),
#                        textcoords='offset points')
#
#
#    plt.xlabel('Date')
#    plt.ylabel(f'Concentration {y_title}')
#    plt.xticks(rotation=75, ha="right")
#    plt.title(f"Contaminants, {i}, for Roskilde 1990 - now, {atr}")
#    plt.tight_layout()
#    plt.savefig(f'contamination_{i}.png')
#    # Show plot
#    plt.show()
#---------------------------------------------save plots as sublots grid---------------------------------------------

cnt = 0
n = 0
fig, axes = plt.subplots(6, 2, figsize=(15, 18))
for i in elements:
    frame = data_frame_r[data_frame_r['Stofparameter'] == i][['Dato', 'Resultat', 'Enhed']]
    print(f"-----------------{i}---------------------")
    print(frame)
    concentration_sorted = data_frame_r[data_frame_r['Stofparameter'] == i]#.sort_values(by='Dato')
    year_sorted = concentration_sorted['Dato'].dt.strftime('%Y-%m') #.dt.year
    concentration_sorted_values = concentration_sorted['Resultat']

    #-------------------------- plotting for each i value --------------------------------------------

    ax = axes[cnt, n]
    # to depict in line plot, uncomment bellow
    #sns.lineplot(x=year_sorted, y=concentration_sorted_values, ax=ax, legend=False, errorbar=None )
    plots = sns.barplot(x=year_sorted, y=concentration_sorted_values, ax=ax, hue=year_sorted, errorbar=None)

    for bar in plots.patches:
        ax.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                        size=5, xytext=(0,2),
                        textcoords='offset points')

    if n % 2 == 0:
        n += 1
    else:
        n = 0
        cnt += 1

    ax.set_title(f"{i}", fontsize=10)
    ax.set_xlabel("  ")
    ax.set_ylabel(f'Concentration {y_title}', fontsize=5)
    ax.tick_params(axis='x', rotation=65, labelsize=4)

plt.tight_layout()
plt.suptitle(f"Contaminants, Roskilde from 1990 to nowadays, {atr}", fontsize=20)
plt.subplots_adjust(top=0.92, wspace=0.15, hspace=0.5)
plt.savefig(f"Contaminants, Roskilde from 1990 to nowadays, {atr}.png")
plt.show()