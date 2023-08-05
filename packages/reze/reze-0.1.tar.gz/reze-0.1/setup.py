from setuptools import setup, find_packages

setup(
    name='reze',

    version='0.1',

    description='Recommendation service API',

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
