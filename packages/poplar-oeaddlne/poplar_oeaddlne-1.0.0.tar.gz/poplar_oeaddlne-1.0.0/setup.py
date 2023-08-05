from setuptools import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name='poplar_oeaddlne',
    version='1.0.0',
    author='2665093 Ontario Inc.',
    url='https://2665093.ca',
    author_email='chris@2665093.ca',
    packages=['poplar_oeaddlne'],
    package_data={
        '': ['vi/*.vi', 'expi.json' ],
        },
    description=("Example Extender customization that adds an OE Order"
                 "line when a line with a particular item is entered."),
    long_description=readme,
    include_package_data=True,
    install_requires=[
    ],
    # Valid classifiers: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=[
        "Orchid", "Extender", "Sage 300", "Automation",
    ],
    download_url="https://pypi.org/project/poplar_oeaddlne",
)
