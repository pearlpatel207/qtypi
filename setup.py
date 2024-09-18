from setuptools import setup, find_packages

setup(
    name='qtypi',
    version='0.1.0',
    description='A Python library for quantum state manipulations and quantum gates',
    author='Your Name',
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
