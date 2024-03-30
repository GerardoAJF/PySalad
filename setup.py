from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1'
DESCRIPTION = "pysalad is a simple python module that will allow you to encode and decode texts using the cesar cipher, the latter through basic statistics."
PACKAGE_NAME = 'pysalad'
AUTHOR = 'OwO programmer'
EMAIL = 'gerardoowo.jovelfranco@gmail.com'
GITHUB_URL = "https://github.com/GerardoAJF/PySalad"

setup (
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points ={ "console_scripts": ["pysalad=pysalad.__main__:main"]},
    version = VERSION,
    license = 'MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = ["cesar cipher", "coder", "decoder", "cryptography", "utilities"],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Build Tools'
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Environment :: Console'
    ]
)
