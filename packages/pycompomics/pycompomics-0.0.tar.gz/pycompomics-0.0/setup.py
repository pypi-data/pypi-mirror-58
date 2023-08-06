import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
        name          = 'pycompomics',
        version       = '0.0',
        description   = 'wrapper for the Compomics suite of MS tools',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author        = 'sebastien Leblanc',
        author_email  = 'sebastien.leblanc5@usherbrooke.ca',
        license       = 'MIT',
        packages      = setuptools.find_packages(),
        python_requires='>=3.6'
    )
