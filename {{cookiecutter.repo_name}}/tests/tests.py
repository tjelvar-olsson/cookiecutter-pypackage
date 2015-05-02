import unittest

class UnitTests(unittest.TestCase):

    def test_can_import_package(self):
        # Raises import error if the package cannot be imported.
        import {{ cookiecutter.repo_name }}

    def test_package_has_version_string(self):
        import {{ cookiecutter.repo_name }}
        self.assertTrue(isinstance({{ cookiecutter.repo_name}}.__version__, str))


if __name__ == "__main__":
    unittest.main()
