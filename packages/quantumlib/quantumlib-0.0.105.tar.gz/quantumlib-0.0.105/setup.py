__version__ = '0.0.105'

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='quantumlib',
    version=__version__,
    author='Altertech',
    author_email='div@altertech.com',
    description='Quantum calculations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alttch/quantumlib',
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
    ),
)
