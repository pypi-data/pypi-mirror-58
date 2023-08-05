from dbnomics_fetcher_toolbox.formats import write_jsonl


def test_write_jsonl__no_items(tmp_path):
    file = tmp_path / "my.jsonl"
    write_jsonl(file, [])
    assert file.is_file()
    assert file.read_text() == ""


def test_write_jsonl__some_items(tmp_path):
    file = tmp_path / "my.jsonl"
    write_jsonl(file, [{"a": 1}, {"b": "hi"}])
    assert file.is_file()
    assert file.read_text() == '{"a":1}\n{"b":"hi"}\n'
