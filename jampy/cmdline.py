import os

import click

from jampy.template import solver_stub


@click.group()
def jampy():
    pass


@jampy.command()
@click.option('--tasknames', default="a_task", help="Name all problem sets separated by a comma. Keep the order for a"
              "correct enumeration of each task.")
@click.argument('project_dir', default="new_jampy_project", type=click.Path())
def startproject(tasknames, project_dir):
    os.makedirs(project_dir)

    for i, taskname in enumerate(tasknames.split(','), 65):
        problem_number = chr(i)
        file_name = "{}_{}.py".format(problem_number, taskname.lower())
        class_name = "{}Solver".format("".join(c for c in taskname if c.isalnum()))

        create_template_file(os.path.join(project_dir, file_name), class_name, problem_number)


def create_template_file(file_path, class_name, problem_number):
        with open(file_path, 'w') as f:
            f.write(solver_stub.format(class_name=class_name, problem_number=problem_number))


@jampy.command()
@click.option('--url', default=None, help="Url to a google code jam contest site.")
def fetchproject():
    pass


@jampy.command()
def run():
    pass

