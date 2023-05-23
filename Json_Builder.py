import os
import sys
from content_block_functions import *
from question_block_functions import *
from question_object import *
import pandas as pd
import re
# 
#  ------ VARIABLES ------------------------------------
# Auszufüllen
name_of_json_file = "kickoff-one-v2"
journey_key = "Test_Short_Trip_Flora"
id = "flora-v"
version = str(15)
write_beginning = True
write_ending = True
etappe = "-1-"
startnumber = 1 # 1 if it should start from beginning
excel_path_or_name = "Jsons/Json Builder/Templates/Kick-Off Begleitung.xlsx"

# -------- EXPLANATIONS ----------
# type: CONTENT, OPTION_QUESTION, OPEN_QUESTION, SCALA_SLIDER, ITEM_LIST_EXPANDABLE (T OR C as answeroption), ITEM_LIST_SINGLE_CHOICE (R)
# content: P = Paragraph, R = Referenz, I = Image, A = Audio, M = More Information Expandable -> Titel ist immer dabei
# answer_option: R = Radio Button, C = Checkbox, T = Text_Field_Expandable
# next_logic_type: NEXT, NEXT_OPTION, REF_KEY_INSIGHT
# next_logic_options: N = option with next

# --------- TO DO --------------
# TODO: Einzelne Questions sind einzelne Objects die von Question erben
# TODO: Next_logic_type: Next_option -> bei nicht linearer json
# TODO: Schlüsselerk. referenz -> ref key insight muss ref_logik in der frage zuvor sein -> es muss ein next_question object mitgegeben werden
# TODO: Englisch text
# question_array = [Question('CONTENT','AM'),Question('SCALA_SLIDER','PRPM'), Question('OPTION_QUESTION','PRP'), Question('CONTENT'), Question('CONTENT'), Question('OPEN_QUESTION','PRP'), Question('SCALA_SLIDER'), Question('CONTENT','PR'), Question('OPEN_QUESTION','PRP'), Question('OPTION_QUESTION'), Question('CONTENT'), Question('CONTENT'), Question('CONTENT')]


# --------- EXCEL ---------

df = pd.read_excel(excel_path_or_name)

# set defaults and clean
if pd.isna(df.iloc[3,1]):
    df.iloc[3,1] = 'Beginne deinen Kurztrip'
# get first informations and delete them from the dataframe
information = df.iloc[:, 1]
# drop the first two columns
df = df.drop(df.columns[[0, 1]], axis=1)

# save always two arrays into the Question object with structure and texts respectively
questions_array = []
for i in range(0, len(df.columns), 2):
    questions_array.append(Question(df.iloc[:, i], df.iloc[:, i+1]))

# ---------- INTER QUESTION DEPENDENCIES ----------

# add next question references
# loop through and add reference backward
for i, question in enumerate(questions_array):
    for x, struct in enumerate(question.structure):
        # check if structure has reference
        if struct == 'REFERENCE':
            # check if key insight reference
            if question.texts[x].isupper():
                # add to question before
                questions_array[i-1].next_question_reference = question.texts[x]
                questions_array[i-1].next_logic_type = 'REF_KEY_INSIGHT'
    

# -------- TESTS --------

# Check if all information fields are there
for i,info in enumerate(information):
    if i > 6:
        break
    if pd.isna(info):
        raise Exception('There is some starting information missing')
    
formatting_flag = 0
    # Test: delete empty questions
for question in questions_array:
    if question.structure.size == 0:
        questions_array.remove(question)

for q_count, question in enumerate(questions_array):
    # Test 1: immer mit subtitle starten
    if not question.structure[0] == 'SUB_TITEL':
        raise Exception ('SUB_TITEL is missing for question ',q_count+1)
    # Test 2: kein item single und item multiple in einer frage 
    if 'ITEM(Multiple)' in question.structure and 'ITEM(Single)' in question.structure:
        raise Exception ('ITEM(Single) und ITEM(Multiple) gemischt in Frage: ', q_count+1)
    # Test more Information:
    if 'MORE_INFORMATION' in question.structure and not '_' in question.texts[np.where(question.structure == 'MORE_INFORMATION')][0]:
        raise Exception ('More information field is missing a title in Question:', q_count+1)
    # Test:
    for text in question.texts:
        if isinstance(text, str):
            if '<br>' in text or '<strong>' in text:
                formatting_flag = 1
    # Test empty Text
    needs_text_array = ['SUB_TITEL','PARAGRAPH','AUDIO', 'IMAGE', 'MORE_INFORMATION', 'MORE_INFORMATION_EXPANDED', 'ITEM(Single)', 'ITEM(Multiple)','SCALA']
    for i,text in enumerate(question.texts):
        # if nan
        if not isinstance(text, str):
            # if it needs some text
            if question.structure[i] in needs_text_array: #and not isinstance(question.structure[i], str):
                raise Exception ('There is a text field missing at question: ', q_count+1)
    
if formatting_flag == 0:
    raise Exception ('Not formatted')



# ---------- TEXT FORMATIERUNG ---------
for question in questions_array:
    for i, text in enumerate(question.texts):
        if not pd.isnull(text):
            # find " and replace with \"
            # find breaks and delete them
            question.texts[i] = text.replace('"', '\\"').replace('\n', '')

# ---------- PROGRESS -------
number_questions = len(questions_array)
progress_steps = round(90/number_questions)
progress = progress_steps
for question in questions_array:
    question.progress = progress
    progress += progress_steps


# -------- WRITE FILE -------------------------------------

with open(os.path.join(sys.path[0], name_of_json_file+".json"), 'w+') as file:

    # BEGINNING
    if write_beginning:    
        file.write(create_beginning(id, version, journey_key, information))

    for count, question in enumerate(questions_array): 
        id_base = id+version+etappe+str(startnumber+count)
        id_base_next_question = id+version+etappe+str(startnumber+count+1)   

        # WRITE & remove comma for the last entry
        if count == (len(questions_array)-1):
            file.write(create_question(question, id_base, count, write_beginning, id_base_next_question)[:-1])
        else:
            file.write(create_question(question, id_base, count, write_beginning, id_base_next_question))

    # ENDING
    if write_ending:   
        file.write('''
      ],
      "questionLoops": []
    }
  ]
}
        '''
        )


printie = ('''JIPIIEE - 
ITS DONE''')
print(printie)