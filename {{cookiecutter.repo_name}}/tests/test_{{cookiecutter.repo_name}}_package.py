"""Test the {{ cookiecutter.repo_name }} package."""


def test_version_is_string():
    import {{ cookiecutter.repo_name }}
    assert isinstance({{ cookiecutter.repo_name }}.__version__, str)
