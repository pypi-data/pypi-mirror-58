from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vrt_generator',
    version='0.0.6',
    packages=['vrt'],
    url='https://github.com/miweru/vrt_generator',
    license='',
    author='Michael Ruppert',
    author_email='michael.ruppert@fau.de',
    description='creating vrt corpora',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "smart_open>=1.9.0",
    ],
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
)
