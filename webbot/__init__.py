import sys
import time
from argparse import ArgumentParser
import contextlib

import yaml
from selenium import webdriver

from .runner import Runner
from .workflow import WorkFlow


@contextlib.contextmanager
def open_url(url, wait_time=20):
    with webdriver.Chrome() as driver:
        # driver.implicitly_wait(wait_time)
        driver.get(url)
        yield driver


def main():
    parser = ArgumentParser(description='cli to perform tvt test')
    parser.add_argument('yaml_files', metavar='filename',
                        action='append', help='yml files to run')
    args = parser.parse_args()

    for yaml_file in args.yaml_files:
        with open(yaml_file) as fd:
            yaml_data = yaml.safe_load(fd)

        workflow = WorkFlow(yaml_data)
        workflow.parse()
        with open_url(workflow.url) as driver:
            runner = Runner(driver)
            print(f'start to execute: {workflow}')
            for task in workflow:
                print(f'run: {task}')
                for action in task:
                    time.sleep(0.1)
                    print('  - ', end='')
                    runner.run_action(action)
            time.sleep(20)
