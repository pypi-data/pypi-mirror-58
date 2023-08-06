import xml.etree.ElementTree as Xml
import pandas as pd
import re


LINK_REGEX = r'(?<=\[#\]\(#)\w+(?=\))'
"""Regex used to retrieve the link ID"""

LINK_REPLACE = r'\[#\]\(#\w+\)'
"""Regex used to match the ENTIRE link text for replacement"""

LINK_LENGTH = 6  # 0 to fit all lengths (becomes O(n))
"""The length of link IDs. Set to 0 to fit all lengths but sacrifice O(n)"""

ENTITY_KEYS = ['entity', 'entities', 'e']
"""Entity keywords"""

COMPONENT_KEYS = ['component', 'components', 'c']
"""Component keywords"""

SYSTEM_KEYS = ['system', 'systems', 's']
"""System keywords"""


class ECSType:
    """
    An enum denoting the three parts of ECS
    """
    ENTITY = 'Entity'
    COMPONENT = 'Component'
    SYSTEM = 'System'


class Node:

    def __init__(self, text, node_id, level, ecs_type=None):
        """
        Creates a node element.

        :param text: The text of the node
        :param node_id: The id of the node
        :param level: The hierarchical level of the node
        :param ecs_type: The type of ECS element
        """

        self.original_text = text
        """The unaltered text of the node"""

        self.node_name = re.sub(LINK_REPLACE, '', text).strip()
        """The node's text stripped of its links"""

        self.text = text
        """The current text of the node"""

        self.node_id = node_id
        """The node's ID in the tree"""

        self.level = level
        """The hierarchical level of the node"""

        self.ecs_type = ecs_type
        """The ECS type"""

        self.entities = []
        """List of attached Entities"""

        self.components = []
        """List of attached Components"""

        self.systems = []
        """List of attached Systems"""

    def attach(self, node):
        """
        Attach an ECS node to this one
        :param node: A node that falls into one of the ECS categories
        :return:
        """
        if node.ecs_type is ECSType.ENTITY:
            self.entities.append(node)
        elif node.ecs_type is ECSType.COMPONENT:
            self.components.append(node)
        elif node.ecs_type is ECSType.SYSTEM:
            self.systems.append(node)

    def get_attachments(self):
        """
        Get the ECS attachments of this node.
        :return: A dict containing the attachments
        """
        return {
            ECSType.ENTITY: tuple(self.entities),
            ECSType.COMPONENT: tuple(self.components),
            ECSType.SYSTEM: tuple(self.systems)
        }

    def has_attachment(self, name, ecs_type=ECSType.COMPONENT):
        """
        Check if node contains an ECS attachment
        :param name: The name of the node to check
        :param ecs_type: The type to check
        :return: True if node contains the given node
        """
        if ecs_type is ECSType.ENTITY:
            return name in self.entities
        elif ecs_type is ECSType.COMPONENT:
            return name in self.components
        elif ecs_type is ECSType.SYSTEM:
            return name in self.systems

    def print(self, spacer=' ', spaced=2, include_id=True):
        """
        Print the node with S T Y L E. Used for pretty print.
        :param spacer: The string to prepend (denotes level)
        :param spaced: The number of times to print the spacer
        :param include_id: True to include the id in the string
        :return: A string representing the node
        """
        if include_id:
            # Example: --This is a node with id! {1a2b3c}
            return f'{spacer * (self.level * spaced)}{self.text} {{{self.node_id}}}'
        else:
            # Example: --This is a node without id!
            return f'{spacer * (self.level * spaced)}{self.text}'

    def __repr__(self):
        # Example: This is a node!
        return self.node_name


