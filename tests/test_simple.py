from populate import populate_string


def test_ready():
    assert True


def test_yaml():
    s = """
    ciao: ok
    other: 
        key: ${{
                str(
                    'sdfsdf"sdfsdf'
                )
            }}
        another:
            obj:
                ciao: 4
    another: ok ok
    """
    print(populate_string(s, do_repr=True))
def test_python():
    s = """
class Ciao:
    def ${{cosa}}():
        return ${{ret}}
    """
    x = populate_string(s, dict(cosa='func', ret='True'))
    print(x)
    exec(x)
