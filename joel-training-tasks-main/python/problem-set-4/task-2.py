import json

def check_json():
    try:
        with open('students.json','r') as read_json:
            student_json_data = json.load(read_json)
    except json.decoder.JSONDecodeError as j:
        raise j
    except FileNotFoundError as f:
        # print(f)
        raise f
    else:
        return student_json_data

try:
    student_list = check_json()
    if len(student_list) == 0:
        raise Exception ('Empty Dictionery')
    for items in student_list:
        if not isinstance(items["name"],str) or not isinstance(items["marks"],int):
            raise TypeError
        print(f'{items["name"]} - {items["marks"]} marks')
except json.decoder.JSONDecodeError as j:
    print("Invalid json format",j )
except FileNotFoundError as f:
    print("File Not found",f)
except TypeError:
    print("Invalid input ")
except Exception as e:
    print(e)