class CoggleECS:

    def __init__(self, file):
        """
        Parse for ECS from a Coggle XML.

        :param file: The XML (or .mm) file to parse.
        """

        self.tree = Xml.parse(file)
        """The XML Tree"""

        self.root = self.tree.getroot()
        """The root node"""

        self.nodes = []
        """List of nodes in the tree (in order)"""

        self.ids = {}
        """Dict of IDs pointing to their node's index"""

        self.links_replaced = False
        """Flag for determining if the links have been replaced"""

        self.entities = []
        """List of Entities in the tree"""

        self.components = []
        """List of Components in the tree"""

        self.systems = []
        """List of Systems in the tree"""

        self.table = None
        """Pandas DataFrame for the ECS data"""

    def parse(self, link_regex=LINK_REGEX, link_replace=LINK_REPLACE, link_length=LINK_LENGTH, auto_replace=True):
        """
        Parse the file and get all nodes.

        :param link_regex: The regex used to retrieve the link ID
        :param link_replace: The regex used to match the ENTIRE link text for replacement
        :param link_length: The length of link IDs (set to 0 to fit all lengths but sacrifice O(n))
        :param auto_replace: Replace all the links with default parameters
        :return:
        """
        self.__get_nodes(self.root, level=0, link_length=link_length)

        if auto_replace:
            self.replace_links(link_regex=link_regex, link_replace=link_replace, link_length=link_length)

    def replace_links(self, link_regex=LINK_REGEX, link_replace=LINK_REPLACE, link_length=LINK_LENGTH, delim=', ', open_str='<', close_str='>'):
        """
        Replace all the id links in the tree with their respective nodes.

        :param link_regex: The regex used to retrieve the link ID
        :param link_replace: The regex used to match the ENTIRE link text for replacement
        :param link_length: The length of link IDs (set to 0 to fit all lengths but sacrifice O(n))
        :param delim: String between each item
        :param open_str: String that prepends the node's list of links
        :param close_str: String that appends the node's list of links
        :return:
        """
        for node in self.nodes:
            # Get all links in node
            links = re.findall(link_regex, node.text)

            # Replace all links in node
            for index, match in enumerate(links):
                replacement_text = ''
                replacement_node = None
                if link_length == 0:
                    replacement_node = self.find_by_id(match)
                    replacement_text = replacement_node.text
                else:
                    replacement_index = self.ids[match[:link_length]]
                    replacement_node = self.nodes[replacement_index]
                    replacement_text = replacement_node.text

                node.attach(replacement_node)

                if index == 0:
                    # Prepend list with open_str
                    replacement_text = f'{open_str}{replacement_text}'
                if index == len(links) - 1:
                    # Append list with close_str
                    replacement_text = f'{replacement_text}{close_str}'
                else:
                    # Add delim between each item (except last)
                    replacement_text = f'{replacement_text}{delim}'

                # Replace the node's text
                node.text = re.sub(link_replace, replacement_text, node.text, count=1)
        # Set flag
        self.links_replaced = True

    def __get_nodes(self, elt, level=0, ecs_type=None, link_length=LINK_LENGTH):
        """
        Recursively search through the tree and track all nodes.

        :param elt: The next element to search
        :param level: The hierarchical level of the element
        :param ecs_type: The ECSType of the node
        :param link_length: The length of link IDs (set to 0 to fit all lengths but sacrifice O(n))
        :return:
        """

        for child in list(elt):

            next_ecs = None
            node_index = len(self.nodes)

            # Try to get certain elements off the child
            try:
                # === GET ATTRIBUTES === #
                # The text of the child
                text = child.attrib.get('TEXT')
                # The id of the child
                node_id = child.attrib.get('ID')

                # === DO WE CARE? === #
                # Skip this element if one of the above does not exist
                if text is None or node_id is None:
                    continue

                # === REDUCE ID === #
                if LINK_LENGTH != 0:
                    # Reduce ids to the specified link length if not 0
                    # This will speed up searches in the future
                    node_id = node_id[:link_length]

                # === THIS ECS TYPE === #
                if ecs_type is ECSType.ENTITY:
                    self.entities.append(node_index)
                elif ecs_type is ECSType.COMPONENT:
                    self.components.append(node_index)
                elif ecs_type is ECSType.SYSTEM:
                    self.systems.append(node_index)

                # === NEXT ECS TYPE === #
                if text.lower() in ENTITY_KEYS:
                    next_ecs = ECSType.ENTITY
                elif text.lower() in COMPONENT_KEYS:
                    next_ecs = ECSType.COMPONENT
                elif text.lower() in SYSTEM_KEYS:
                    next_ecs = ECSType.SYSTEM

                # === CREATE NODE === #
                node = Node(text=text, node_id=node_id, level=level, ecs_type=ecs_type)

                # === SAVE NODE === #
                # Track index of node by its id
                self.ids[node_id] = node_index
                # Store node
                self.nodes.append(node)

            except KeyError:
                # One of the attributes doesn't exist -> skip it
                pass
            # Recursive call to any children elements
            self.__get_nodes(child, level+1, ecs_type=next_ecs, link_length=link_length)

    def print_tree(self, delim=' ', delim_count=4, include_id=False):
        """
        Print the parsed tree.

        :param delim: Prepends node (Used to denote the level)
        :param delim_count: Number of delims to print
        :param include_id: Include the node's id at the end
        :return:
        """
        if len(self.nodes) == 0:
            print('Tree is empty ( Make sure you use .parse() first! )')
            return
        for node in self.nodes:
            print(node.print(spacer=delim, spaced=delim_count, include_id=include_id))

    def find_by_id(self, start_of_id):
        """
        Find a node by the start of its id.

        .. note:: Performs in O(n) time.

        :param start_of_id:
        :return:
        """
        return [v for k, v in self.ids.items() if k.startswith(start_of_id)][0]

    def get_entities(self, name_only=False):
        """
        Get the Entities in the tree
        :param name_only: Return only the names of the nodes
        :return: A list of Entities
        """
        if name_only:
            return [self.nodes[index].node_name for index in self.entities]
        else:
            return [self.nodes[index] for index in self.entities]

    def get_components(self, name_only=False):
        """
        Get the Components in the tree
        :param name_only: Return only the names of the nodes
        :return: A list of Components
        """
        if name_only:
            return [self.nodes[index].node_name for index in self.components]
        else:
            return [self.nodes[index] for index in self.components]

    def get_systems(self, name_only=False):
        """
        Get the Systems in the tree
        :param name_only: Return only the names of the nodes
        :return: A list of Systems
        """
        if name_only:
            return [self.nodes[index].node_name for index in self.systems]
        else:
            return [self.nodes[index] for index in self.systems]

    def create_table(self, include_systems=True):
        """
        Create a pandas table of the data
        :param include_systems: Include Systems data in the table
        :return:
        """

        # === REPLACE LINKS IF HAVEN'T === #
        if not self.links_replaced:
            self.replace_links()

        # === CREATE DATA === #
        def create_data(nodes, component_list, indexes_list):
            """
            Create the data for the pandas DataFrame
            :param nodes: The list of nodes to add
            :param component_list: The list of components to check against
            :param indexes_list: The list of indexes to apply
            :return:
            """
            return_data = []
            for node in nodes:
                # === COMPONENTS === #
                # Add True or False for each component based on if node has it
                node_data = [component in node.components for component in component_list]

                # === INDEXES === #
                for index in indexes_list[::-1]:
                    if index == 'Name':
                        node_data.insert(0, node.node_name)
                    elif index == 'Type':
                        node_data.insert(0, node.ecs_type)

                # === ADD DATA === #
                return_data.append(node_data)
            return return_data

        # === CREATE TABLE === #
        # Stores the indexes of the table
        indexes = []
        # Stores the data of the table
        data = []
        # --- Get Data --- #
        if include_systems:
            indexes = ['Type', 'Name']
            names = self.get_entities() + self.get_systems()
            data = create_data(names, self.get_components(), indexes)
        else:
            indexes = ['Name']
            names = self.get_entities()
            data = create_data(names, self.get_components(), indexes)

        # --- Name Columns --- #
        columns = indexes + self.get_components(True)

        # --- Create Table --- #
        self.table = pd.DataFrame(data, columns=columns).set_index(indexes)

    def print_table(self, use_ticks=True, true_tick='X', false_tick=''):
        """
        Prints the data in a table format.
        :param use_ticks: Replace True and False with given strings
        :param true_tick: Tick to replace True
        :param false_tick: Tick to replace False
        :return:
        """

        # === CREATE TABLE IF NONE === #
        if self.table is None:
            self.create_table()

        # === PRINT TABLE === #
        if use_ticks:
            print(self.table.replace({True: true_tick, False: false_tick}))
        else:
            print(self.table)

    def output_text(self, outfile, delim=' ', indent=4, include_id=False):
        """
        Output the tree to a text file.
        :param outfile: The output file
        :param delim: Prepends node (Used to denote the level)
        :param indent: Number of delims to print
        :param include_id: Include the node's id at the end
        :return:
        """
        with open(outfile, 'w') as f:
            outstring = []
            for node in self.nodes:
                outstring.append(node.print(spacer=delim, spaced=indent, include_id=include_id))
            f.write('\n'.join(outstring))

    def output_structure(self, outfile, indent=3, down='|', level='+', dash='-', space=' '):
        """
        Output the tree in a folder structure format to a text file.
        :param indent: The number to indent each level
        :param down: The character denoting a change in level
        :param level: The character denoting a new parent
        :param dash: The character bridging between the level and the node
        :param space: The empty space between down characters
        :param outfile: The output file
        :return:
        """
        with open(outfile, 'w') as f:
            outstring = []
            is_root = True
            empty_dir = f'{down}{space * indent}'
            full_dir = f'{level}{dash * indent} '
            for node in self.nodes:
                lvl = node.level
                prepender = f'{"" if is_root else empty_dir * (lvl - 1)}'
                current = f'{"" if is_root else full_dir}'
                outstring.append(f'{prepender}{current}{node.text}')
                is_root = False
            f.write('\n'.join(outstring))

    def output_table(self, outfile, use_ticks=True, true_tick='X', false_tick=''):
        """
        Output the table to a text file.
        :param outfile: The output file
        :param use_ticks: Replace True and False with given strings
        :param true_tick: Tick to replace True
        :param false_tick: Tick to replace False
        :return:
        """
        # === CREATE TABLE IF NONE === #
        if self.table is None:
            self.create_table()

        # === WRITE FILE === #
        with open(outfile, 'w') as f:
            if use_ticks:
                f.writelines(self.table.replace({True: true_tick, False: false_tick}).to_string())
            else:
                f.writelines(self.table.to_string())

    def output_csv(self, outfile, sep=','):
        """
        Output the table to a CSV file.
        :param outfile: The output file
        :param sep: The CSV separator
        :return:
        """
        # === CREATE TABLE IF NONE === #
        if self.table is None:
            self.create_table()

        # === WRITE FILE === #
        self.table.to_csv(outfile, sep=sep)

    def output_json(self, outfile, orient='split'):
        """
        Output the table to a JSON file.
        :param outfile: The output file
        :param orient: Indication of expected JSON string format (pandas)
        :return:
        """
        # === CREATE TABLE IF NONE === #
        if self.table is None:
            self.create_table()

        # === WRITE FILE === #
        self.table.to_json(outfile, orient=orient)


if __name__ == '__main__':
    parser = CoggleECS('example.mm')
    parser.parse()
    parser.output_text('tree.txt')
    parser.output_structure('structure.txt')
    parser.output_table('table.txt')
    parser.output_csv('table.csv')
    parser.output_json('table.json')
