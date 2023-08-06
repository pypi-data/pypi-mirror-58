O que há neste pacote?
============

Classe para uso da API Asana.

Métodos Disponíveis:
------------

- get_workspaces -> list
- get_teams(self, workspace) -> list
- get_projects(self, worspace, team) -> list
- get_tasks(self, project) -> list:
- get_task_by_id(self, task_gid) -> dict
- get_events(self, resource, sync='') -> tuple

Exemplo de uso:
------------
```python
from lins_asana import ApiAsana

api = ApiAsana(url='https://app.asana.com/api/1.0', token='1a1sd1as23d1as56d15615')

projects = api.get_projects(worspace=1231515961915181, team=1516519663541896)

## ... Do something with projects... ##
```

