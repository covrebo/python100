from hello import hello_name

def test_hello_name():
    assert hello_name('clark') == 'hello, clark'