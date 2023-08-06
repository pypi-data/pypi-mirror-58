O que há neste pacote?
============

Classe para uso da API Asana.

Métodos Disponíveis:
------------

- get_workspaces(fields: list = []) -> list
- get_teams(workspace, fields: list = []) -> list
- get_projects(worspace, team, fields: list = []) -> list
- get_tasks(project, fields: list = []) -> list:
- get_task_by_id(task_gid, fields: list = []) -> dict
- patch_task(task_gid: int, data: dict) -> tuple
- get_events(resource, sync='') -> tuple
- get_webhooks(workspace: int, fields: list = []) -> list
- post_webhook(resource: int, target: str) -> bool

Exemplo de uso:
------------
```python
from lins_asana.api_asana import ApiAsana

api = ApiAsana(url='https://app.asana.com/api/1.0', token='1a1sd1as23d1as56d15615')

projects = api.get_projects(worspace=1231515961915181, team=1516519663541896)

## ... Do something with projects... ##
```

