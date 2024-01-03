from setuptools import setup, find_namespace_packages


setup(name ="census-income",
      version = "0.0.1",
      author = "Linga",
      author_email = "lingasodana25@gmail.com",
      packages=find_namespace_packages(),
      install_requires=["pandas", "numpy", "flask"]
      )