import os
from setuptools import find_packages, setup

# readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
# with open(readme_file) as readme:
#     README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

README = """
Seriously, 
---

I knows you deserve the most complete, easy-to-read, exemplified documentation in the world... 
well, with all my respect, please let me say you the same Axel said several years ago,

    "All we need is just a little patience" 



_It is a fact, jokes aren't one of my best skills._
"""

setup(
    name="tokko-cli",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        'playbook': ['src/playbooks/*.*']
    },
    include_package_data=True,
    license="BSD License",  # TODO: Read about..
    description="Tokko broker developers CLI.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/josesalgado1024/tokko-cli",
    author="Jose Salgado",
    author_email="jose.salgado.wrk@gmail.com",
    install_requires=["click", "arrow"],
    entry_points='''
        [console_scripts]
        tokko=src.commands:services
    ''',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",  # TODO: Read about..
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
