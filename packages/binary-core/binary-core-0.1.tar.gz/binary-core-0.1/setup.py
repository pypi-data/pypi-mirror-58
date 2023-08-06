from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name='binary-core',
    version='0.1',
    license='MIT',
    description=description,
    author='Tom Gringauz',
    author_email='tomgrin10@gmail.com',
    url='https://github.com/tomgrin10/binary-core',
    packages=find_packages(),
    install_requires=[
        'six'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
