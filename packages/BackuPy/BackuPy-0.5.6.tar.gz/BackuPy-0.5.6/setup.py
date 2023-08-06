import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BackuPy",
    version="0.5.6",
    description="BackuPy: A small python program for backing up directories with an emphasis on clear rules, simple usage, and logging changes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elesiuta/backupy",
    py_modules=['backupy'],
    entry_points={
        'console_scripts': [
            'backupy = backupy:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
