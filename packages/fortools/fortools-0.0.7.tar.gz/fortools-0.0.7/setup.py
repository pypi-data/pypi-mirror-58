from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fortools",
    version="0.0.7",
    author="5ha0",
    author_email="fortools.official@gmail.com",
    description="forensics python library fortools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/5ha0/fortools/fortools",
    download_url='https://github.com/5ha0/fortools/archive/master.zip',
    packages=find_packages(),
    python_requires='>3.5',
    install_requires=[
        'bitstring',
        'chardet',
        'image',
        'libesedb-python',
        'libevtx-python',
        'libewf-python',
        'lxml',
        'matplotlib',
        'numpy',
        'olefile',
        'PyPDF2',
        'python-docx',
        'python-magic',
        'python-magic-bin',
        'python-registry',
        'pytsk3',
        'xmltodict',
    ],
    classifiers=[
      "Programming Language :: Python :: 3",
    ],
)
