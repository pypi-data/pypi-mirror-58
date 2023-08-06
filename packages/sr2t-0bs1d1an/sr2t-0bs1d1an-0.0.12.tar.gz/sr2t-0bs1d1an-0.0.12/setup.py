import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sr2t-0bs1d1an",
    version="0.0.12",
    author="Guido Kroon",
    author_email="gkroon@maelstrom.ninja",
    description="Converts scanning reports to a tabular format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/0bs1d1an/sr2t",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['argparse', 'PrettyTable', 'XlsxWriter'],
    package_data={
        'sr2t': ['data/*.*'],
    },
    entry_points={
        'console_scripts': ['sr2t=sr2t.sr2t:main'],
    }
)
