import re
import csv

phonenumber_pattern = r"(\+7|8)\s?\(?(\d{3})\)?(-|\s)?(\d{3})-?(\d{2})-?(\d{2})"
subnumber_pattern = r"\(?доб\.\s(\d+)\)?"
formatted_number = r"+7(\2)\4-\5-\6"
formatted_subnumber = r"доб.\1"

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = []
for contact in contacts_list[1:]:
    full_name = " ".join(contact[0:3])
    splitted_full_name = full_name.split(" ")
    phonenumber = contact[5]
    new_number = re.sub(phonenumber_pattern, formatted_number, phonenumber)   
    new_subnumber = re.sub(subnumber_pattern, formatted_subnumber, new_number)

    person = [
        splitted_full_name[0],
        splitted_full_name[1],
        splitted_full_name[2],
        contact[3],
        contact[4],
        new_subnumber,
        contact[6]
    ]
    new_contacts_list.append(person)
    
contacts_exist = {}
final_contacts_list = []
counter = 0
for contact in new_contacts_list:
    if contact[0] not in contacts_exist.keys():       
        contacts_exist[contact[0]] = counter
        counter += 1
        final_contacts_list.append(contact)      
    else:
        for i, data in enumerate(contact, start=0):
            if data != "":
                index = contacts_exist[contact[0]]
                final_contacts_list[index][i] = data

with open("phonebook.csv", "w", encoding="utf-8", newline = "") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)