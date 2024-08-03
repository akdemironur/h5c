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
        grp.attrs.create("my_attr", 1)  # Attribute with integer value
        grp.attrs.create(
            "my_string_attr", "Hello, World!"
        )  # Attribute with string value
        grp.attrs.create("my_float_attr", 3.14)  # Attribute with float value
        grp.attrs.create("my_bool_attr", True)  # Attribute with boolean value
        grp.attrs.create("my_double_attr", 2.71828)  # Attribute with double value

        # Create a subgroup
        subgrp = grp.create_group("my_subgroup")
        subgrp.attrs.create("subgroup_attr", "Subgroup Attribute")
        subgrp.attrs.create("subgroup_attr_int", 1)

        # Create a dataset
        dataset = grp.create_dataset("my_dataset", shape=(10,), dtype="int")
        dataset.attrs.create("dataset_attr", "Dataset Attribute")
        dataset.attrs.create(
            "dataset_double_attr", 3.14159
        )  # Attribute with double value

    return file_path


'''


def test_view_attribute(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints the correct output."""
    view_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()

    assert "my_attr: 1" in captured.out


def test_view_attribute_nonexistent(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints an error message for a non-existent attribute."""
    target_path = "my_group"
    attr_name = "nonexistent_attr"
    view_attribute(mock_hdf5_file, target_path, attr_name)

    captured = capsys.readouterr()

    assert f"Error: '{attr_name}' does not exist in '{target_path}'." in captured.err


def test_view_attribute_no_attr_name(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints all attributes when no attribute name is provided."""
    view_attribute(mock_hdf5_file, "my_group")

    captured = capsys.readouterr()

    assert "my_attr: 1" in captured.out
    assert "my_string_attr: Hello, World!" in captured.out
    assert "my_float_attr: 3.14" in captured.out
    assert "my_bool_attr: True" in captured.out
    assert "my_double_attr: 2.71828" in captured.out


def test_view_attribute_nonexistent_target(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints an error message for a non-existent target path."""
    target_path = "nonexistent_group"
    view_attribute(mock_hdf5_file, target_path)

    captured = capsys.readouterr()

    assert f"Error: '{target_path}' does not exist." in captured.err


def test_view_attribute_subgroup(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints the correct output for a subgroup."""
    view_attribute(mock_hdf5_file, "my_group/my_subgroup", "subgroup_attr")

    captured = capsys.readouterr()

    assert "subgroup_attr: Subgroup Attribute" in captured.out


def test_view_attribute_subgroup_int(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints the correct output for a subgroup."""
    view_attribute(mock_hdf5_file, "my_group/my_subgroup", "subgroup_attr_int")

    captured = capsys.readouterr()

    assert "subgroup_attr_int: 1" in captured.out


def test_view_attribute_dataset(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints the correct output for a dataset."""
    view_attribute(mock_hdf5_file, "my_group/my_dataset", "dataset_attr")

    captured = capsys.readouterr()

    assert "dataset_attr: Dataset Attribute" in captured.out


def test_view_attribute_dataset_double(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints the correct output for a dataset."""
    view_attribute(mock_hdf5_file, "my_group/my_dataset", "dataset_double_attr")

    captured = capsys.readouterr()

    assert "dataset_double_attr: 3.14159" in captured.out


def test_view_attribute_dataset_nonexistent(capsys, mock_hdf5_file):
    """Test that the view_attribute function prints an error message for a non-existent attribute."""
    target_path = "my_group/my_dataset"
    attr_name = "nonexistent_attr"
    view_attribute(mock_hdf5_file, target_path, attr_name)

    captured = capsys.readouterr()

    assert f"Error: '{attr_name}' does not exist in '{target_path}'." in captured.err


def test_explore_hdf5(capsys, mock_hdf5_file):
    """Test that the explore_hdf5 function prints the correct output."""
    with h5py.File(mock_hdf5_file, "r") as file:
        explore_hdf5(file)
    captured = capsys.readouterr()

    assert "|-- Group: /my_group" in captured.out
    assert "|   |-- Attribute: my_attr (int64): 1" in captured.out
    assert "|   |-- Attribute: my_string_attr (str): Hello, World!" in captured.out
    assert "|   |-- Attribute: my_float_attr (float32): 3.14" in captured.out
    assert "|   |-- Attribute: my_bool_attr (bool_): True" in captured.out
    assert "|   |-- Attribute: my_double_attr (float64): 2.71828" in captured.out
    assert "|   |-- Group: /my_group/my_subgroup" in captured.out
    assert (
        "|   |   |-- Attribute: subgroup_attr (str): Subgroup Attribute" in captured.out
    )
    assert "|   |   |-- Attribute: subgroup_attr_int (int32): 1" in captured.out
    assert "|   |-- Dataset: my_dataset" in captured.out
    assert "|   |   |-- Datatype: int64" in captured.out
    assert "|   |   |-- Shape: (10,)" in captured.out
    assert (
        "|   |   |--   Attribute: dataset_attr (str): Dataset Attribute" in captured.out
    )
    assert (
        "|   |   |--   Attribute: dataset_double_attr (float64): 3.14159"
        in captured.out
    )
