import pytest
import h5py
from h5c.view import view_attribute, explore_hdf5
from .test_mock_hdf5 import mock_hdf5_file

'''
@pytest.fixture
def mock_hdf5_file(tmp_path):
    """Create a temporary HDF5 file with some attributes for testing."""
    file_path = tmp_path / "test.h5"
    with h5py.File(file_path, "w") as file:
        grp = file.create_group("my_group")
        grp.attrs.create("my_attr", np.int64(1))
        grp.attrs.create("my_string_attr", "Hello, World!")
        grp.attrs.create("my_float_attr", np.float32(3.14))
        grp.attrs.create("my_bool_attr", True)
        grp.attrs.create("my_double_attr", np.float64(2.71828))

        subgrp = grp.create_group("my_subgroup")
        subgrp.attrs.create("subgroup_attr", "Subgroup Attribute")
        subgrp.attrs.create("subgroup_attr_int", np.int32(1))

        dataset = grp.create_dataset("my_dataset", shape=(10,), dtype="int64")
        dataset.attrs.create("dataset_attr", "Dataset Attribute")
        dataset.attrs.create("dataset_double_attr", np.float64(3.14159))

    return file_path
'''


def test_update_attribute(capsys, mock_hdf5_file):
    """Test that the update_attribute function updates the attribute value correctly."""
    from h5c.update import update_attribute

    update_attribute(mock_hdf5_file, "my_group", "my_attr", 42)

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' updated successfully." in captured.out
    assert "1 -> 42" in captured.out


def test_update_attribute_invalid_value(capsys, mock_hdf5_file):
    """Test that the update_attribute function prints an error message for an invalid value."""
    from h5c.update import update_attribute

    update_attribute(mock_hdf5_file, "my_group", "my_attr", "invalid_value")

    captured = capsys.readouterr()

    assert (
        "Error: Cannot cast 'invalid_value' to <class 'numpy.int64'>." in captured.out
    )


def test_remove_attribute(capsys, mock_hdf5_file):
    """Test that the remove_attribute function removes the attribute correctly."""
    from h5c.update import remove_attribute

    remove_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' removed from 'my_group' successfully." in captured.out


def test_remove_attribute_nonexistent(capsys, mock_hdf5_file):
    """Test that the remove_attribute function prints an error message for a non-existent attribute."""
    from h5c.update import remove_attribute

    target_path = "my_group"
    attr_name = "nonexistent_attr"
    remove_attribute(mock_hdf5_file, target_path, attr_name)

    captured = capsys.readouterr()

    assert f"Error: '{attr_name}' does not exist in '{target_path}'." in captured.err


def test_remove_attribute_nonexistent_target(capsys, mock_hdf5_file):
    """Test that the remove_attribute function prints an error message for a non-existent target path."""
    from h5c.update import remove_attribute

    target_path = "nonexistent_group"
    remove_attribute(mock_hdf5_file, target_path, "my_attr")

    captured = capsys.readouterr()

    assert f"Error: '{target_path}' does not exist." in captured.err


def test_remove_dataset(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function removes the dataset or group correctly."""
    from h5c.update import remove_dataset_or_group

    remove_dataset_or_group(mock_hdf5_file, "my_group/my_dataset")

    captured = capsys.readouterr()

    assert "Dataset 'my_group/my_dataset' removed successfully." in captured.out


def test_remove_group(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function removes the dataset or group correctly."""
    from h5c.update import remove_dataset_or_group

    remove_dataset_or_group(mock_hdf5_file, "my_group/my_subgroup")

    captured = capsys.readouterr()

    assert "Group 'my_group/my_subgroup' removed successfully." in captured.out


def test_remove_nonexistent(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function prints an error message for a non-existent path."""
    from h5c.update import remove_dataset_or_group

    remove_dataset_or_group(mock_hdf5_file, "nonexistent_path")

    captured = capsys.readouterr()

    assert "Error: Path 'nonexistent_path' does not exist." in captured.err
