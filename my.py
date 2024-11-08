from lesson_3 import UserService, User

user = UserService()

user_service = User(name='Nicxai', email='nicxai@gmail.com', age=15)
user.add_user(user_service)

find = user.find_user_by_email(user_service.email)
if find:
    print(f'Найден: {find.name}  {find.email}  {find.age}')

user.delete_user('nicxai@gmail.com')