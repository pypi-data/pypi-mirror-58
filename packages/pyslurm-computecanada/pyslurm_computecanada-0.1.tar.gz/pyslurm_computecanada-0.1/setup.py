import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
        name          = 'pyslurm_computecanada',
        version       = '0.1',
        description   = 'wrapper for slurm job manager on compute canada clusters',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author        = 'sebastien Leblanc',
        author_email  = 'sebastien.leblanc5@usherbrooke.ca',
        license       = 'MIT',
        packages      = setuptools.find_packages(),
        python_requires='>=3.6'
    )
