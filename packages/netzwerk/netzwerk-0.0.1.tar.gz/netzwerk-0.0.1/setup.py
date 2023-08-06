import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='netzwerk',
    version='0.0.1',
    author='Noel Kaczmarek',
    author_email='noel.kaczmarek@gmail.com',
    description='Peer to peer decentralised networking package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NoelKaczmarek/P2P',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)