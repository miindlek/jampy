import os

import click

from jampy.templates import solver_stub


@click.group()
def jampy():
    pass


@jampy.command()
@click.option('--tasknames', default="task", help="Name all problem sets separated by a comma. Keep the order for a"
              "correct enumeration of each task.")
@click.argument('project_dir', default="new_jampy_project", type=click.Path())
def startproject(tasknames, project_dir):
    os.makedirs(project_dir)

    for i, taskname in enumerate(tasknames.split(','), 65):
        problem_number = chr(i)
        name = camel_case(taskname)
        file_name = "{}_{}.py".format(problem_number, name).lower()
        class_name = "{}Solver".format(name)

        create_template_file(os.path.join(project_dir, file_name), class_name, problem_number)

@jampy.command()
@click.option('--url', help="Url to a google code jam contest site.")
def fetchproject(url):
    # Examplerequest:
    # resp = requests.get("https://code.google.com/codejam/contest/6254486/dashboard/ContestInfo")

    pass


@jampy.command()
def run():
    jampy.commands.run.execute

