from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stock-research',
    version='0.1.0',
    description='Tool to review/find companies based primarily on past performance.',
    long_description=readme,
    author='Levi Balling',
    author_email='leviballing@gmail.com',
    url='https://github.com/AshitakaLax/stock-research',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)