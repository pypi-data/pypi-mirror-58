import os
import io
from setuptools import setup, find_packages

VERSION = '0.0.2'

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='py-snake',
    version=VERSION,
    author='Jake Hadar',
    author_email='jakehadar.dev@gmail.com',
    description='CLI Snake game.',
    url='https://github.com/jakehadar/py-snake',
    python_requires='>=2.7',
    include_package_data=True,
    long_description=io.open(os.path.join(here, 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords='snake game python cli command line',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment :: Arcade',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    install_requires=io.open(os.path.join(here, 'requirements.txt'), encoding='utf-8').readlines(),
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['snake=snake.run:main']
    }
)
