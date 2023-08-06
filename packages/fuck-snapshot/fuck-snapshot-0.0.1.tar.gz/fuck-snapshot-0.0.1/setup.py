from setuptools import setup

setup(
    name='fuck-snapshot',
    version='0.0.1',
    author='jnddd',
    author_email='122296743@qq.com',
    description='a easy snap js',
    packages=['fuck_snapshot'],
    package_dir={'fuck_snapshot': 'fuck_snapshot'},
    package_data={'fuck_snapshot': ['snap.js']},
)