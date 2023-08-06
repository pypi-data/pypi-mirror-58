from setuptools import find_packages, setup


package_name = 'python-pypi-example'
version = '0.0.3'
classifiers = [
    'Development Status :: 1 - Planning',

    'Intended Audience :: Developers',

    'Programming Language :: Python :: 3.6',
]

setup(
    name=package_name,
    version=version,
    packages=find_packages(),
    classifiers=classifiers,
    author='Guy King',
    author_email='grking8@gmail.com',
    license='MIT',
    url='https://github.com/family-guy/python-pypi-example.git',
)
