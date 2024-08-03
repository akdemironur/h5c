import h5py


def update_attribute(file_path, path, attribute_name, new_value):
    with h5py.File(file_path, "r+") as file:
        if path in file:
            obj = file[path]
            if attribute_name in obj.attrs:
                old_value = obj.attrs[attribute_name]
                old_value_type = type(old_value)
                try:
                    casted_value = old_value_type(new_value)
                    obj.attrs[attribute_name] = casted_value
                    print(f"Attribute '{attribute_name}' updated successfully.")
                    print(f"Old value: {old_value}, New value: {casted_value}")
                except ValueError:
                    print(f"Error: Cannot cast '{new_value}' to {old_value_type}.")
            else:
                print(f"Error: Attribute '{attribute_name}' does not exist.")
        else:
            print(f"Error: Path '{path}' does not exist.")


def remove_attribute(file_path, path, attribute_name):
    with h5py.File(file_path, "r+") as file:
        if path in file:
            obj = file[path]
            if attribute_name in obj.attrs:
                del obj.attrs[attribute_name]
                print(f"Attribute '{attribute_name}' removed successfully.")
            else:
                print(f"Error: Attribute '{attribute_name}' does not exist.")
        else:
            print(f"Error: Path '{path}' does not exist.")


def remove_dataset_or_group(file_path, path):
    with h5py.File(file_path, "r+") as file:
        if path in file:
            del file[path]
            print(f"Dataset or group '{path}' removed successfully.")
        else:
            print(f"Error: Path '{path}' does not exist.")
