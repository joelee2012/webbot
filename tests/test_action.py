import pytest
from webbot.action import new_action


class TestClickAction:

    name = 'click'

    @pytest.mark.parametrize('args', ['//abc',
                                      {'value': '//abc'},
                                      {'value': '//abc', 'selector': 'id'}])
    def test_correct_args(self, args):
        action = new_action(self.name, args)
        assert action.name == self.name
        if isinstance(args, str):
            expected = {'selector': 'xpath', 'value': args}
        else:
            expected = {'selector': 'xpath'}
            expected.update(args)
        assert action.args == expected

    @pytest.mark.parametrize('args, keyword', [({}, 'required'),
                                               ({'value': '//abc',
                                                 'unsupported': 'x'}, 'expects arguments'),
                                               ({'value': '//abc', 'selector': 'x'}, 'expects selectors')])
    def test_wrong_args(self, args, keyword):
        with pytest.raises(ValueError) as e:
            new_action(self.name, args)
        assert keyword in str(e.value)


class TestInputAction:
    name = 'input'

    @pytest.mark.parametrize('args', [{'value': '//abc', 'text': 'abc'},
                                      {'value': '//abc', 'text': 'abc', 'selector': 'id'}])
    def test_correct_args(self, args):
        action = new_action(self.name, args)
        assert action.name == self.name
        expected = {'selector': 'xpath'}
        expected.update(args)
        assert action.args == expected

    @pytest.mark.parametrize('args, keyword', [({}, 'required'),
                                               ({'value': '//abc', 'text': 'abc',
                                                 'unsupported': 'x'}, 'expects arguments'),
                                               ({'value': '//abc', 'text': 'abc', 'selector': 'x'}, 'expects selectors')])
    def test_wrong_args(self, args, keyword):
        with pytest.raises(ValueError) as e:
            new_action(self.name, args)
        assert keyword in str(e.value)


class TestSwitchWindow:
    name = 'switch_window'

    @pytest.mark.parametrize('args', ['1',
                                      {'index': 1},
                                      {'index': '1'}])
    def test_correct_args(self, args):
        action = new_action(self.name, args)
        assert action.name == self.name
        if isinstance(args, str):
            args = {'index': args}
        assert action.args == args

    @pytest.mark.parametrize('args', ['', 'a',
                                      {'index': ''},
                                      {'index': 'a'}])
    def test_wrong_args(self, args):
        with pytest.raises(ValueError) as e:
            a = new_action(self.name, args)
            print(a)
        print(e.value)
        assert 'expects int' in str(e.value)
