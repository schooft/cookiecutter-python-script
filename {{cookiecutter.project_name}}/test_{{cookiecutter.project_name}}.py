from {{cookiecutter.project_name}} import greeting, parse_args, main
import pytest


def test_greeting():
    assert greeting("John") == "Hello, John!"


def test_greeting_en():
    assert greeting("John", "en") == "Hello, John!"


def test_greeting_de():
    assert greeting("John", "de") == "Hallo, John!"


def test_greeting_unknown_lang():
    with pytest.raises(ValueError):
        greeting("John", "fr")


@pytest.mark.parametrize("argv, lang, name", [
    (["John"], "en", "John"),
    (["-l", "en", "John"], "en", "John"),
    (["-l", "de", "John"], "de", "John"),
    (["John Doe"], "en", "John Doe"),
])
def test_parse_args(argv, lang, name):
    args = parse_args(argv)
    assert args.name == name
    assert args.language == lang


def test_main(capsys):
    ret = main(["-l", "en", "John"])
    assert ret == 0
    captured = capsys.readouterr()
    assert captured[0] == "Hello, John!\n"  # stdout
    assert captured[1] == ""  # stderr
