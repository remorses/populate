from populate import populate_string


def test_1():
    s = '''
    def ${{ name }}():
        ${{
            'return ' + 'xxx' if horny else 'xoxoxo'
        }}

    ${{
        indent_to('    ', ''.join([
            """
            def fuck_you():
                return 'fucku'
            """ for i in range(3)
        ]))
    }}
    '''
    y = populate_string(s, dict(horny=True, name='boooo'))
    print(y)