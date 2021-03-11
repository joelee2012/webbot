import pytest

from webbot.workflow import Task


class TestTask:

    def test_action_is_list(self):
        raw = {'name': 'fake task', 'click': ['xpath1', 'xpath2']}
        task = Task(dict(raw))
        assert task.name == raw['name']
        for index, action in enumerate(task):
            assert action.name == 'click'
            assert action.args == {'selector': 'xpath',
                                   'value': raw['click'][index]}

    def test_action_is_str(self):
        raw = {'name': 'fake task', 'click': 'xpath2'}
        task = Task(dict(raw))
        assert task.name == raw['name']
        assert task.actions[0].name == 'click'
        assert task.actions[0].args == {'selector': 'xpath',
                                        'value': raw['click']}

    def test_action_is_dict(self):
        raw = {'name': 'fake task', 'input': {
            'value': 'xpath2', 'text': 'abc'}}
        task = Task(dict(raw))
        assert task.name == raw['name']
        assert task.actions[0].name == 'input'
        assert task.actions[0].args == {'selector': 'xpath',
                                        'text': raw['input']['text'],
                                        'value': raw['input']['value']}
