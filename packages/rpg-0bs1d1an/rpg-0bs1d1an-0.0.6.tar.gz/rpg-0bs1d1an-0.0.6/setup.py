import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpg-0bs1d1an",
    version="0.0.6",
    author="Guido Kroon",
    author_email="gkroon@maelstrom.ninja",
    description="Risk plot generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/0bs1d1an/rpg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['argparse', 'matplotlib'],
    package_data={
        'rpg': ['data/*.png'],
    },
    entry_points={
        'console_scripts': ['rpg=rpg.rpg:main'],
    }
)
