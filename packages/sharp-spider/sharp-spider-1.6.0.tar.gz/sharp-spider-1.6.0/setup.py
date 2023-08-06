from setuptools import setup, find_packages

setup(
    name='sharp-spider',
    version='1.6.0',
    description='Distributed crawler based on async tornado redis',
    license='Free',
    author='wangzongzhe',
    author_email='17184032534@163.com',
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    python_requires='>=3.6',
    install_requires=[
    'lxml',
    'bs4',
    'tornado',
    'bs4',
    'redis>=2.10.5',
    'uuid',
    'selenium',
    'requests',
    'six'
    ],
)
