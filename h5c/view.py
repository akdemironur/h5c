import h5py
import sys


def view_attribute(file_path, target_path, attr_name=None):
    with h5py.File(file_path, "r") as file:
        if target_path in file:
            target = file[target_path]
            if attr_name:
                if attr_name in target.attrs:
                    attr_value = target.attrs[attr_name]
                    print(f"{attr_name}: {attr_value}")
                else:
                    print(
                        f"Error: '{attr_name}' does not exist in '{target_path}'.",
                        file=sys.stderr,
                    )
            else:
                for key, value in target.attrs.items():
                    print(f"{key}: {value}")
        else:
            print(f"Error: '{target_path}' does not exist.", file=sys.stderr)


def explore_hdf5(group, prefix=""):
    contents = []

    # Get all attributes and items
    attrs = list(group.attrs.items())
    keys = list(group.keys())
    total_items = len(attrs) + len(keys)

    # Process attributes
    for i, (attr_name, attr_value) in enumerate(attrs):
        is_last = i == total_items - 1
        contents.append(
            f"{prefix}{'└── ' if is_last else '├── '}@{attr_name}: {attr_value} ({type(attr_value).__name__})"
        )

    # Process datasets and subgroups
    for i, key in enumerate(keys):
        item = group[key]
        is_last = i + len(attrs) == total_items - 1

        if isinstance(item, h5py.Dataset):
            contents.append(f"{prefix}{'└── ' if is_last else '├── '}{key} (Dataset)")
            next_prefix = prefix + ("    " if is_last else "│   ")
            contents.append(f"{next_prefix}├── Datatype: {item.dtype}")
            contents.append(f"{next_prefix}├── Shape: {item.shape}")

            # Process dataset attributes
            dataset_attrs = list(item.attrs.items())
            for j, (attr_name, attr_value) in enumerate(dataset_attrs):
                is_last_attr = j == len(dataset_attrs) - 1
                contents.append(
                    f"{next_prefix}{'└── ' if is_last_attr else '├── '}@{attr_name}: {attr_value} ({type(attr_value).__name__})"
                )

        elif isinstance(item, h5py.Group):
            contents.append(f"{prefix}{'└── ' if is_last else '├── '}{key}/ (Group)")
            next_prefix = prefix + ("    " if is_last else "│   ")
            contents.extend(explore_hdf5(item, next_prefix))

    return contents


def explore_tree(file_path):
    try:
        with h5py.File(file_path, "r") as file:
            print(file_path)
            contents = explore_hdf5(file)
            print("\n".join(contents))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
