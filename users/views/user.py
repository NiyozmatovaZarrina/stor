from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""1. Регистрация пользователя:
def register_user(username, password, email):
    # Проверить, что пользователь с таким именем пользователя или адресом электронной почты не существует
    if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        raise Exception("User with this username or email already exists")
    
    # Создание и сохранение нового пользователя в базе данных
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    
    return user


2. Аутентификация пользователя:
def authenticate_user(username, password):
    # Найти пользователя по имени пользователя или адресу электронной почты
    user = User.objects.filter(Q(username=username) | Q(email=username)).first()
    
    # Проверка правильности пароля пользователя
    if user is not None and user.check_password(password):
        return user
    
    return None


3. Получение профиля пользователя:
def get_user_profile(user_id):
    # Найти пользователя по его идентификатору
    user = User.objects.get(id=user_id)
    
    # Получить профиль пользователя
    profile = user.profile
    
    return profile


4. Обновление профиля пользователя:
def update_user_profile(user_id, data):
    # Найти пользователя по его идентификатору
    user = User.objects.get(id=user_id)
    
    # Обновить данные профиля пользователя
    user.profile.name = data.get('name', user.profile.name)
    user.profile.age = data.get('age', user.profile.age)
    user.profile.address = data.get('address', user.profile.address)
    
    user.profile.save()

"""