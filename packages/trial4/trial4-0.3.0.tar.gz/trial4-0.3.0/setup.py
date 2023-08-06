"""Setup for the trial4 package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Pooja Agicha",
    author_email="pooja.m.agicha@gmail.com",
    name='trial4',
    license="MIT",
    description='trial4 is a python package for basic mathematical calculations .',
    version='v0.3.0',
    long_description=README,
    url='https://github.com/poojaagicha/trial1',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)