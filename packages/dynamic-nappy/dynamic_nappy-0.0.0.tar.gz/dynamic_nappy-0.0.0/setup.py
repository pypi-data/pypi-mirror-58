import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except Exception as e:
    import sys
    import traceback
    print(e)
    traceback.print_exc()
    sys.exit(1)


setuptools.setup(
    name='dynamic_nappy',
    version='0.0.0',
    author='Rodney Meredith McKay',
    # author_email='',
    description='dynamic non-atomic parser (python)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ep12/dynamic_nappy',
    packages=setuptools.find_packages(where='src'),
    license='GNU AGPL v3',
    keywords=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Typing :: Typed',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    python_requires='>=3.6',
    install_requires=[
    ]
)
