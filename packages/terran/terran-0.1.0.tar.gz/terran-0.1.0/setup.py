import os

from setuptools import setup, find_packages


INSTALL_REQUIRES = [
    'click',
    'ffmpeg-python',
    'lycon',
    'numpy',
    'pycairo',
    'requests',
    'scikit-image',
    'sklearn',
    'torch',
    'torchvision',
]

# Dependencies that are to be removed if the environment is `READTHEDOCS`, so
# we don't run into troubles trying to install unsupported C-extensions. The
# list should match `autodoc_mock_imports` in `docs/conf.py`, but with the
# package names instead of the top-level modules.
MOCKED_IN_DOCS = [
    'lycon',
    'pycairo',
]

if os.environ.get('READTHEDOCS'):
    INSTALL_REQUIRES = list(
        set(INSTALL_REQUIRES) - set(MOCKED_IN_DOCS)
    )

setup(
    name='terran',
    version='0.1.0',

    author='Agustín Azzinnari',
    author_email='me@nagitsu.com',
    url='https://github.com/nagitsu/terran',

    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,

    entry_points="""
        [console_scripts]
        terran=terran:cli
    """,

    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
