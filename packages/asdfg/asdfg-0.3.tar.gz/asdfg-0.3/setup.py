from setuptools import setup,find_packages

setup(
    name='asdfg',
    version='0.3',
    packages=find_packages(exclude=['documentation.txt']),
    package_dir={'':'asdfg'},
    url="http://www.example.com",
    license='',
    author='veera',
    author_email='veerabhadrarao.uppu@nexiilabs.com',
    description='asdfg_description',
    download_url="https://github.com/uvbr/package_creation/archive/0.3.tar.gz"
)