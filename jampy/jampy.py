import os
import traceback

import click


class CodeJammer:
    base_path = ""
    file_list = None

    def __init__(self, debug=False):
        if not self.file_list:
            raise ValueError('"file_list" variable not declared. '
                             'You need to specify a list of input files as class attribute.')
        self._debug = debug

    def _read_file(self, path):
        click.echo("{} not implemented.".format(click.style("_read_file()", fg='blue')))
        raise NotImplementedError

    def _write_file(self, path, results):
        with open(path, "w") as f:
            for i, result in enumerate(results, 1):
                f.write("Case #{}: {}\n".format(i, result))

    def _solve_one(self, arguments):
        click.echo("{} not implemented.".format(click.style("_solve_one()", fg='blue')))
        raise NotImplementedError

    def _solve(self, in_path, out_path):
        click.echo('Start solving {} ...'.format(click.style(in_path, fg='blue')), nl=False)

        arguments = self._read_file(in_path)
        results = [self._solve_one(arg) for arg in arguments]
        self._write_file(out_path, results)

        click.secho('\r\r\r done.', fg='green')

    def run(self):
        for file_name in self.file_list:
            in_path = os.path.join(self.base_path, file_name)
            out_path = "_out".join(os.path.splitext(in_path))

            try:
                self._solve(in_path, out_path)
            except Exception:
                click.secho('\r\r\r failed!', fg='red')
                if self._debug:
                    traceback.print_last()
