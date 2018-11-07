import {{cookiecutter.project_name}}
import pytest


def test_greeting():
    assert {{cookiecutter.project_name}}.greeting("John") == "Hello, John!"


def test_greeting_en():
    assert {{cookiecutter.project_name}}.greeting("John", "en") == "Hello, John!"


def test_greeting_de():
    assert {{cookiecutter.project_name}}.greeting("John", "de") == "Hallo, John!"


def test_greeting_unknown_lang():
    with pytest.raises(ValueError):
        {{cookiecutter.project_name}}.greeting("John", "fr")


@pytest.mark.parametrize("argv, lang, name", [
    (["John"], "en", "John"),
    (["-l", "en", "John"], "en", "John"),
    (["-l", "de", "John"], "de", "John"),
    (["John Doe"], "en", "John Doe"),
])
def test_parse_args(argv, lang, name):
    args = {{cookiecutter.project_name}}.parse_args(argv)
    assert args.name == name
    assert args.language == lang


def test_main(capsys):
    ret = {{cookiecutter.project_name}}.main(["-l", "en", "John"])
    assert ret == 0
    captured = capsys.readouterr()
    assert captured[0] == "Hello, John!\n"  # stdout
    assert captured[1] == ""  # stderr
