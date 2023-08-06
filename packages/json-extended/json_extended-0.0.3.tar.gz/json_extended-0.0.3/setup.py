import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='json_extended',
    version='0.0.3',
    author='Gyeongsu Yim',
    author_email='point1304@gmail.com',
    description='json module with ``datetime``, ``date`` and ``uuid`` support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/point1304/json_extended',
    packages=setuptools.find_packages(),
    include_package_data=True, #: Check MANIFEST.in for explicit rules
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)
