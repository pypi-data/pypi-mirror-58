from setuptools import setup, find_packages

setup(
    name="allenpoly",
    packages=find_packages(),
    version="0.0.1",
    license="BSD",
    description="An library to use AllenNLP library in Polyaxon environment.",
    author="Evidence Prime Sp. z o.o.",
    author_email="mateusz.pieniak@evidenceprime.com",
    url="https://bitbucket.org/evidenceprime/allenpoly",
    keywords=["allennlp", "polyaxon"],
    install_requires=[
        # "python-dateutil<2.8.1, >=2.1",
        # "docutils<0.16, >=0.10",
        # "rhea==0.5.4",
        "allennlp",
        "polyaxon-client",
    ],
    python_requires=">=3.6.9",
    entry_points={"console_scripts": ["allenpoly=allenpoly.run:run"]},
)