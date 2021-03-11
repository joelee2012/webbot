# Command line tool for performing web action follow by task defined in yml


## Installation

```sh
python3 -m pip install webbot
```

## Example to open bing.com and search python:

define tasks as following bing.yml file
```yaml
---
name: search content in bing.com
url: http://www.bing.com
driver: chrome
tasks:
  - name: open the main page of bing.com
    input:
      - value: '//*[@id="sb_form_q"]'
        text: 'python'
    click:
      - selector: xpath
        value: '//*[@id="sb_form"]/label'
```

then call webbot:

```sh
webbot bing.yml
```

## Document

### Supported [selectors](https://selenium-python.readthedocs.io/locating-elements.html) are :
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

### click

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

### input

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

### switch_window

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