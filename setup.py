from setuptools import setup

setup(
    name='jampy',
    version='0.1',
    author='miindlek',
    author_email='miindlek@gmail.com',
    url='https://github.com/miindlek/jampy',

    py_modules=["jampy"],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'jampy=jampy.cmdline:jampy',
        ]
    }
)