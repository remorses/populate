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
    ---
    ${{ None }}
    """
    print(populate_string(s, do_repr=True))
def test_python():
    s = """
class Ciao:
    "${{
        (
            "heeeey"
        )
    }}"
    def ${{cosa}}():
        return ${{ret}} or ${{ret}}
    "${{ return_iterpolated() }}"
    """
    x = populate_string(s, dict(cosa='func', ret='True', return_iterpolated=lambda: '${{ ciao }}'))
    print(x)
    # exec(x)
