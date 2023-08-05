import io
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='py-snake',
    version=VERSION,
    author='Jake Hadar',
    author_email='jakehadar.dev@gmail.com',
    description='CLI Snake game.',
    url='https://github.com/jakehadar/py-snake',
    python_requires='>=2.7',
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords='snake game python cli command line',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    install_requires=io.open('requirements.txt', encoding='utf-8').readlines(),
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['snake=snake.run:main']
    }
)
