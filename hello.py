# import required python packages

import datetime
import os
import pandas as pd

username = input("Enter your name:")
condition = input("Are you sober or drunk?")

# load a sample paragraph
para = "The quick brown fox jumps over the lazy dog"

ask user to press key in order to begin the typing test
def display_text():
    keypress = input("Press C to display typing test:")
    return keypress

keypress = display_text()
# in case user presses the wrong key, add recursion to prompt user to type in the right key
while keypress!='C':
    keypress = display_text()

# add start time marker
start_time = datetime.datetime.now()
typed = input("Type the paragraph:")
# add end time marker
end_time = datetime.datetime.now()
# get the value in seconds
seconds = (end_time - start_time).total_seconds()
# print(seconds)

# store result in text file for multiple trials
text_path = "E:\\Documents\\talks\\webinar_py_research_labs\\programs\\venv1\\"+condition+"\\"+username+".txt"

# check if text file to store the data exists already. if not, create new file

if os.path.exists(text_path):
    open(text_path,'a').close()

# write seconds to text file. use str() method to convert from float to string
with open(text_path,'a') as f:
    f.write(str(seconds)+"\n")

# read data from .txt file and convert to excel report
# pandas dataframe is a row x col datastructure. Usually, it follows the below notation:
# row_1 = [col1,col2]
# row_2 = [col1,col2]
# dataframe = [row_1,row_2]

row = [username,condition]
with open(text_path,'r') as f:
   data = f.readlines() # this will return a python list where each line is a list element
   for i in data:
   		column = i.strip() # to remove trailing characters & delimiters like \n
        row.append(column)


data_list = [row]
df = pd.DataFrame(data_list,columns=["subject_name","condition","trial_1"])
# make sure excel file is already created in local
df.to_excel("E:\\Documents\\talks\\webinar_py_research_labs\\programs\\venv1\\download_report.xlsx") 