from setuptools import setup, find_packages

setup(
    name='qtypi',  # Make sure the package name is unique and valid
    version='0.1.0',
    description='A Python library for quantum state manipulations and quantum gates',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Include the content type
    author='Pearl',
    author_email = 'pearl207@gmail.com',
    url='https://github.com/pearlpatel207/qtypi',  # Your project's URL
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
