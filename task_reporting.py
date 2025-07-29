from datetime import datetime,date
tasks = [
    {
        "task_id": 1,
        "user_id": "2",
        "description": "assignment",
        "deadline": "2025-07-31",
        "status": "Pending"
    },
    {
        "task_id": 2,
        "user_id": "3",
        "description": "project proposal",
        "deadline": "2025-08-05",
        "status": "In Progress"
    },
    {
        "task_id": 3,
        "user_id": "4",
        "description": "final report submission",
        "deadline": "2025-08-10",
        "status": "Pending"
    },
    {
        "task_id": 4,
        "user_id": "2",
        "description": "code review",
        "deadline": "2025-07-30",
        "status": "Completed"
    },
    {
        "task_id": 5,
        "user_id": "5",
        "description": "design mockups",
        "deadline": "2025-07-28",
        "status": "In Progress"
    }
]

def completed_task(task_json) -> list :
    completed_task_list = []
    for task in task_json:
        status = task["status"]
        if status == 'Completed':
            completed_task_list.append(task)
    return completed_task_list


def pending_task (task_json) -> list :
    pending_task = []
    for task in task_json:
        status = task["status"]
        if status == 'Pending':
            pending_task.append(task)
    return pending_task


def task_due(task_json) -> dict:
    today = date.today()
    print(today)
    due_task = []
    for task in task_json:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        if today == deadline:
            due_task.append(task)
    return due_task


def overdue(task_json) -> list:
    overdue = []
    today = datetime.now()
    due_date_past = 0
    for task in task_json:
        date_object = datetime.strptime(task["deadline"], "%Y-%m-%d")
        due_date_past = (date_object - today).days
        if due_date_past < 0:
            overdue.append(task)
    return overdue


def average_days (task_json) -> int :
    average_days = 0
    no_task = 0
    today = datetime.now()
    for task in task_json:
        if task["status"] == 'Pending':
            no_task += 1
            date_object = datetime.strptime(task["deadline"], "%Y-%m-%d")
            due_date_past = (date_object - today).days
            average_days += due_date_past
    average_days = average_days/no_task
    return average_days

print("Completed Tasks:", completed_task(tasks))
print("Pending Tasks:", pending_task(tasks))
print("Tasks Due Today:", task_due(tasks))
print("Overdue Tasks:", overdue(tasks))
print("Average Days for Pending Tasks:", average_days(tasks))