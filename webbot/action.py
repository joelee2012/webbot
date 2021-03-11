class BaseAction:

    schema = {"required": ["value", "text"],
              "optional": {"selector": "xpath"}}
    selectors = ('xpath', 'css', 'id', 'name', 'link_text', 'tag_name',
                 'class_name', 'css_selector', 'partial_link_text')

    def __init__(self, args):
        self.args = self.parse(args)

    def parse(self, args):
        return getattr(self, f'_parse_{type(args).__name__}')(args)

    def _parse_dict(self, args):
        if any(name not in args for name in self.required):
            raise ValueError(
                f'{self.name} expects argument "{self.required}" is required, but got {args}')
        expected = self.required + list(self.optional)
        if any(name not in expected for name in args):
            raise ValueError(
                f'{self.name} expects arguments are {expected}, but got {args}')
        selector = args.get('selector')
        if selector and selector not in self.selectors:
            raise ValueError(
                f'{self.name} expects selectors are {self.selectors}, but got {selector}')
        result = dict(self.optional)
        result.update(args)
        return result

    def _parse_str(self, args):
        result = dict(self.optional)
        result.update({'value': args})
        return self._parse_dict(result)

    def __getattr__(self, name):
        return self.schema[name]

    def __str__(self):
        return f'<{type(self).__name__}: {self.args}>'


class ClickAction(BaseAction):
    schema = {"required": ["value"],
              "optional": {"selector": "xpath"}}
    name = 'click'


class InputAction(BaseAction):
    name = 'input'


class SelectAction(BaseAction):
    name = 'select'


class DynamicSelectAction(BaseAction):
    name = 'dynamic_select'


class ScrollAction(BaseAction):
    schema = {
        "required": [],
        "optional": {}
    }
    name = 'scroll_window'


class SwitchWindowAction(BaseAction):
    name = 'switch_window'
    schema = {
        "required": ["index"],
        "optional": {}
    }


    def _parse_dict(self, args):
        args = super()._parse_dict(args)
        if not isinstance(args['index'], int) and not args['index'].isdigit():
            raise ValueError(f'{self.name} expects int, but got {args}')
        return args

    def _parse_str(self, args):
        result = dict(self.optional)
        if not args.isdigit():   # args are set by Task, it's only be str
            raise ValueError(f'{self.name} expects int, but got {args}')
        result.update({'index': args})
        return self._parse_dict(result)


class ScreenAction(BaseAction):
    schema = {
        "required": [],
        "optional": {}
    }
    name = 'screenshot'


class MustContainAction(BaseAction):
    name = 'assert_contain'


def _new_action():
    actions = {'click': ClickAction,
               'scroll_window': ScrollAction,
               'screenshot': ScreenAction,
               'input': InputAction,
               'switch_window': SwitchWindowAction,
               'dynamic_select': DynamicSelectAction,
               'select': SelectAction,
               'assert_contain': MustContainAction}

    def _get(name, args):
        if name not in actions:
            raise ValueError(f'{name} not in supported actions')
        return actions[name](args)
    return _get


new_action = _new_action()
