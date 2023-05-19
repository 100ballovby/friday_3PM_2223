import requests as r

url = 'https://jsonplaceholder.typicode.com/todos'
response = r.get(url)  # пытаемся подключиться к серверу по адресу

print(response.status_code)  # проверить подключение

todos = response.json()  # преобразуем ответ сервера в словарь Python, чтобы с ним можно было работать
user9_count = 0
incompl = 0
for todo in todos:
    print(f'ID: {todo["id"]}, User: {todo["userId"]}, Done: {todo["completed"]}')
    print(f'Raw: {todo}')
    if todo['userId'] == 2 and todo['completed'] == False:
        user9_count += 1
    if not todo['completed']:
        incompl += 1

print(f'User with id 2 has {user9_count} incompleted tasks.')
print(f'{incompl} tasks has not completed')
completed_perc = int((incompl / len(todos)) * 100)
print(f'{completed_perc} percent of completed tasks')

