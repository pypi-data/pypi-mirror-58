"""In this file, we test to ensure that the output of
check_syntax is as expected.

We also test to ensure that check_syntax does not accidently
change any existing error handling settings.

"""

import friendly_traceback as friendly


def test_check_syntax():
    # set-up
    bad_code_syntax = "True = 1"
    bad_code_exec = "a = b"  # Not a syntax error, but a NameError
    good_code = "c = 1"

    friendly.set_stream("capture")
    original_level = friendly.get_level()
    installed = friendly.is_installed()
    # ----- end of set-up

    # When a SyntaxError is raised, check_syntax returns False

    assert not friendly.check_syntax(source=bad_code_syntax)
    result = friendly.get_output()  # content is flushed
    assert "Python exception" in result
    assert "SyntaxError" in result

    assert not friendly.get_output()  # confirm that content was flushed

    # When no SyntaxError is raised, check_syntax returns a tuple
    # containing a code object and a file name
    assert friendly.check_syntax(source=bad_code_exec)
    assert friendly.check_syntax(source=good_code)
    assert not friendly.get_output()  # no new exceptions recorded

    try:
        exec(bad_code_syntax, {})
    except Exception:
        assert not friendly.get_output()

    # When friendly-traceback is not installed, a call to check_syntax
    # will end with level set to 0, which corresponds to normal Python
    # tracebacks
    friendly.uninstall()
    friendly.check_syntax(source=bad_code_syntax)
    assert friendly.get_level() == 0
    friendly.check_syntax(source=bad_code_syntax, level=4)
    assert friendly.get_level() == 0

    # When friendly-traceback is "installed", a call to check_syntax
    # leaves its level unchanged.
    friendly.install()

    friendly.set_level(3)
    friendly.check_syntax(source=bad_code_syntax)
    assert friendly.get_level() == 3
    friendly.check_syntax(source=bad_code_syntax, level=4)
    assert friendly.get_level() == 3

    # Clean up and restore for other tests
    friendly.get_output()
    friendly.set_stream(None)
    if installed:
        friendly.uninstall()
    friendly.set_level(original_level)


if __name__ == "__main__":
    test_check_syntax()
    print("Success!")
