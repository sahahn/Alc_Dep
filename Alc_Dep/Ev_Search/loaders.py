import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler

def intoarrays(data, key='Alc'):

    X = np.array(data.drop(key, axis=1))
    y = np.array(data.loc[:, key])

    return [X,y]

def load_enigma(loc='more_data.csv', d_keys=None, i_keys=None, x_y=True):
    data = pd.read_csv(loc, na_values=['#NULL!', ''])
    data = data.drop(['PI', 'Subject', 'Dependent = 1', 'Unnamed: 4', 'Unnamed: 19',
     'Unnamed: 20', 'Unnamed: 89'], axis=1)
    
    #data = data.dropna(axis='rows', how='any', thresh=145)
    #data = data.fillna(data.mean())

    data = data.dropna(axis='columns', how='all')
    data = data.dropna()

    rename_dict = {'Dependent': 'Alc'}
    data = data.rename(index=str, columns = rename_dict)

    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data

def load_germans(loc='germans.csv', d_keys=None, i_keys=None, x_y=True):
    
    data = pd.read_csv(loc)
    data = data.dropna(axis=1, how='any')
    
    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data

def load_unres_enigma(loc='enigma.csv', d_keys=None, i_keys=None, x_y=True):

    data = pd.read_csv(loc)
    data = data.dropna(axis=1, how='any')
    
    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data

def load_HCP(loc='hcp_residuals.csv', config=1, d_keys=None, i_keys=None, x_y=True):
    data = pd.read_csv(loc)
    
    data = data.dropna(axis=1, how='any')
    data['Alc'] = -1

    #Controls
    data.loc[(data.Alc1 == 0) & (data.Alc2 == 0) & (data.Alc3 == 0) & (data.Alc4 == 0), 'Alc'] = 0
    
    c_name = 'Alc' + str(config)
    data.loc[(data[c_name] == 1), 'Alc'] = 1
    
    data = data.drop(data[data.Alc==-1].index)
    data = data.drop(['Alc1', 'Alc2', 'Alc3', 'Alc4'], axis=1)
    
    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data


def load_monster(loc='monster.csv', d_keys=None, i_keys=None, x_y=True):

    data = pd.read_csv('monster.csv')
    data = data.drop('Unnamed: 0', axis=1)

    #data = data[(data.Site != 10)]

    train_data = data[(data.Site != 5)]
    test_data = data[(data.Site == 5)]

    train_data = train_data.drop('Site', axis=1)
    test_data = test_data.drop('Site', axis=1)

    train_data = process(train_data, d_keys, i_keys)
    test_data = process(test_data, d_keys, i_keys)

    if x_y:
        return intoarrays(train_data), intoarrays(test_data)
    else:
        return train_data, test_data


def load_enigma_subset(loc='monster.csv', d_keys=None, i_keys=None, x_y=True):

    data = pd.read_csv('monster.csv')
    data = data.drop('Unnamed: 0', axis=1)

    data = data[(data.Site != 1) & (data.Site != 2) & (data.Site != 10)]

    data = data.drop('Site', axis=1)
    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data

def load_enigma_and_HCP_negs(loc='monster.csv', d_keys=None, i_keys=None, x_y=True):

    data = pd.read_csv('monster.csv')
    data = data.drop('Unnamed: 0', axis=1)

    data = data.drop('Site', axis=1)
    data = process(data, d_keys, i_keys)

    if x_y:
        return intoarrays(data)
    else:
        return data



def load_enigma_and_german_res(loc ='Enigma_Germans_Res.csv', d_keys=None, i_keys=None, x_y=True, e=True, g=True):
    
    data = pd.read_csv(loc)
    data = data.dropna(axis=1, how='any')

    data = process(data, d_keys, i_keys)

    enigma = data[:-382]
    germans = data[-382:]

    if e and g:
        
        if x_y:
            return intoarrays(enigma), intoarrays(germans)
        else:
            return enigma, germans

    if e:

        if x_y:
            return intoarrays(enigma)
        else:
            return enigma

    if g:

        if x_y:
            return intoarrays(germans)
        else:
            return germans



def process(data, d_keys, i_keys):
    
    if d_keys != None:

        to_remove = set()
        col_names = list(data)

        for name in col_names:
            for key in d_keys:
                if key in name:
                    to_remove.add(name)

        data = data.drop(list(to_remove), axis=1)
        
    if i_keys != None:
        
        i_keys.append('Alc')
        
        to_remove = set()
        col_names = list(data)
        
        for name in col_names:
            flag = False
            
            for key in i_keys:
                if key in name:
                    flag = True
            
            if not flag:
                to_remove.add(name)
                
        data = data.drop(list(to_remove), axis=1)
            
    return data

