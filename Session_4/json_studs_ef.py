# -*- coding: utf-8 -*-


# json module for outputting
import json
import urllib

# read in raw text from url
link = "https://raw.githubusercontent.com/albop/modern_scientific_programming/master/Students/students.md"
url_req = urllib.request.urlopen(link)
full_text = url_req.read().decode()

## read in raw text from local file
#with open("D:\emanu\OneDrive\Git\modern_scientific_programming\Students\students.md", "r") as read_in:
#    full_text = read_in.read()

# split according to MD syntax
# outputs a list of strings w/
# all students' blocks 
stud_list = full_text.split("## ")
                            
raw_list = list()

for i in range(1,len(stud_list)):
    # probably better create a function for dict's keys
    temp = {'identifier': stud_list[i].split("- identifier:")[1].splitlines()[0],
                        'email' : stud_list[i].split("- email:")[1].splitlines()[0],
                        'last name' : stud_list[i].split("- last name:")[1].splitlines()[0],
                        'first name' : stud_list[i].split("- first name:")[1].splitlines()[0],
                        'OS' : stud_list[i].split("- operating system:")[1].splitlines()[0],
                        'memory' : stud_list[i].split("- memory:")[1].splitlines()[0],
                        'RI' : stud_list[i].split("- research interest:")[1].splitlines()[0],
                        'Expectations' : stud_list[i].split("- expectations:")[1].splitlines()[0]
                        }
    raw_list.append(temp)


# output: use again shorthand of 'open'
with open('student_list.json', 'w') as outfile:
    json.dump(raw_list, outfile)