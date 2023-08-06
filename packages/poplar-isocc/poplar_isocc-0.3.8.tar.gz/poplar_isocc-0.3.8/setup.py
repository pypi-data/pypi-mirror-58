from setuptools import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name='poplar_isocc',
    version='0.3.8',
    author='2665093 Ontario Inc.',
    url='https://2665093.ca',
    author_email='chris@2665093.ca',
    packages=['poplar_isocc'],
    package_data={
        '': ['vi/*.vi', 'expi.json' ],
        },
    description=("Enforce the use of ISO-3166-1 compliant country codes on any"
                 "View field."),
    long_description=readme,
    include_package_data=True,
    install_requires=[
        'extools',
        'iso3166',
        'fuzzywuzzy',
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
        "Orchid", "Extender", "Sage 300", "Automation", "Country", "Code",
        "ISO-3166", "ISO", "3166",
    ],
    download_url="https://pypi.org/project/poplar_isocc",
)
