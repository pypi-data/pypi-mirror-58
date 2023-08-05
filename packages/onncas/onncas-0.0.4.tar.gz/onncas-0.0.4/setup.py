from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()


setup(
    name='onncas',
    version='0.0.4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='http://oznetnerd.com',
    install_requires=install_requires,
    license='',
    author='Will Robinson',
    author_email='will@oznetnerd.com',
    description='Convenience module for interacting with Trend Micro Cloud App Security (CAS)'
)