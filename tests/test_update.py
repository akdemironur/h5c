from h5c.view import view_attribute
from h5c.update import update_attribute, remove_attribute, remove_dataset_or_group
from .test_mock_hdf5 import mock_hdf5_file


def test_update_attribute(capsys, mock_hdf5_file):
    """Test that the update_attribute function updates the attribute value correctly."""

    update_attribute(mock_hdf5_file, "my_group", "my_attr", 42)

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' updated successfully." in captured.out
    assert "1 -> 42" in captured.out


def test_update_attribute_invalid_value(capsys, mock_hdf5_file):
    """Test that the update_attribute function prints an error message for an invalid value."""

    update_attribute(mock_hdf5_file, "my_group", "my_attr", "invalid_value")

    captured = capsys.readouterr()

    assert (
        "Error: Cannot cast 'invalid_value' to <class 'numpy.int64'>." in captured.out
    )


def test_remove_attribute(capsys, mock_hdf5_file):
    """Test that the remove_attribute function removes the attribute correctly."""

    remove_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' removed from 'my_group' successfully." in captured.out


def test_remove_attribute_nonexistent(capsys, mock_hdf5_file):
    """Test that the remove_attribute function prints an error message for a non-existent attribute."""

    target_path = "my_group"
    attr_name = "nonexistent_attr"
    remove_attribute(mock_hdf5_file, target_path, attr_name)

    captured = capsys.readouterr()

    assert f"Error: '{attr_name}' does not exist in '{target_path}'." in captured.err


def test_remove_attribute_nonexistent_target(capsys, mock_hdf5_file):
    """Test that the remove_attribute function prints an error message for a non-existent target path."""

    target_path = "nonexistent_group"
    remove_attribute(mock_hdf5_file, target_path, "my_attr")

    captured = capsys.readouterr()

    assert f"Error: '{target_path}' does not exist." in captured.err


def test_remove_dataset(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function removes the dataset or group correctly."""

    remove_dataset_or_group(mock_hdf5_file, "my_group/my_dataset")

    captured = capsys.readouterr()

    assert "Dataset 'my_group/my_dataset' removed successfully." in captured.out


def test_remove_group(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function removes the dataset or group correctly."""

    remove_dataset_or_group(mock_hdf5_file, "my_group/my_subgroup")

    captured = capsys.readouterr()

    assert "Group 'my_group/my_subgroup' removed successfully." in captured.out


def test_remove_nonexistent(capsys, mock_hdf5_file):
    """Test that the remove_dataset_or_group function prints an error message for a non-existent path."""

    remove_dataset_or_group(mock_hdf5_file, "nonexistent_path")

    captured = capsys.readouterr()

    assert "Error: Path 'nonexistent_path' does not exist." in captured.err


def test_update_attribute_view(capsys, mock_hdf5_file):
    """Test that the update_attribute function updates the attribute value correctly and can be viewed."""

    update_attribute(mock_hdf5_file, "my_group", "my_attr", 42)

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' updated successfully." in captured.out
    assert "1 -> 42" in captured.out

    # Verify the updated attribute value using the view_attribute function
    view_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()

    assert "my_attr: 42" in captured.out


def test_remove_attribute_view(capsys, mock_hdf5_file):
    """Test that the remove_attribute function removes the attribute correctly and can be viewed."""

    remove_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()

    assert "Attribute 'my_attr' removed from 'my_group' successfully." in captured.out

    # Verify that the attribute is no longer present using the view_attribute function
    view_attribute(mock_hdf5_file, "my_group", "my_attr")

    captured = capsys.readouterr()
    print(captured.err)
    assert "Error: 'my_attr' does not exist in 'my_group'." in captured.err
