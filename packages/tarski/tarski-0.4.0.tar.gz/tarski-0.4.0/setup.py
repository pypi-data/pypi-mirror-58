from setuptools import setup, find_packages
from codecs import open
from os import path
import importlib

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Load the version from ./src/tarski/version.py
spec = importlib.util.spec_from_file_location('tsk.version', path.join(here, 'src/tarski/version.py'))
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)


def main():

    setup(
        name='tarski',
        version=version.__version__,
        description='Tarski is a framework for the specification, modeling and manipulation of AI planning problems.',
        long_description=long_description,
        long_description_content_type='text/markdown',

        url='https://github.com/aig-upf/tarski',
        author='Miquel Ramírez and Guillem Francès',
        author_email='guillem.frances@unibas.ch',

        keywords='planning logic STRIPS RDDL',
        classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',

            'Topic :: Scientific/Engineering :: Artificial Intelligence',

            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],

        packages=find_packages('src'),  # include all packages under src
        package_dir={'': 'src'},  # tell distutils packages are under src


        install_requires=[
            'psutil',
            'antlr4-python3-runtime>=4.7.2',
            'numpy',
            'pyrddl',
        ],

        extras_require={
            'dev': ['pytest', 'tox', 'pytest-cov', 'mypy'],
            'test': ['pytest', 'tox', 'pytest-cov', 'mypy'],
            'doc': ['sphinx', 'recommonmark', 'nbsphinx', 'sphinx_rtd_theme', 'ipykernel', 'ipython'],
            'sdd': [
                'Cython',
                'PySDD>=0.2.9',  # This doesn't seem to fully install pysdd.sdd
                # 'pysdd@git+https://git@github.com/wannesm/PySDD.git@259e8b5',  # This doesn't seem to work on Travis
                # 'pysdd@https://github.com/wannesm/PySDD/archive/259e8b5.zip',  # This doesn't seem to work on Travis
                'cysignals'
            ],
            'scipy': ['scipy']
        },

        # This will include non-code files specified in the manifest, see e.g.
        # http://python-packaging.readthedocs.io/en/latest/non-code-files.html
        include_package_data=True,
    )


if __name__ == '__main__':
    main()
