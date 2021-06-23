import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'clairvoyance',
    packages = ["clairvoyance"],
    version = '1.0.0',
    license='MIT',
    description = 'The official Presage Python wrapper, a straightforward cryptocurrency prediction service.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/clairvoyance',
    download_url = 'https://github.com/rmaniego/clairvoyance/archive/v1.0.tar.gz',
    keywords = ['presage', 'cryptocurrency', 'prediction', 'python', 'wrapper'],
    install_requires=["requests", "arkivist"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)