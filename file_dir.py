import os
from datetime import datetime


path = "C:\dir_project"

time = os.path.getmtime(path)


for file in os.listdir(path):
    if file.endswith(".txt"):
        mod_date = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file)))       
        print(os.path.join(path, file),mod_date)



#print("These are the text files and when they were last modified: {} \n{}".format(dir_list, time))
