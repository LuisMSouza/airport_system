import os
from celery import Celery

# Este trecho é necessário para que o Celery possa descobrir as configurações do Django.
# Ele deve ser executado antes de qualquer outra coisa no arquivo.
# Isso garante que o Django esteja configurado corretamente antes de inicializar o Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airport_sistem.settings')

# Cria uma instância do Celery.
app = Celery('airport_sistem')
# Carrega as configurações do Django.
# O namespace 'CELERY' é usado para que o Celery possa encontrar as configurações específicas do Celery no arquivo de configurações do Django.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Carrega as tarefas de todos os aplicativos Django instalados.
# Isso permite que o Celery descubra automaticamente as tarefas definidas em cada aplicativo.
app.autodiscover_tasks()
