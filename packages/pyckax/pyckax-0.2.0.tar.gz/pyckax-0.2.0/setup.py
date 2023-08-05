import setuptools

with open('readme.md', 'r') as reader:
    long_description = reader.read()

setuptools.setup(
    name='pyckax',
    version='0.2.0',
    description='yet a crawl library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='chaosannals',
    author_email='chaosannals@outlook.com',
    url='https://github.com/chaosannals',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
    ],
)