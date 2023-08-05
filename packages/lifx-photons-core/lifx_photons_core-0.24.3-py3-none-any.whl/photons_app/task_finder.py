"""
Responsible for finding tasks and executing them
"""

from photons_app.actions import available_actions, all_tasks
from photons_app.errors import BadTask

from delfick_project.norms import sb


class TaskFinder(object):
    def __init__(self, collector):
        self.tasks = all_tasks
        self.collector = collector

    async def task_runner(self, task, **kwargs):
        target = sb.NotSpecified
        if ":" in task:
            target, task = task.split(":", 1)

        if task not in self.tasks:
            raise BadTask("Unknown task", task=task, available=sorted(list(self.tasks.keys())))

        return await self.tasks[task].run(
            target, self.collector, available_actions, self.tasks, **kwargs
        )
