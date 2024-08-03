import h5py


def view_attribute(file_path, target_path, attr_name=None):
    try:
        with h5py.File(file_path, "r") as file:
            target = file[target_path]
            if attr_name:
                print(f"{attr_name}: {target.attrs[attr_name]}")
            else:
                for key, value in target.attrs.items():
                    print(f"{key}: {value}")
    except KeyError as e:
        print(f"Error: Attribute {e} not found.")
    except Exception as e:
        print(f"Error: {e}")


def explore_hdf5(group, indent="|-- "):
    print(f"{indent}Group: {group.name}")
    new_indent = "|   " + indent

    for attr_name, attr_value in group.attrs.items():
        print(
            f"{new_indent}Attribute: {attr_name} ({type(attr_value).__name__}): {attr_value}"
        )

    for key, item in group.items():
        if isinstance(item, h5py.Dataset):
            print(f"{new_indent}Dataset: {key}")
            print(f"|   {new_indent}Datatype: {item.dtype}")
            print(f"|   {new_indent}Shape: {item.shape}")
            for attr_name, attr_value in item.attrs.items():
                print(
                    f"{new_indent}  Attribute: {attr_name} ({type(attr_value).__name__}): {attr_value}"
                )

    for key, item in group.items():
        if isinstance(item, h5py.Group):
            explore_hdf5(item, new_indent)


def explore_tree(file_path):
    try:
        with h5py.File(file_path, "r") as file:
            explore_hdf5(file)
    except Exception as e:
        print(f"Error: {e}")
