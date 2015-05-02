from setuptools import setup
import {{ cookiecutter.repo_name }}

setup(name="{{ cookiecutter.repo_name }}",
      version={{ cookiecutter.repo_name }}.__version__,
      packages=["{{ cookiecutter.repo_name}}"]
)
