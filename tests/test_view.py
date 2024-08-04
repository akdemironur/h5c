import numpy as np
from h5c.view import view_attribute
from .test_mock_hdf5 import mock_hdf5_file


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


# TODO: Add tests for explore_hdf5
