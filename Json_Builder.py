import os
import pandas as pd
import openpyxl
from trip_object import Trip
from datetime import datetime
# 
#  ------ VARIABLES ------------------------------------
# Fill in:
name_of_json_file = str(datetime.now().strftime("%y_%m_%d_")) + "Entscheidungsmatrix" # name with which you want to save the Json
journey_key = "TEST_SHORT_TRIP_FLORA" # test key or Key of Journey
id_base = "flora-" # id base -> for testing e.g. your name, for the app the journey_key in small letters
version = "v"+str(93) # version of the json 90
write_beginning = True # False if you want to add to an existing json
write_ending = True # False if you want to add to an existing json
etappe = 1 # usually 1 except you want to add to an existing json in a different etappe
startnumber = 1 # usually 1 except you want to add to an existing json at a different screen number
excel_path_or_name = "/Users/flora.latz/Library/Mobile Documents/com~apple~CloudDocs/Dokumente/Arbeit/Onesome/Coding/Jsons/Excels/Json_Excel_Entscheidungsmatrix.xlsx" # path to the exel template
save_directory = '/Users/flora.latz/Library/Mobile Documents/com~apple~CloudDocs/Dokumente/Arbeit/Onesome/Coding/Jsons/Created' # path where you want to save the jsons
english_translation = False # is the english translation column filled?
starts_in_the_middle_of_etappe = False # does the excel start with e.g. 3.8 instead of 3.1?
nummeration_is_not_correct = True # if nummeration is not correct because 3.8 is followed by 3.10 instead of 3.9 (be aware that 3.8 needs a 'weiter mit screen' then)

# --------- EXCEL ---------

# check if path exists
if not os.path.exists(excel_path_or_name):
    raise Exception ('Excel path does not exist: ', excel_path_or_name)

# Load the Excel file
workbook = openpyxl.load_workbook(excel_path_or_name)
sheet = workbook.worksheets[0]

# Convert the sheet data to a list of lists
data = sheet.values
data_list = list(data)

# Create a DataFrame from the list of lists
df = pd.DataFrame(data_list)

# set first row as heading
df.columns = df.iloc[0]
df = df.iloc[1:].reset_index(drop=True)

# convert all entries to strings
df = df.astype(str)


# ---------- CREATE QUESTIONS -----------------

trip = Trip(df, id_base, version, write_beginning, write_ending, journey_key, english_translation, etappe, starts_in_the_middle_of_etappe, nummeration_is_not_correct)

# -------- WRITE FILE -------------------------------------

with open(os.path.join(save_directory, name_of_json_file+".json"), 'w+') as file:
    file.write(trip.json)


printie = ('''JIPIIEE - 
ITS DONE''')
print(printie)