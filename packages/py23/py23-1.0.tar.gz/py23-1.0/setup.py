import setuptools


long_description = """
# Py23

Python 2/3 compatible functions pack
"""

setuptools.setup(
    name = 'py23',
    version = '1.0',
    author = 'Vitaly Bogomolov',
    author_email = 'mail@vitaly-bogomolov.ru',
    description = 'Python 2/3 compatible functions pack',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/vb64/py23',
    packages = ['py23'],
    download_url = 'https://github.com/vb64/py23/archive/v1.0.tar.gz',
    keywords = ['python', 'load_module_by_path'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
