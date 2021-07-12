import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'shameni',
    packages = ["shameni"],
    version = '1.0.4',
    license='MIT',
    description = 'The official Python wrapper for Presage, a straightforward cryptocurrency prediction service.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/shameni',
    download_url = 'https://github.com/rmaniego/shameni/archive/v1.0.tar.gz',
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