def load_all(
    enigma_loc=None,
    german_loc=None,
    hcp_loc=None,
    hcp_config=1,
    d_keys=None,
    i_keys=None,
    x_y = True,
    all_together = False
    ):

    if enigma_loc != None:
        Enigma = load_enigma(loc=enigma_loc, d_keys=d_keys, i_keys=i_keys, x_y=False)
    else:
        Enigma = load_enigma(d_keys=d_keys, i_keys=i_keys, x_y=False)

    Enigma['dataset'] = 0

    if german_loc != None:
        German = load_germans(loc=german_loc, d_keys=d_keys, i_keys=i_keys, x_y=False)
    else:
        German = load_germans(d_keys=d_keys, i_keys=i_keys, x_y=False)
    
    German['dataset'] = 1

    if hcp_loc != None:
        HCP = load_HCP(loc=hcp_loc, config=hcp_config, d_keys=d_keys, i_keys=i_keys, x_y=False)
    else:
        HCP = load_HCP(config=hcp_config, d_keys=d_keys, i_keys=i_keys, x_y=False)
   
    HCP['dataset'] = 2

    all_data = pd.concat([Enigma, German, HCP])

    if all_together:

        all_data = all_data.drop('dataset', axis=1)
        return intoarrays(all_data)

    Enigma = all_data[all_data.dataset == 0]
    German = all_data[all_data.dataset == 1]
    HCP = all_data[all_data.dataset == 2]

    Enigma = Enigma.drop('dataset', axis=1)
    German = German.drop('dataset', axis=1)
    HCP = HCP.drop('dataset', axis=1)

    if x_y:
        return intoarrays(Enigma), intoarrays(German), intoarrays(HCP)

    return Enigma, German, HCP


def binarize_1X(in_value):
    if in_value == 1:
        return 0
    else:
        return 1
    
def conv_hcp_age(in_value):
    
    if '-' in in_value:
        i = in_value.split('-')
        
        return (float(i[0]) + float(i[1])) / 2
    
    elif '+' in in_value:
        i = in_value.replace('+', '')
        
        i = float(i)
        
        return i + 10

def conv_age(x):

    if type(x) == str:
        return -1
    else:
        return x

def conv_gender(x):

    if type(x) == str:
        return -1
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    
def conv_german_site(x):
    
    if x == 'Berlin':
        return 50
    elif x == 'Bonn':
        return 51
    elif x == 'Mannheim':
        return 52

def load_raw_hcp():
    
    ref_data = pd.read_csv('germans.csv')
    ref = list(ref_data)

    data = pd.read_csv('HCP.csv')
    var_names = list(data)

    conv_dict = {}

    for name in var_names:
        
        try:
        
            comp = name.replace('FS_', '')
            comp = comp.replace('Thck', 'thickavg')
            comp = comp.replace('Area', 'surfavg')
            comp = comp.split('_')

            comp[1] = comp[1].lower()
            comp = '_'.join(comp)

            comp = comp.replace('_thalamusproper_Vol', 'thal')
            comp = comp.replace('_caudate_Vol', 'caud')
            comp = comp.replace('_putamen_Vol', 'put')
            comp = comp.replace('_pallidum_Vol', 'pal')
            comp = comp.replace('_hippo_Vol', 'hippo')
            comp = comp.replace('_amygdala_Vol', 'amyg')
            comp = comp.replace('_accumbenssurfavg_Vol', 'accumb')
            
            if comp in ref:
                conv_dict[name] = comp
        
        except:
            pass
        
    conv_dict['FS_IntraCranial_Vol'] = 'ICV'
    conv_dict['Subject'] = 'SID'

    data = data.rename(index=str, columns = conv_dict)

    ref.append('SID')
    ref.append('Age')
    ref.append('ICV')

    for var in list(data):
        if var not in ref:
            data = data.drop(var, axis=1)
            
    data = data.dropna(axis=0, how='any')

    data2 = pd.read_csv('HCP_Drinking_Vars.csv')
    D_V = data2[['SID', 'Gender', 'Violates_DPW_guidelines','Binge_1+_Weekly','SSAGA_Alc_D4_Ab_Dx','SSAGA_Alc_D4_Dp_Dx']]

    all_data = pd.merge(data, D_V)

    all_data['Gender'] = all_data['Gender'].apply(binarize_1X)
    all_data['SSAGA_Alc_D4_Ab_Dx'] = all_data['SSAGA_Alc_D4_Ab_Dx'].apply(binarize_1X)
    all_data['SSAGA_Alc_D4_Dp_Dx'] = all_data['SSAGA_Alc_D4_Dp_Dx'].apply(binarize_1X)
    all_data['Age'] = all_data['Age'].apply(conv_hcp_age)

    all_data = all_data.drop('SID', axis=1)

    return all_data

