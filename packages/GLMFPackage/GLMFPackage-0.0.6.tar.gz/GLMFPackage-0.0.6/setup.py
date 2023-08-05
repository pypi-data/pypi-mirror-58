# Version is automatically set from git
# More details here : https://pypi.org/project/setuptools-scm/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GLMFPackage", 
    # version="0.1",
    author="Fred",
    author_email="fritz.smh@gmail.com",
    description="A GLMF library package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://boutique.ed-diamond.com/",
    
    # Version from git
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    
    # Commands available from $PATH
    entry_points = {
        'console_scripts': ['glmfpackage-version=glmfpackage.version:print_version'],
    },
    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

