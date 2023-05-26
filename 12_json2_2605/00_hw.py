import requests as r

url = 'https://jsonplaceholder.typicode.com/todos'
response = r.get(url)  # пытаемся подключиться к серверу по адресу

print(response.status_code)  # проверить подключение

todos = response.json()  # преобразуем ответ сервера в словарь Python, чтобы с ним можно было работать
users_tasks = {}
for todo in todos:
    if todo['userId'] not in users_tasks:
        users_tasks[todo['userId']] = [0, 0]
    else:
        if todo['completed']:
            users_tasks[todo['userId']][0] += 1
        else:
            users_tasks[todo['userId']][1] += 1

print(users_tasks)
for user in users_tasks.keys():
    completed = users_tasks[user][0]
    not_completed = users_tasks[user][1]
    kpi = round(completed / (completed + not_completed) * 100, 2)
    print(f'ID: {user}\nCompleted: {completed}\nNot completed: {not_completed}\nKPI: {kpi}%')

