from rest_framework import generics
from storage.models import Provider
from storage.serializers import ProviderSerializer
from rest_framework import viewsets


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

"""1. Создание нового провайдера:
def create_provider(name, email, phone):
    # Проверить, что провайдер с таким именем или электронной почтой не существует
    if Provider.objects.filter(Q(name=name) | Q(email=email)).exists():
        raise Exception("Provider with this name or email already exists")
    
    # Создание и сохранение нового провайдера в базе данных
    provider = Provider(name=name, email=email, phone=phone)
    provider.save()
    
    return provider


2. Получение информации о провайдере:
def get_provider(provider_id):
    # Найти провайдера по его идентификатору
    provider = Provider.objects.get(id=provider_id)
    
    return provider


3. Обновление информации о провайдере:
def update_provider(provider_id, data):
    # Найти провайдера по его идентификатору
    provider = Provider.objects.get(id=provider_id)
    
    # Обновление информации о провайдере
    provider.name = data.get('name', provider.name)
    provider.email = data.get('email', provider.email)
    provider.phone = data.get('phone', provider.phone)
    
    provider.save()


4. Получение списка услуг, предоставляемых провайдером:
def get_provider_services(provider_id):
    # Найти провайдера по его идентификатору
    provider = Provider.objects.get(id=provider_id)
    
    # Получение списка услуг, предоставляемых провайдером
    services = Service.objects.filter(provider=provider)
    
    return services


5. Создание новой услуги провайдера:
def create_service(provider_id, name, price):
    # Найти провайдера по его идентификатору
    provider = Provider.objects.get(id=provider_id)
    
    # Создание и сохранение новой услуги провайдера в базе данных
    service = Service(name=name, price=price, provider=provider)
    service.save()
    
    return service"""