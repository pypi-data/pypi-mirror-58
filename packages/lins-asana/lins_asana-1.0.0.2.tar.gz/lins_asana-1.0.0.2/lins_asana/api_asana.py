import json
import requests


class ApiAsana:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Accept': '/',
            'Accept-Encoding': 'gzip, deflate',
            'Authorization': token,
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

    def get_workspaces(self) -> list:
        url = f'{self.base_url}/workspaces'
        response = requests.get(url=url, headers=self.headers)
        return json.loads(response.text).get('data', [])

    def get_teams(self, workspace) -> list:
        url = f'{self.base_url}/organizations/{workspace}/teams'
        response = requests.get(url=url, headers=self.headers)
        return json.loads(response.text).get('data', [])

    def get_projects(self, worspace, team) -> list:
        url = f'{self.base_url}/projects'
        params = {
            'workspace': worspace,
            'team': team
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return json.loads(response.text).get('data', [])

    def get_tasks(self, project='') -> list:
        url = f'{self.base_url}/tasks'
        params = {
            'project': project
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return json.loads(response.text).get('data', [])

    def get_task_by_id(self, task_gid) -> dict:
        url = f'{self.base_url}/tasks/{task_gid}'
        response = requests.get(url=url, headers=self.headers)
        return json.loads(response.text).get('data', {})

    def get_events(self, resource, sync='') -> tuple:
        url = f'{self.base_url}/events'
        params = {
            'resource': resource,
            'sync': sync
        }
        response = requests.get(url, params=params, headers=self.headers)
        obj = json.loads(response.text)
        return obj.get('data', []), obj.get('sync', '')
