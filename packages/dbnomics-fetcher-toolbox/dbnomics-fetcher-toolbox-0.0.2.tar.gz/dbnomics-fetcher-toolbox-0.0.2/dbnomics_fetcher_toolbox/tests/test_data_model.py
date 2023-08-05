import pytest
from pydantic import ValidationError

from dbnomics_fetcher_toolbox.data_model import Category, write_series_jsonl


def test_Category__no_code_no_name():
    with pytest.raises(ValidationError):
        Category()


def test_write_series_jsonl__no_series(tmp_path):
    write_series_jsonl(tmp_path, [])
    file = tmp_path / "series.jsonl"
    assert file.is_file()
    assert file.read_text() == ""


def test_write_jsonl__some_series(tmp_path):
    write_series_jsonl(tmp_path, [{"code": "A.FR"}, {"code": "A.DE"}])
    file = tmp_path / "series.jsonl"
    assert file.is_file()
    assert (
        file.read_text() == '{"code":"A.DE"}\n{"code":"A.FR"}\n'
    ), "Series must be sorted by code"
