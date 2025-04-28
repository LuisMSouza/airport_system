from .celery import app as celery_app

# Este trecho é necessário para que o Celery possa descobrir as tarefas definidas em cada aplicativo Django.
# Isso permite que o Celery encontre automaticamente as tarefas definidas em cada aplicativo.
__all__ = ('celery_app',)