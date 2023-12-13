# Ensure needed columns and mapping columns are complete in below 'mapping_dict'
import os.path

start_year = 2006
end_year = 2016

file_path_2006 = 'content/h06f4a.sav'
file_path_2008 = 'content/h08f3a.sav'
file_path_2010 = 'content/hd10f6a.sav'
file_path_2012 = 'content/h12f3a.sav'
file_path_2014 = 'content/h14f2b.sav'
file_path_2016 = 'content/h16f2c.sav'

needed_col_2006 = ["PN", "HHID", "KLB037A", "KLB037B", "KLB037C", "KLB037D", "KLB037E", "KLB037F", "KLB037G",
                   "KLB037H", "KLB037I", "KLB037J", "KLB030A", "KLB030B", "KLB030C", "KLB030D", "KLB030E",
                   "KLB021A", "KLB021B", "KLB021C", "KLB021D", "KLB021E", "KLB021F", "KLB021G", "KLB021H",
                   "KD174", "KD184", "KD122", "KD142", "KD143", "KD144", "KD145", "KD146", "KD101", "KX004_R",
                   "KX067_R", "KX060_R", "KB014", "KC001", "KB002", "KB028", "KB089M1M", "KB085", "KLB037A",
                   "KLB037B", "KLB037C", "KLB037D", "KLB037E", "KLB037F", "KLB037G", "KLB037H", "KLB037I","KLB037J"]
needed_col_2008 = ["PN", "HHID", "LLB037A", "LLB037B", "LLB037C", "LLB037D", "LLB037E", "LLB037F", "LLB037G",
                   "LLB037K", "LLB037L", "LLB037M", "LLB037N", "LLB030A", "LLB030B", "LLB030C", "LLB030D",
                   "LLB030E", "LLB030F", "LLB021A", "LLB021B", "LLB021C", "LLB021D", "LLB021E", "LLB021F",
                   "LLB021G", "LLB021H", "LD174", "LD184", "LD122", "LD142", "LD143", "LD144", "LD145", "LD146",
                   "LD101", "LX004_R", "LX067_R", "LX060_R", "LB014", "LC001", "LB002", "LB028", "LB089M1M",
                   "LB085", "LLB037A", "LLB037B", "LLB037C", "LLB037D", "LLB037E", "LLB037F", "LLB037G",
                   "LLB037K", "LLB037L", "LLB037M", "LLB037N"]
needed_col_2010 = ["PN", "HHID", "MLB037A", "MLB037B", "MLB037C", "MLB037D", "MLB037E", "MLB037F", "MLB037G",
                   "MLB037K", "MLB037L", "MLB037M", "MLB037N", "MLB030A", "MLB030B", "MLB030C", "MLB030D",
                   "MLB030E", "MLB030F", "MLB021A", "MLB021B", "MLB021C", "MLB021D", "MLB021E", "MLB021F",
                   "MLB021G", "MLB021H", "MD174", "MD184", "MD122", "MD142", "MD143", "MD144", "MD145", "MD146",
                   "MD101", "MX004_R", "MX067_R", "MX060_R", "MB014", "MC001", "MB002", "MB028", "MB089M1M",
                   "MB085", "MLB037A", "MLB037B", "MLB037C", "MLB037D", "MLB037E", "MLB037F", "MLB037G",
                   "MLB037K", "MLB037L", "MLB037M", "MLB037N"]
needed_col_2012 = ["PN", "HHID", "NLB037A", "NLB037B", "NLB037C", "NLB037D", "NLB037E", "NLB037F", "NLB037G",
                   "NLB037K", "NLB037L", "NLB037M", "NLB037N", "NLB030A", "NLB030B", "NLB030C", "NLB030D",
                   "NLB030E", "NLB030F", "NLB021A", "NLB021B", "NLB021C", "NLB021D", "NLB021E", "NLB021F",
                   "NLB021G", "NLB021H", "ND174", "ND184", "ND122", "ND142", "ND143", "ND144", "ND145", "ND146",
                   "ND101", "NX004_R", "NX067_R", "NX060_R", "NB014", "NC001", "NB002", "NB028", "NB089M1M",
                   "NB085", "NLB037A", "NLB037B", "NLB037C", "NLB037D", "NLB037E", "NLB037F", "NLB037G",
                   "NLB037K", "NLB037L", "NLB037M", "NLB037N"]
needed_col_2014 = ["PN", "HHID", "OLB029A", "OLB029B", "OLB029C", "OLB029D", "OLB029E", "OLB029F", "OLB020A",
                   "OLB020B", "OLB020C", "OLB020D", "OLB020E", "OLB020F", "OLB020G", "OLB020H", "OD174",
                   "OD184", "OD122", "OD142", "OD143", "OD144", "OD145", "OD146", "OD101", "OX004_R", "OX067_R",
                   "OX060_R", "OB014", "OC001", "OB002", "OB028", "OB089M1M", "OB085"]
needed_col_2016 = ["PN", "HHID", "PLB029A", "PLB029B", "PLB029C", "PLB029D", "PLB029E", "PLB029F", "PLB020A",
                   "PLB020B", "PLB020C", "PLB020D", "PLB020E", "PLB020F", "PLB020G", "PLB020H", "PD174",
                   "PD184", "PD122", "PD142", "PD143", "PD144", "PD145", "PD146", "PD101", "PX004_R", "PX067_R",
                   "PX060_R", "PB014", "PC001", "PB002", "PB028", "PB089M1M", "PB085"]

