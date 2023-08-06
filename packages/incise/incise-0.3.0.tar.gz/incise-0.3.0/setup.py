import setuptools
import itertools

with open('README.rst') as file:

    readme = file.read()

name = 'incise'

version = '0.3.0'

author = 'Exahilosys'

url = f'https://github.com/{author}/{name}'

setuptools.setup(
    name = name,
    version = version,
    url = url,
    packages = setuptools.find_packages(),
    license = 'MIT',
    description = 'Live Segmentation Framework.',
    long_description = readme,
    install_requires = [
        'docopt'
    ],
    extras_require = {
        'docs': [
            'sphinx',
            'sphinx_rtd_theme'
        ]
    },
    entry_points = {
        'console_scripts': [
            f'{name} = {name}.console:serve',
        ]
    }
)
