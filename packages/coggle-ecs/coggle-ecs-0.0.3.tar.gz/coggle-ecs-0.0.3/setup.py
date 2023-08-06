import pathlib
from setuptools import setup, find_packages

# The directory containing this file
ROOT = pathlib.Path(__file__).parent

# The text of the README file
README = (ROOT / "README.md").read_text()

setup(
    name='coggle-ecs',
    version='0.0.3',
    url='https://github.com/MrGVSV/coggle-ecs',
    license='MIT',
    author='Gino Valente',
    author_email='gino.valente.code@gmail.com',
    description='Convert Coggle .mm files to ECS tables and whatnot',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas'],
    python_requires='>=3.6'

)
