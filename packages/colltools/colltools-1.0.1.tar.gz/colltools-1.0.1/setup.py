from setuptools import setup, find_packages
from os import path


with open('requirements-test.txt') as fp:
    extras_require = fp.read()

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='colltools',
    version='1.0.1',
    python_requires='>=3.6',
    description='Tools for iterating and working with collections',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/JakubTesarek/colltools',
    author='Jakub Tesárek',
    author_email='jakub@tesarek.me',
    license='APACHE LICENSE 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers'
    ],
    keywords='itertools collections iteration',
    packages=find_packages(),
    extras_require={'test': extras_require}
)
