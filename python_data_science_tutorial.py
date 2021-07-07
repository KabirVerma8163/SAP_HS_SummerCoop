import csv
import pprint
from collections import defaultdict, Counter

with open('/Users/toastedwaffle/Desktop/Datasets/developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    total = 0

    dev_type_info = {

    }

    for line in csv_reader:
        dev_types = line['DevType'].split(";")

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })

            languages = line['LanguageWorkedWith'].split(";")
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1

for dev_type, info in dev_type_info.items():
    print(f"{dev_type}")

    for language, value in info['language_counter'].most_common(5):
        language_pct = round((value * 100 / info['total']), 2)
        print(f"\t{language}: {language_pct}%")



'''
this is the code for finding out the most popular languages

with open('/Users/toastedwaffle/Desktop/Datasets/developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    total = 0
    total = 0

    languages_counter = Counter()
    for line in csv_reader:
        total += 1

        languages = line['LanguageWorkedWith'].split(";")
        languages_counter.update(languages)

# print(pprint.pprint(languages_counter))
print("Top 5 most commonly used languages in 2019:")
for language, value in languages_counter.most_common(5):
    language_pct = round((value * 100/total), 2)
    print(f"{language}: {language_pct}%")
'''




'''
This is the code for the basics, just learning about the hobbies and stuff
with open('/Users/toastedwaffle/Desktop/Datasets/developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    yes_hobby = 0
    no_hobby = 0
    total = 0

    hobby = {
        'Yes': 0,
        'No': 0,
    }
    # can be initialized as a default dictionary with hobby = defaultdict(int)
    # can also just do hobby = Counter()

    for line in csv_reader:
        total += 1
        # if line['Hobbyist'] == "Yes":
        #     yes_hobby += 1
        # elif line['Hobbyist'] == "No":
        #     no_hobby += 1

        hobby[line['Hobbyist']] += 1

        # print(pprint.pprint(line['Hobbyist']))
        # break


none_hobby = total - (no_hobby + yes_hobby)
#
# yes_hobby_percent = round(yes_hobby*100/total, 2)
# no_hobby_percent = round(no_hobby * 100 / total, 2)
# none_hobby_percent = round(none_hobby * 100 / total)

yes_hobby_percent = round(hobby['Yes']*100/total, 2)
no_hobby_percent = round(hobby['No'] * 100 / total, 2)
none_hobby_percent = round(none_hobby * 100 / total)
print(f"Total: {total} \n Yes: {yes_hobby} \n No: {no_hobby} \n None: {none_hobby}")
print(f"\n Percentages \n Yes: {yes_hobby_percent}% \n No: {no_hobby_percent}% \n None: {none_hobby_percent}%")
'''



