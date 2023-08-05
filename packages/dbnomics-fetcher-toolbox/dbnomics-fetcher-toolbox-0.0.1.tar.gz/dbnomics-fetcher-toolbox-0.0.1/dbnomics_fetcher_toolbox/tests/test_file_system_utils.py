import pytest

from dbnomics_fetcher_toolbox.file_system_utils import iter_child_directories


@pytest.fixture
def dummy_dataset_dir(tmp_path):
    dir2 = tmp_path / "dir2"
    dir2.mkdir()
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    hidden_dir = tmp_path / ".hidden_dir"
    hidden_dir.mkdir()
    (tmp_path / "file1").write_text("hi")
    return tmp_path


def test_iter_child_directories__default(dummy_dataset_dir):
    """Test that child directories are yielded alphabetically."""
    assert list(iter_child_directories(dummy_dataset_dir)) == [
        dummy_dataset_dir / "dir1",
        dummy_dataset_dir / "dir2",
    ]


def test_iter_child_directories__include_hidden(dummy_dataset_dir):
    assert list(iter_child_directories(dummy_dataset_dir, include_hidden=True)) == [
        dummy_dataset_dir / ".hidden_dir",
        dummy_dataset_dir / "dir1",
        dummy_dataset_dir / "dir2",
    ]
