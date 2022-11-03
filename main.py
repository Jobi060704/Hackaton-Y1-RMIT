import json


def search_base(req, att_sel, data):

    # exact matching
    exact_sugg = []
    for i in data:
        if str(i[att_sel]) == str(req):
            exact_sugg.append(i)

    # partial matching
    part_sugg = []
    for i in data:
        if str(i[att_sel]).find(str(req)) != -1:
            part_sugg.append(i)


    return exact_sugg, part_sugg


def print_res(data,att_lst):
    
    for i in data:
        print(f"Index: {i['Index']}")
        for j in att_lst[1:]:
            print(f"\t{j}: {i[j]}")
        print()



with open('AC2-07337-anon.json') as data_file: data = json.load(data_file)

att_lst = list(data["PartInformation"][0].keys())

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




ret_ext, ret_part = search_base(req,att_sel,data["PartInformation"])

if ret_ext == [] and ret_part == []:
    print("No matches!\n")
    exit()
elif ret_part == []:
    print("No partial matches, displaying exact results\n")
    print_res(ret_ext,att_lst)
elif ret_ext == []:
    print("No exact matches, displaying partial results\n")
    print_res(ret_part,att_lst)
else:
    print_res(ret_ext,att_lst)
    print_res(ret_part,att_lst)
