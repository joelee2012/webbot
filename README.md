# Command line tool for performing Technical Verification Testing


Supported [selectors](https://selenium-python.readthedocs.io/locating-elements.html) are :
```
xpath
css
id
name
link_text
tag_name
class_name
css_selector
partial_link_text
```

## click

click the element

```yaml
---
click: '<value of xpath>' # implicit selector is 'xpath'
click: # implicit selector is 'xpath'
    - '<value of xpath1>'
    - '<value of xpath2>'
click:
    selector: 'xpath' # optional
    value: '<value of xpath>'

click:
    - selector: 'id' # explict set selector
      value: '<value of id>'
    - value: '<value of xpath2>'
    - '<value of xpath3>'
```

## input

input text for element

```yaml
---
input:
    selector: 'xpath' # optional, default selector is 'xpath'
    value: '<value of xpath>'
    text: 'text to be input'

input:
    - selector: 'xpath' # optional
      value: '<value of xpath1>'
      text: 'text to be input'
    - selector: 'xpath' # optional
      value: '<value of xpath2>'
      text: 'text to be input'
```

## switch_window

switch window

```yaml
---
switch_window: 1
switch_window: '1'
switch_window:
    - 1
    - '1'
switch_window:
    index: 1
switch_window:
    index: '1'
switch_window:
    - index: 1
    - index: '1'

```