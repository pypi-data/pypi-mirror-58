import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'nag_b2b_api_HalfBottleOfMind',
    version = '0.0.1.dev4',
    author = 'HalfBottleOfMind',
    author_email = 'andromalak222@gmail.com',
    description = 'Library for processing data from https://b2b-api.nag.ru/api',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/halfbottleofmind/nag-b2b-api',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)