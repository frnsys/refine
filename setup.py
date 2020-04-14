from setuptools import setup

setup(
    name='refine',
    version='0.0.1',
    description='tool for data processing pipelines',
    url='https://github.com/frnsys/refine',
    author='Francis Tseng',
    author_email='f@frnsys.com',
    license='MIT',

    packages=['refine'],
    install_requires=[
        'PyYAML==5.1',
        'click==6.2',
    ],
    entry_points='''
        [console_scripts]
        refine=refine.cli:refine
    ''',
)
