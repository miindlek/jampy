import os

import click


class CodeJammer:
    def __init__(self, *, base_path="", file_list, debug=False):
        in_paths = [os.path.join(base_path, f) for f in file_list]
        out_paths = ["_out".join(os.path.splitext(p)) for p in in_paths]

        self._path_tuples = list(zip(in_paths, out_paths))
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
        for in_path, out_path in self._path_tuples:
            try:
                self._solve(in_path, out_path)
            except Exception:
                click.secho('\r\r\r failed!', fg='red')
                if self._debug:
                    raise
