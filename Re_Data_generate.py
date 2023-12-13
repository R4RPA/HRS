import pyreadstat
import pandas as pd

def clean_df(result,old_column_names,new_column_names,year):
    result=result[old_column_names]
    result = result.rename(columns=dict(zip(old_column_names, new_column_names)))
    result['age']=year-result['birthyear']
    result['year_data']=int(year)
    return result

# YEAR 2006

# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/h06f4a.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()

needed_col=["PN", "HHID", "KLB037A", "KLB037B", "KLB037C", "KLB037D", "KLB037E",
            "KLB037F", "KLB037G", "KLB037H", "KLB037I", "KLB037J",
            "KLB030A", "KLB030B", "KLB030C", "KLB030D", "KLB030E",
            "KLB021A", "KLB021B", "KLB021C", "KLB021D", "KLB021E", "KLB021F",
            "KLB021G", "KLB021H", "KD174", "KD184", "KD122", "KD142", "KD143",
            "KD144", "KD145", "KD146", "KD101", "KX004_R", "KX067_R", "KX060_R",
            "KB014", "KC001", "KB002", "KB028", "KB089M1M","KB085", "KLB037A",
            "KLB037B", "KLB037C", "KLB037D", "KLB037E", "KLB037F", "KLB037G",
            "KLB037H", "KLB037I", "KLB037J"]
rename_col=["PN", "HHID", "AT1",  "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1",
             "CT3", "CT4", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
            "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7",
            "ctrauma1", "ctrauma3", "ctrauma4"
            ]
year=2006

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)

# YEAR 2008

# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/h08f3a.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()

needed_col=["PN", "HHID", "LLB037A", "LLB037B", "LLB037C", "LLB037D", "LLB037E",
             "LLB037F", "LLB037G", "LLB037K", "LLB037L", "LLB037M", "LLB037N",
             "LLB030A", "LLB030B", "LLB030C", "LLB030D", "LLB030E", "LLB030F",
             "LLB021A", "LLB021B", "LLB021C", "LLB021D", "LLB021E", "LLB021F",
             "LLB021G", "LLB021H", "LD174", "LD184", "LD122", "LD142", "LD143",
             "LD144", "LD145", "LD146", "LD101", "LX004_R", "LX067_R", "LX060_R",
             "LB014", "LC001", "LB002", "LB028", "LB089M1M","LB085", "LLB037A",
            "LLB037B", "LLB037C", "LLB037D", "LLB037E", "LLB037F", "LLB037G",
            "LLB037K", "LLB037L", "LLB037M", "LLB037N"]
rename_col=["PN", "HHID", "AT1",  "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2",
             "CT3", "CT4", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "discrimination6", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
             "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7",
             "ctrauma1", "ctrauma2", "ctrauma3", "ctrauma4"
            ]
year=2008

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)

# YEAR 2010

# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/hd10f6a.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()

needed_col=["PN", "HHID", "MLB037A", "MLB037B", "MLB037C", "MLB037D", "MLB037E",
             "MLB037F", "MLB037G", "MLB037K", "MLB037L", "MLB037M", "MLB037N",
             "MLB030A", "MLB030B", "MLB030C", "MLB030D", "MLB030E", "MLB030F",
             "MLB021A", "MLB021B", "MLB021C", "MLB021D", "MLB021E", "MLB021F",
             "MLB021G", "MLB021H", "MD174", "MD184", "MD122", "MD142", "MD143",
             "MD144", "MD145", "MD146", "MD101", "MX004_R", "MX067_R", "MX060_R",
             "MB014", "MC001", "MB002", "MB028", "MB089M1M","MB085", "MLB037A",
             "MLB037B", "MLB037C", "MLB037D", "MLB037E", "MLB037F", "MLB037G",
             "MLB037K", "MLB037L", "MLB037M", "MLB037N"]
rename_col=["PN", "HHID", "AT1",  "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2",
             "CT3", "CT4", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "discrimination6", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
             "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7",
             "ctrauma1", "ctrauma2", "ctrauma3", "ctrauma4"
            ]
year=2010

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)

# YEAR 2012

# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/h12f3a.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()

