# h5c: HDF5 Command-Line Tool

h5c is a command-line tool for viewing and updating attributes in HDF5 files. It provides a simple interface to explore HDF5 file structures, view and modify attributes, and remove attributes or entire datasets/groups.

## Features

- Explore HDF5 file structure
- View attributes of datasets or groups
- Update attribute values
- Remove specific attributes
- Remove entire datasets or groups

## Installation

Ensure you have Python 3.8 or later installed. Then install h5c using pip:

`pip install git+https://github.com/akdemironur/h5c.git`

## Usage

h5c provides three main commands: `view`, `update`, and `remove`.

### View Command

To explore the file structure or view attributes:

`h5c view <file_path> [<path_in_file>] [<attribute_name>]`

- If only `<file_path>` is provided, it explores the entire file structure.
- If `<path_in_file>` is provided, it shows attributes of that dataset or group.
- If `<attribute_name>` is also provided, it shows the value of that specific attribute.

### Update Command

To update an attribute value:

`h5c update <file_path> <path_in_file> <attribute_name> <new_value>`

### Remove Command

To remove an attribute or a dataset/group:

`h5c remove <file_path> <path_in_file> [<attribute_name>]`

- If `<attribute_name>` is provided, it removes that specific attribute.
- If `<attribute_name>` is not provided, it removes the entire dataset or group at `<path_in_file>`.

## Examples

1. Explore the file structure:

`h5c view example.h5`

2. View all attributes of a dataset:

`h5c view example.h5 /path/to/dataset`

3. View a specific attribute:

`h5c view example.h5 /path/to/dataset attribute_name`

4. Update an attribute:

`h5c update example.h5 /path/to/dataset attribute_name new_value`

5. Remove an attribute:

`h5c remove example.h5 /path/to/dataset attribute_name`

6. Remove a dataset or group:

`h5c remove example.h5 /path/to/dataset_or_group`

## Contributing

This tool was developed for personal use. If you don't find a feature you want, it's likely because I didn't need it. However, if you need additional functionality:

1. Open an issue to request the feature
2. Or, if you're able to implement it yourself, feel free to open a Pull Request


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Onur Akdemir

Project Link: https://github.com/akdemironur/h5c