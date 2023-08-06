import setuptools

long_description = """
CoggleECS is a small tool used to parse `.mm` files created at [coggle.it]() for ECS data. It can then output ECS data as a tree or table. It can also be used to simply show links in your map.

For instance, Coggle creates links between nodes using a markdown format: `Player [#](#5d3adc) [#](#78959d)`. CoggleECS will replace those links with their respective nodes: `Player <Move,  Transform>`.
"""

setuptools.setup(
    name='coggle-ecs',
    version='0.0.1',
    url='https://github.com/MrGVSV/coggle-ecs',
    license='MIT',
    author='Gino Valente',
    author_email='gino.valente.code@gmail.com',
    description='Convert Coggle .mm files to ECS tables and whatnot',
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=['pandas'],
    python_requires='>=3.6'

)
