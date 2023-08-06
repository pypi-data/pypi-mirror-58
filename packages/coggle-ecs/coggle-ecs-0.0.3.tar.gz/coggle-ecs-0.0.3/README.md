# CoggleECS

CoggleECS is a small tool used to parse `.mm` files created at [coggle.it](https://coggle.it) for ECS data. It can then output ECS data as a tree or table. It can also be used to simply show links in your map.

For instance, Coggle creates links between nodes using a markdown format: `Player [#](#5d3adc) [#](#78959d)`. CoggleECS will replace those links with their respective nodes: `Player <Move,  Transform>`.



## Installation

### Using pip [![PyPI version](https://badge.fury.io/py/coggle-ecs.svg)](https://badge.fury.io/py/coggle-ecs)

Run the following line in the terminal:

`pip install coggle-ecs`

### Using setup.py

Clone or download this repository and run the following line from the project's root directory:

`python setup.py install`

### Using Ctl+C

Copy and paste if you're daring enough.

 

## Setup & Usage

### 1. In Coggle

Outputting as tree data can work for any type of Coggle map (in fact you can just export the map itself as a text tree from Coggle if you don't care about replacing links). 

However, outputting as a table requires a few things:

1. There **needs** to be nodes named each of the following (not case-sensitive):
   * 'Entitities' or 'Entity' or 'E'
   * 'Components' or 'Component' or 'C'
   * 'Systems' or 'System' or 'S'
2. Entities should link **to** their respective Components.
3. Systems should link **to** their respective Components.

Without the three nodes, the table will not render. And if those nodes exist but there are no links (or improper ones) then table will be be unfilled.

### 2. In CoggleECS

Once the above steps have been completed and your map has been filled, download it as a `.mm`. Then follow a similar program to below:

```python
from coggle_ecs import CoggleECS
my_map = CoggleECS('path/to/your/map.mm')
my_map.parse()
```

You're all set to use `my_map` (or whatever you named it) to export in whatever format you prefer!



## Examples

### Input

```xml
<map version="0.9.0">
    <node TEXT="Game Engine" FOLDED="false" POSITION="right" ID="5e0568ca68fbc74e9bb7c666" X_COGGLE_POSX="0" X_COGGLE_POSY="0">
        <edge COLOR="#b4b4b4"/>
        <font NAME="Helvetica" SIZE="17"/>
        <node TEXT="Entities" FOLDED="false" POSITION="right" ID="c2876d86e931f9deab2da00f">
            <edge COLOR="#ebd95f"/>
            <font NAME="Helvetica" SIZE="15"/>
            <node TEXT="Player [#](#5d3adc) [#](#78959d)" FOLDED="false" POSITION="right" ID="2fbd2a01b1c71bd12bcbcb6b">
                <edge COLOR="#ecd966"/>
                <font NAME="Helvetica" SIZE="13"/>
                <node TEXT="This is some description." FOLDED="false" POSITION="right" ID="b5b0332157c9287b3640d066">
                    <edge COLOR="#ecd870"/>
                    <font NAME="Helvetica" SIZE="13"/>
                </node>
            </node>
            <node TEXT="Alien [#](#78959d) [#](#feee8a)" FOLDED="false" POSITION="right" ID="22db55a2c98a51c71bca1791">
                <edge COLOR="#ead86c"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
        </node>
        <node TEXT="Components" FOLDED="false" POSITION="right" ID="abed60d3595a05321d843d5c">
            <edge COLOR="#efa670"/>
            <font NAME="Helvetica" SIZE="15"/>
            <node TEXT="Hostile" FOLDED="false" POSITION="right" ID="feee8a5d3ea26d514852b5db">
                <edge COLOR="#eea26d"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
            <node TEXT="Transform" FOLDED="false" POSITION="right" ID="78959d52cbc1843fb429b409">
                <edge COLOR="#ee9d65"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
            <node TEXT="Move" FOLDED="false" POSITION="right" ID="5d3adc4deef6b0da6ebcc899">
                <edge COLOR="#f09e65"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
        </node>
        <node TEXT="Systems" FOLDED="false" POSITION="right" ID="36c5720bc10e612f2a18cad1">
            <edge COLOR="#e68782"/>
            <font NAME="Helvetica" SIZE="15"/>
            <node TEXT="Movement System [#](#5d3adc) [#](#78959d)" FOLDED="false" POSITION="right" ID="22e2424c6291b42cd61178e7">
                <edge COLOR="#e37e7b"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
            <node TEXT="Enemy System [#](#feee8a)" FOLDED="false" POSITION="right" ID="0ed47a23e497face721424d9">
                <edge COLOR="#e78682"/>
                <font NAME="Helvetica" SIZE="13"/>
            </node>
        </node>
        <node TEXT="Art" FOLDED="false" POSITION="left" ID="14bf08663116d2383d6c20f3">
            <edge COLOR="#e096e9"/>
            <font NAME="Helvetica" SIZE="15"/>
        </node>
    </node>
</map>
```

### Output

```
Game Engine
    Entities
        Player <Move,  Transform>
            This is some description.
        Alien <Transform,  Hostile>
    Components
        Hostile
        Transform
        Move
    Systems
        Movement System <Move,  Transform>
        Enemy System <Hostile>
    Art
```

```
                       Hostile Transform Move
Type   Name                                  
Entity Player                          X    X
       Alien                 X         X     
System Movement System                 X    X
       Enemy System          X               
```



## Output Functions

```python
output_text(self, outfile, delim=' ', indent=4, include_id=False)
```

Output the map as a tree into a text file.

​		*outfile*: The output file

​		*delim*: Prepends node (Used to denote the level)

​		*indent*: Number of delims to print

​		*include_id*: Include the node's id at the end

```python
output_structure(self, outfile, indent=3, down='|', level='+', dash='-', space=' ')
```

Output the map as a tree (in a folder structure format) into a text file.

​		*outfile*: The output file
​		*indent*: The number to indent each level
​		*down*: The character denoting a change in level
​		*level*: The character denoting a new parent
​		*dash*: The character bridging between the level and the node
​		*space*: The empty space between down characters

```python
output_table(self, outfile, use_ticks=True, true_tick='X', false_tick='')
```

Output the map as a table into a text file.

​		*outfile*: The output file
​		*use_ticks*: Replace True and False with given strings
​		*true_tick*: Tick to replace True
​		*false_tick*: Tick to replace False

```python
output_csv(self, outfile, sep=',')
```

Output the map as a table into a CSV file.

​		*outfile*: The output file

​		*sep*: The CSV separator

```python
output_json(self, outfile, orient='split')
```

Output the map as a table into a JSON file.

​		*outfile*: The output file

​		*orient*: The format for the JSON (used internally by a pandas DataFrame)



## Other Functionality

You can also tap into your `CoggleECS` instance to get other data. Some examples:

```python
from coggle_ecs import CoggleECS
my_map = CoggleECS('path/to/your/map.mm')
my_map.parse()

# Find a node by the beginning of its ID (returns first occurence)
node = my_map.find_by_id('1a2b3c')
# Get all the Entities, Components, or Systems
entities = my_map.get_entities()
components = my_map.get_components()
systems = my_map.get_systems()
# Get the ECS pandas DataFrame
my_map.create_table(include_systems=True)
df = my_map.table
```



## Dependencies

This tool runs on Python 3 or later.

It also requires Pandas (the library, not the bear).