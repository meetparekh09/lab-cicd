from hello import hello_world


def test_hello_world():
    expected = "Hello World, Now I Use CI/CD"
    result = hello_world()
    assert expected == result
