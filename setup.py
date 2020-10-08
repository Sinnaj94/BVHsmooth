import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='BVHSmooth',
    version='0.1',
    author='Virgínia Balbo',
    description='Smoothen your BVH Files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/Sinnaj94/BVHsmooth',
    python_requires='>=3.6',
)