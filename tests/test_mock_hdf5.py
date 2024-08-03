import pytest
import h5py
import numpy as np


@pytest.fixture
def mock_hdf5_file(tmp_path):
    """Create a temporary HDF5 file with some attributes for testing."""
    file_path = tmp_path / "test.h5"
    with h5py.File(file_path, "w") as file:
        grp = file.create_group("my_group")
        grp.attrs.create("my_attr", np.int64(1))
        grp.attrs.create("my_string_attr", "Hello, World!")
        grp.attrs.create("my_float_attr", np.float32(3.14))
        grp.attrs.create("my_bool_attr", np.bool_(True))
        grp.attrs.create("my_double_attr", np.float64(2.71828))

        subgrp = grp.create_group("my_subgroup")
        subgrp.attrs.create("subgroup_attr", "Subgroup Attribute")
        subgrp.attrs.create("subgroup_attr_int", np.int32(1))

        dataset = grp.create_dataset("my_dataset", shape=(10,), dtype="int64")
        dataset.attrs.create("dataset_attr", "Dataset Attribute")
        dataset.attrs.create("dataset_double_attr", np.float64(3.14159))

    return file_path
