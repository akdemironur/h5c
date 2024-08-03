import argparse
from .view import view_attribute, explore_tree
from .update import update_attribute, remove_attribute, remove_dataset_or_group


def main():
    parser = argparse.ArgumentParser(
        description="HDF5 command line tool for viewing and updating attributes"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    # View command
    view_parser = subparsers.add_parser(
        "view", help="View attributes of a dataset or group or explore the file tree"
    )
    view_parser.add_argument("file", help="Path to the HDF5 file")
    view_parser.add_argument(
        "path", nargs="?", help="Path to the dataset or group in the HDF5 file"
    )
    view_parser.add_argument(
        "attribute", nargs="?", help="Name of the attribute to view"
    )

    # Update command
    update_parser = subparsers.add_parser(
        "update", help="Update the value of an attribute in a dataset or group"
    )
    update_parser.add_argument("file", help="Path to the HDF5 file")
    update_parser.add_argument(
        "path", help="Path to the dataset or group in the HDF5 file"
    )
    update_parser.add_argument("attribute", help="Name of the attribute to update")
    update_parser.add_argument("value", help="New value for the attribute")

    # Remove command
    remove_parser = subparsers.add_parser(
        "remove", help="Remove an attribute from a dataset or group"
    )
    remove_parser.add_argument("file", help="Path to the HDF5 file")
    remove_parser.add_argument(
        "path", help="Path to the dataset or group in the HDF5 file"
    )
    remove_parser.add_argument(
        "attribute", nargs="?", help="Name of the attribute to remove"
    )

    args = parser.parse_args()

    if args.command == "view":
        if args.path:
            view_attribute(args.file, args.path, args.attribute)
        else:
            explore_tree(args.file)
    elif args.command == "update":
        update_attribute(args.file, args.path, args.attribute, args.value)
    elif args.command == "remove":
        if args.attribute:
            remove_attribute(args.file, args.path, args.attribute)
        else:
            remove_dataset_or_group(args.file, args.path)


if __name__ == "__main__":
    main()
