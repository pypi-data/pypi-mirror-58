# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taskipy']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['task = taskipy.cli:main']}

setup_kwargs = {
    'name': 'taskipy',
    'version': '1.0.1',
    'description': 'tasks runner for python projects',
    'long_description': '<img src="./logo.svg" width="150" />\n\n> the complementary task runner for python\n\n## General\nEvery development pipeline has tasks, such as `test`, `lint` or `publish`. With taskipy, you can define those tasks in one file and run them with a simple command.\n\nFor instance, instead of running the following command:\n```bash\npython -m unittest tests/test_*.py\n```\n\nYou can create a task called `test` and simply run:\n```bash\ntask test\n```\n\nIn addition, you can compose tasks and group them together, and also create dependencies between them.\n\nThis project is heavily inspired by [npm\'s run script command](https://docs.npmjs.com/cli/run-script).\n\n## Requirements\nPython 3.5 or newer.\n\nYour project directory should include a valid `pyproject.toml` file, as specified in [PEP-518](https://www.python.org/dev/peps/pep-0518/).\n\n## Usage\n### Installation\nTo install taskipy using pip, simply run:\n```bash\npip install taskipy\n```\n\n#### With Poetry\nIf you\'re using [poetry](https://python-poetry.org/), add taskipy as a dev dependency:\n```bash\npoetry add --dev taskipy\n```\n\n### Adding Tasks \nIn your `pyproject.toml` file, add a new section called `[tool.taskipy.tasks]`.\n\nThe section is a key-value map, from the names of the task to the actual command that should be run in the shell.\n\nExample:\n\n__pyproject.toml__\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nlint = "pylint tests taskipy"\n```\n\n### Running Tasks\nIn order to run a task, run the following command in your terminal (or virtualenv):\n```bash\ntask test\n```\n\n#### With Poetry\nIf you\'re using poetry, you can use its `run` function:\n```bash\npoetry run task test\n```\n\n### Composing Tasks\n#### Grouping Subtasks Together\nSome tasks are composed of multiple subtasks. Instead of writing plain shell commands and stringing them together, you can break them down into multiple subtasks:\n```toml\n[tool.taskipy.tasks]\nlint_pylint = "pylint tests taskipy"\nlint_mypy = "mypy tests taskipy"\n```\n\nAnd then create a composite task:\n```toml\n[tool.taskipy.tasks]\nlint = "task lint_pylint && task lint_mypy"\nlint_pylint = "pylint tests taskipy"\nlint_mypy = "mypy tests taskipy"\n```\n\n#### Pre Task Hook\nTasks might also depend on one another. For example, tests might require some binaries to be built. Take the two following commands, for instance:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nbuild = "make ."\n```\n\nYou could make tests depend on building, by using the **pretask hook**:\n```toml\n[tool.taskipy.tasks]\npre_test = "task build"\ntest = "python -m unittest tests/test_*.py"\nbuild = "make ."\n```\n\nThe pretask hook looks for `pre_<task_name>` task for a given `task_name`. It will run it before running the task itself. If the pretask fails, then taskipy will exit without running the task itself.\n\n#### Post Task Hook\nFrom time to time, you might want to run a task in conjuction with another. For example, you might want to run linting after a successful test run. Take the two following commands, for instance:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nlint = "pylint tests taskipy"\n```\n\nYou could make tests trigger linting, by using the **posttask hook**:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\npost_test = "task lint"\nlint = "pylint tests taskipy"\n```\n\nThe posttask hook looks for `post_<task_name>` task for a given `task_name`. It will run it after running the task itself. If the task failed, then taskipy will not run the posttask hook.\n',
    'author': 'Roy Sommer',
    'author_email': 'roy@sommer.co.il',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/illBeRoy/taskipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
