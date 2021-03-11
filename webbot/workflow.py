from .action import new_action
import copy


class Task:

    def __init__(self, raw):
        if 'name' not in raw:
            raise ValueError(f'name for task is required: {raw}')
        self.raw = copy.deepcopy(raw)
        self.name = self.raw.pop('name')
        self.actions = []
        self.parse()

    def parse(self):
        for action, args in self.raw.items():
            if not args:  # for action does not require args
                args = {}
            if not isinstance(args, (str, dict, list)):
                args = str(args)
            getattr(self, f'_parse_{type(args).__name__}')(action, args)

    def _parse_str(self, action, args):
        self.actions.append(new_action(action, args))

    def _parse_dict(self, action, args):
        self.actions.append(new_action(action, args))

    def _parse_list(self, action, args):
        for arg in args:
            self._parse_str(action, arg)

    def __getattr__(self, name):
        return self.raw[name]

    def __iter__(self):
        yield from self.actions

    def __str__(self):
        return f'<{type(self).__name__}: {self.name}>'


class WorkFlow:
    def __init__(self, raw):
        self.raw = raw
        self.tasks = []

    def parse(self):
        for task in self.raw['tasks']:
            self.tasks.append(Task(task))

    def __iter__(self):
        yield from self.tasks

    def __getattr__(self, name):
        return self.raw[name]

    def __str__(self):
        return f'<{type(self).__name__}: {self.name}>'