rename_col_2006 = ["PN", "HHID", "AT1", "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT3", "CT4",
                   "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "vandalism", "rubbish", "vacancy", "safety", "belonging", "trust",
                   "friendliness", "help", "immediate10", "delayed10", "backwardcount", "serial1", "serial2",
                   "serial3", "serial4", "serial5", "selfmemory", "birthmonth", "birthyear", "sex", "education",
                   "genhealth", "USborn", "hispanic", "race", "citizenship", "trauma1", "trauma2", "trauma3",
                   "trauma4", "trauma5", "trauma6", "trauma7", "ctrauma1", "ctrauma3", "ctrauma4"]
rename_col_2008 = ["PN", "HHID", "AT1", "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2", "CT3", "CT4",
                   "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "discrimination6", "vandalism", "rubbish", "vacancy", "safety",
                   "belonging", "trust", "friendliness", "help", "immediate10", "delayed10", "backwardcount",
                   "serial1", "serial2", "serial3", "serial4", "serial5", "selfmemory", "birthmonth",
                   "birthyear", "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
                   "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7", "ctrauma1",
                   "ctrauma2", "ctrauma3", "ctrauma4"]
rename_col_2010 = ["PN", "HHID", "AT1", "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2", "CT3", "CT4",
                   "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "discrimination6", "vandalism", "rubbish", "vacancy", "safety",
                   "belonging", "trust", "friendliness", "help", "immediate10", "delayed10", "backwardcount",
                   "serial1", "serial2", "serial3", "serial4", "serial5", "selfmemory", "birthmonth",
                   "birthyear", "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
                   "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7", "ctrauma1",
                   "ctrauma2", "ctrauma3", "ctrauma4"]
rename_col_2012 = ["PN", "HHID", "AT1", "AT2", "AT3", "AT4", "AT5", "AT6", "AT7", "CT1", "CT2", "CT3", "CT4",
                   "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "discrimination6", "vandalism", "rubbish", "vacancy", "safety",
                   "belonging", "trust", "friendliness", "help", "immediate10", "delayed10", "backwardcount",
                   "serial1", "serial2", "serial3", "serial4", "serial5", "selfmemory", "birthmonth",
                   "birthyear", "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship",
                   "trauma1", "trauma2", "trauma3", "trauma4", "trauma5", "trauma6", "trauma7", "ctrauma1",
                   "ctrauma2", "ctrauma3", "ctrauma4"]
rename_col_2014 = ["PN", "HHID", "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "discrimination6", "vandalism", "rubbish", "vacancy", "safety",
                   "belonging", "trust", "friendliness", "help", "immediate10", "delayed10", "backwardcount",
                   "serial1", "serial2", "serial3", "serial4", "serial5", "selfmemory", "birthmonth",
                   "birthyear", "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship"]
rename_col_2016 = ["PN", "HHID", "discrimination1", "discrimination2", "discrimination3", "discrimination4",
                   "discrimination5", "discrimination6", "vandalism", "rubbish", "vacancy", "safety",
                   "belonging", "trust", "friendliness", "help", "immediate10", "delayed10", "backwardcount",
                   "serial1", "serial2", "serial3", "serial4", "serial5", "selfmemory", "birthmonth",
                   "birthyear", "sex", "education", "genhealth", "USborn", "hispanic", "race", "citizenship"]

mapping_dict_proper = {2006: {'prefix': 'K', 'needed_col': needed_col_2006, 'rename_col': rename_col_2006, 'file': file_path_2006},
                2008: {'prefix': 'L', 'needed_col': needed_col_2008, 'rename_col': rename_col_2008, 'file': file_path_2008},
                2010: {'prefix': 'M', 'needed_col': needed_col_2010, 'rename_col': rename_col_2010, 'file': file_path_2010},
                2012: {'prefix': 'N', 'needed_col': needed_col_2012, 'rename_col': rename_col_2012, 'file': file_path_2012},
                2014: {'prefix': 'O', 'needed_col': needed_col_2014, 'rename_col': rename_col_2014, 'file': file_path_2014},
                2016: {'prefix': 'P', 'needed_col': needed_col_2016, 'rename_col': rename_col_2016, 'file': file_path_2016}}

mapping_dict = {2006: {'prefix': 'K', 'needed_col': needed_col_2006, 'rename_col': rename_col_2006, 'file': file_path_2006},
                2008: {'prefix': 'L', 'needed_col': needed_col_2008, 'rename_col': rename_col_2008, 'file': file_path_2008},
                2010: {'prefix': 'K', 'needed_col': needed_col_2006, 'rename_col': rename_col_2006, 'file': file_path_2010},
                2012: {'prefix': 'L', 'needed_col': needed_col_2008, 'rename_col': rename_col_2008, 'file': file_path_2012},
                2014: {'prefix': 'K', 'needed_col': needed_col_2006, 'rename_col': rename_col_2006, 'file': file_path_2014},
                2016: {'prefix': 'L', 'needed_col': needed_col_2008, 'rename_col': rename_col_2008, 'file': file_path_2016}}

# Validate if mapping dict is complete
for year in range(start_year, end_year+1, 2):
    if year not in mapping_dict:
        raise ValueError(f'mapping dict incomplete for {year}')

# Validate if all source files exist
for year in range(start_year, end_year + 1, 2):
    file = mapping_dict[year]['file']
    if not os.path.exists(file):
        raise ValueError(f'file does not exist: {file}')


