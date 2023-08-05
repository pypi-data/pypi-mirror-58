from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='reze',

    version='0.2',

    description='Recommendation service API',

    long_description=long_description,

    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='http://ftech.ai',

    # Author details
    author='FTech Team',
    author_email='tungdt@ftech.ai',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='recommendation engine as a service',

    packages=find_packages(),

    install_requires=['requests'],

)
