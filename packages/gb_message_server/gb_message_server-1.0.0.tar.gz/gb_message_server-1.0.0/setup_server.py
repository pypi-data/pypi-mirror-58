from setuptools import setup, find_packages

setup(name="gb_message_server",
      version="1.0.0",
      description="messanger_server",
      author="Oleg Spresov",
      author_email="spoliv@rambler.ru",
      packages=find_packages(),
      install_requires=['Click', 'PyQt5', 'sqlalchemy', 'pycryptodome']
      )