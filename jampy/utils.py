
def camel_case(name):
    return "".join(c for c in name.title() if c.isalnum())


def create_template_file(file_path, class_name, problem_number):
        with open(file_path, 'w') as f:
            f.write(solver_stub.format(class_name=class_name, problem_number=problem_number))

