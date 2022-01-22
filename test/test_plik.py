from plik import dodawanie


def test_dodawanie():
    assert dodawanie(3, 4) == 7
    assert dodawanie(5, 6) == 11
    assert dodawanie(10, -5) == 5
