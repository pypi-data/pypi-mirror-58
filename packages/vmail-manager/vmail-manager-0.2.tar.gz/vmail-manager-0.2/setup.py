from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='vmail-manager',
    version='0.2',
    author='Dominik Rimpf',
    author_email='dev@d-rimpf.de',
    description='Handy cli interface to manage an vmail-sql-db.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/domrim/vmail-manager/',
    packages=['vmail_manager'],
    package_data={
        'vmail_manager': ['config_default.yaml'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    platforms=[
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.6',
    install_requires=[
        'click>=7.0',
        'sqlalchemy>=1.3.8',
        'pymysql>=0.9.3',
        'tabulate>=0.8.5',
        'argon2_cffi>=19.1.0',
        'confuse>=1.0.0',
    ],
    entry_points='''
    [console_scripts]
    vmail-manager=vmail_manager:cli
    ''',
)
