import os

import click


@click.group()
def jampy():
    pass


@jampy.command()
@jampy.option('--tasknames', default="a_task", help="Name all problem sets separated by a comma. Keep the order for a correct enumeration of each task.")
@jampy.argument('project_dir', default="new_jampy_project", type=click.Path(), help="Folder of the new jampy project.")
def startproject(tasknames, project_dir):
    os.makedirs(project_dir)

    for i, taskname in enumerate(tasknames.split(','), 65):
        problem_number = chr(i)
        file_name = "{}_{}.py".format(problem_number, taskname.lower())
        class_name = "".join(c for c in taskname if c.isalnum())







@jampy.command()
@jampy.option('--url', default=None, help="Url to a google code jam contest site.")
def fetchproject():
    pass


@jampy.command()
def run():
    pass

