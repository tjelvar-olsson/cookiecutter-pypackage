from setuptools import setup

url = ""
version = "{{ cookiecutter.version }}"
readme = open('README.rst').read()

setup(name="{{ cookiecutter.repo_name }}",
      packages=["{{ cookiecutter.repo_name}}"],
      version=version,
      description="{{ cookiecutter.description }}",
      long_description=readme,
      include_package_data=True,
      author="{{ cookiecutter.author }}",
      author_email="{{ cookiecutter.author_email }}",
      url=url,
      download_url="{}/tarball/{}".format(url, version),
      license="MIT")
