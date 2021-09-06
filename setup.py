import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="normalizer",
    version="0.0.1",
    description="Normalizer for bengali / english text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['normalizer'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python'
    ],
    install_requires=[
        "regex",
        "emoji==1.4.2",
        "ftfy==6.0.3"
    ],
    package_data={'': ['*']},
    python_requires='>=3.5',
)