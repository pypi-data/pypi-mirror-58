from setuptools import setup, find_packages


LONG_DESCRIPTION = open('README.md').read()

INSTALL_REQUIRES = [
    'google-api-python-client',
    'google-auth-httplib2',
    'setuptools'
]


setup(
    name='hangouts-helper',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Helper Python classes for handling and responding to Hangouts Chat events',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='http://github.com/christippett/hangouts-helper',
    author='Chris Tippett',
    author_email='c.tippett@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