needed_col=["PN", "HHID", "NLB037A", "NLB037B", "NLB037C", "NLB037D", "NLB037E",
             "NLB037F", "NLB037G", "NLB037K", "NLB037L", "NLB037M", "NLB037N",
             "NLB030A", "NLB030B", "NLB030C", "NLB030D", "NLB030E", "NLB030F",
             "NLB021A", "NLB021B", "NLB021C", "NLB021D", "NLB021E", "NLB021F",
             "NLB021G", "NLB021H", "ND174", "ND184", "ND122", "ND142", "ND143",
             "ND144", "ND145", "ND146", "ND101", "NX004_R", "NX067_R", "NX060_R",
             "NB014", "NC001", "NB002", "NB028", "NB089M1M","NB085", "NLB037A",
             "NLB037B", "NLB037C", "NLB037D", "NLB037E", "NLB037F", "NLB037G",
             "NLB037K", "NLB037L", "NLB037M", "NLB037N"]
rename_col=["PN", "HHID", "AT1",  "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2",
             "CT3", "CT4", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "discrimination6", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
             "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7",
             "ctrauma1", "ctrauma2", "ctrauma3", "ctrauma4"
            ]
year=2012

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)


# YEAR 2014
# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/h14f2b.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()


needed_col=["PN", "HHID", "OLB029A", "OLB029B", "OLB029C", "OLB029D",
             "OLB029E", "OLB029F", "OLB020A", "OLB020B", "OLB020C", "OLB020D",
             "OLB020E", "OLB020F", "OLB020G", "OLB020H", "OD174", "OD184", "OD122",
             "OD142", "OD143", "OD144", "OD145", "OD146", "OD101", "OX004_R",
             "OX067_R", "OX060_R", "OB014", "OC001", "OB002", "OB028", "OB089M1M",
             "OB085"]
rename_col=["PN", "HHID", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "discrimination6", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship"
            ]
year=2014

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)

# YEAR 2016

# Replace 'your_file.sav' with the path to your .sav file
file_path = '/content/h16f2c.sav'

# Read the .sav file with encoding
df, meta = pyreadstat.read_sav(file_path)
df.columns = df.columns.str.upper()


needed_col=["PN", "HHID", "PLB029A", "PLB029B", "PLB029C", "PLB029D",
             "PLB029E", "PLB029F", "PLB020A", "PLB020B", "PLB020C", "PLB020D",
             "PLB020E", "PLB020F", "PLB020G", "PLB020H", "PD174", "PD184", "PD122",
             "PD142", "PD143", "PD144", "PD145", "PD146", "PD101", "PX004_R",
             "PX067_R", "PX060_R", "PB014", "PC001", "PB002", "PB028", "PB089M1M",
             "PB085"]
rename_col=["PN", "HHID", "discrimination1", "discrimination2", "discrimination3",
             "discrimination4", "discrimination5", "discrimination6", "vandalism",
             "rubbish", "vacancy", "safety", "belonging", "trust", "friendliness",
             "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
             "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear",
             "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship"
            ]
year=2016

prefix={2006:'K',
        2008:'L',
        2010:'M',
        2012:'N',
        2014:'O',
        2016:'P'}


new_needed_col=[i for i in needed_col if not i.endswith('D122')]
rename_col.remove('backwardcount')

new_needed_col.append(prefix[year]+'D124')
rename_col.append('backwardcount-try1')
new_needed_col.append(prefix[year]+'D129')
rename_col.append('backwardcount-try2')

new_df=clean_df(df,new_needed_col,rename_col,year)
s='rand_'+str(year)+'_single_file_extract.csv'
new_df.to_csv(s, index=False)

# CONSOLIDATE 2006 TO 2016

clean_2006=pd.read_csv("/content/rand_2006_single_file_extract.csv")
clean_2008=pd.read_csv("/content/rand_2008_single_file_extract.csv")
clean_2010=pd.read_csv("/content/rand_2010_single_file_extract.csv")
clean_2012=pd.read_csv("/content/rand_2012_single_file_extract.csv")
clean_2014=pd.read_csv("/content/rand_2014_single_file_extract.csv")
clean_2016=pd.read_csv("/content/rand_2016_single_file_extract.csv")

temp=pd.concat([clean_2006, clean_2008,clean_2010,clean_2012,clean_2014,clean_2016], axis=0, ignore_index=True)
temp.to_csv("Merged_data_regenerate.csv",index=False)

