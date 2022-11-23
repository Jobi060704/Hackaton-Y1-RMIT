"""
Testing data:

0
345896
- all work orders starting with 345896

2
Left Qtr Panel
- all records of Left Qtr Panel part present

3
FRONT
- all records of tools being placed in the front
"""

import json, os


# function to search the multi-array
def search_base(req, att_sel, data):

    exact_sugg = []
    part_sugg = []

    for f in data:

        for i in f:
            if str(i[att_sel]) == str(req):
                exact_sugg.append(i)

        for i in f:
            if str(i[att_sel]).find(str(req)) != -1:
                part_sugg.append(i)


    return exact_sugg, part_sugg


# function to print all respectable findings
def print_res(data,att_lst,typ):
    print(f"Displaying findings for {typ} results")
    for i in data:
        print(f"Index: {i['Index']}")
        for j in att_lst:
            print(f"\t{j}: {i[j]}")
        print()


# get all .json files in folder
filepaths = os.listdir()
corrpath = []
for i in range(len(filepaths)):
    if filepaths[i][-4:] == 'json':
        corrpath.append(filepaths[i])


# store all PartInfomation data to an array
all_data = []
for i in corrpath:
    with open(i) as data_file: full_data = json.load(data_file)["PartInformation"]
    all_data.append(full_data)


# get option and keyword for search
att_lst = list(full_data[0].keys())[1:]
print("Please select the attribute (with num option) to search with:")

cnt = -1
for i in att_lst:
    cnt +=1
    print(f"\t{cnt} - {i}")

inp = int(input("\nSelection: "))

try:
    att_sel = att_lst[inp]
except:
    print("Wrong selection!")
    exit()

req = str(input("Please select the keyword to search for the data: "))



# seach for exact and similar data in the multiarray
ret_ext, ret_part = search_base(req, att_sel, all_data)
typ_ext = "exact"
typ_part = "partial"
print(ret_part)


# selective print of results
print()
if ret_ext == [] and ret_part == []:
    print("No matches!\n")
    exit()
elif ret_part == []:
    print("No partial matches, displaying exact results\n")
    print_res(ret_ext,att_lst,typ_ext)
elif ret_ext == []:
    print("No exact matches, displaying partial results\n")
    print_res(ret_part,att_lst,typ_part)
else:
    print("Both partial and exact results found, displaying all results\n")
    print_res(ret_ext,att_lst,typ_ext)
    print_res(ret_part,att_lst,typ_part)
