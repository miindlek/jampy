solver_stub = '''from jampy import CodeJammer


class {class_name}(CodeJammer):
    # You can define a base path where your input files are stored.
    # If omitted the input files are expected to be in the same folder
    # as this file.
    #base_path = ""

    # Adjust the following list according to the given input file names.
    file_list = [
        "example.in"
        "{problem_number}-small-practice.in",
        "{problem_number}-large-practice.in",
    ]

    @classmethod
    def _setup(cls):
        """Class method called exactly once before solving all input files.

        This method can be used to initialize variables needed for solving,
        which do not change across different input files (for example the
        declaration of a glossary).
        """
        pass

    def _read_file(self, path):
        """Reads one input file.

        This method defines how to read the input file, yielding the
        arguments for each single test case.
        """
        with open(path, 'r') as f:
            # Adjust the following code to your needs.
            f.readline()
            for line in f:
                yield line.strip().split()

    def _solve_one(self, arguments):
        """Solve one test case.

        This method defines how to solve one single test case for the
        given arguments.
        """
        pass
'''