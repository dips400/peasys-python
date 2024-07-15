import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="peasys",
    version="1.0.2",
    author="DIPS",
    keywords="ibm db2 peasys",
    license="MIT",
    url="https://github.com/dips400/peasys-python",
    author_email="dips@dips400.com",
    description="A clear and concise python client for IBM Db2 and peasys service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["peasys"],
)