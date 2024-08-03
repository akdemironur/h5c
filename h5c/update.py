import h5py
import sys


def update_attribute(file_path, target_path, attr_name, new_value):
    with h5py.File(file_path, "r+") as file:
        if target_path in file:
            obj = file[target_path]
            if attr_name in obj.attrs:
                old_value = obj.attrs[attr_name]
                old_value_type = type(old_value)
                try:
                    casted_value = old_value_type(new_value)
                    obj.attrs[attr_name] = casted_value
                    print(f"Attribute '{attr_name}' updated successfully.")
                    print(f"{old_value} -> {casted_value}")
                except ValueError:
                    print(f"Error: Cannot cast '{new_value}' to {old_value_type}.")
            else:
                print(
                    f"Error: '{attr_name}' does not exist in '{target_path}'.",
                    file=sys.stderr,
                )
        else:
            print(f"Error: '{target_path}' does not exist.", file=sys.stderr)


def remove_attribute(file_path, target_path, attr_name):
    with h5py.File(file_path, "r+") as file:
        if target_path in file:
            obj = file[target_path]
            if attr_name in obj.attrs:
                del obj.attrs[attr_name]
                print(
                    f"Attribute '{attr_name}' removed from '{target_path}' successfully."
                )
            else:
                print(
                    f"Error: '{attr_name}' does not exist in '{target_path}'.",
                    file=sys.stderr,
                )
        else:
            print(f"Error: '{target_path}' does not exist.", file=sys.stderr)


def remove_dataset_or_group(file_path, path):
    with h5py.File(file_path, "r+") as file:
        if path in file:
            target = file[path]
            target_type = "Dataset" if isinstance(target, h5py.Dataset) else "Group"
            del file[path]
            print(f"{target_type} '{path}' removed successfully.")
        else:
            print(f"Error: Path '{path}' does not exist.", file=sys.stderr)
