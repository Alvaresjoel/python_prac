import datetime
import re 
def create_reminder(task_name,task_time):
    try:
        if datetime.datetime.strptime(task_time, "%H:%M"):
            task_date = datetime.datetime.now().date()
            print(f'Reminder set for {task_name} at {task_time} on {task_date}')
            # with open('remainder.csv')
        else :
            raise Exception('Invalid time format')

    except TypeError as t:
        raise t
    except Exception as e:
        raise e
try:
    create_reminder("123","12765:23")
except TypeError as t :
    print(t)
except Exception as e :
    print(e)