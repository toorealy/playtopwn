from setuptools import find_packages, setup


setup(
    name='playtopwn',
    version='0.1.1',
    description='Interactive guide to hacking boxes',
    license='LICENSE',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'playtopwn = playtopwn.game:the_beginning',
        ],
    }
)