def proc_raw_enigma(ref, data, control=False):
    
    names = [d for d in list(data) if d in ref]
    
    if not control:
        names.append('Dependent on Primary Drug ')
    else:
        names.append('Primary Drug')
        
    names.append('Site')
    names.append('Age')
    names.append('Sex')
    names.append('ICV.3')
    
    data = data.dropna(how='all', axis=1)
    data = data[names]
    
    data.Age = data.Age.apply(conv_age)
    data.Sex = data.Sex.apply(conv_gender)
    
    data = data.dropna()
    
    if not control:
        data = data.rename({'Dependent on Primary Drug ': 'Alc'}, axis=1)
    else:
        data = data.rename({'Primary Drug': 'Alc'}, axis=1)
        
    data = data.rename({'ICV.3': 'ICV'}, axis=1)
    data = data.dropna(axis='columns', how='all')
    data = data.drop(data[~data.applymap(np.isreal).all(1)].index, axis=0)
    
    return data


def load_raw_german():
    
    german = pd.read_excel('NGFNplus_merged_10_01_2019.xlsx')
    german = german.drop(['Llatvent', 'Rlatvent', 'SubjID', 'LSurfArea', 'RSurfArea', 'LThickness', 'RThickness', 'ICV.1', 'site_dmy1', 'site_dmy2'], axis=1)

    german.SITE = german.SITE.apply(conv_german_site)
    german = german.rename({'SITE': 'Site', 'Dx_AUD1' : 'Alc', 'age': 'Age', 'sexM1': 'Sex'}, axis=1)

    return german


def load_it_all(loc = 'All_Data.csv', age=False, sex=False, split_enigma=False, d_keys=None, i_keys=None):
    
    data = pd.read_csv(loc)
    data = data.drop(['Unnamed: 0'], axis=1)

    if age == False:
        data = data.drop(['Age'], axis = 1)
        
    if sex == False:
        data = data.drop(['Sex'], axis = 1)
    
    enigma = data[(data.Site != 50) & (data.Site != 51) & (data.Site != 52) & (data.Site != 70)]
    german = data[(data.Site == 50) | (data.Site == 51) | (data.Site == 52)]
    hcp    = data[ data.Site == 70]
    
    if split_enigma:
        t_inds = np.where(enigma.Site != 5)
        v_inds = np.where(enigma.Site == 5)
        
    enigma = enigma.drop('Site', axis=1)
    german = german.drop('Site', axis=1)
    hcp    = hcp.drop(   'Site', axis=1)
    
    if age:
        
        avg_age = np.mean(enigma[enigma.Age != -1].Age)
        enigma.Age = np.where(enigma.Age == -1, avg_age, enigma.Age) 
        german.Age = np.where(german.Age == -1, avg_age, german.Age) 
        hcp.Age    = np.where(hcp.Age == -1, avg_age, hcp.Age)
    
    if sex:
        
        enigma.Sex = np.where(enigma.Sex == -1, .5, enigma.Sex) 
        german.Sex = np.where(german.Sex == -1, .5, german.Sex) 
        hcp.Sex    = np.where(hcp.Sex == -1, .5, hcp.Sex)


    e,g,h = process(enigma, d_keys, i_keys), process(german, d_keys, i_keys), process(hcp, d_keys, i_keys)    
    e,g,h = intoarrays(e), intoarrays(g), intoarrays(h)
    scaler = StandardScaler()
    
    e[0] = scaler.fit_transform(e[0])
    g[0] = scaler.transform(g[0])
    h[0] = scaler.transform(h[0])
    
    if split_enigma:

        e1 = [e[0][t_inds], e[1][t_inds]]
        e2 = [e[0][v_inds], e[1][v_inds]]
    
        return e1, e2, g, h
    
    return e,g,h
    
    
        
    
        
    
    









