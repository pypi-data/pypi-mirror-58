from setuptools import find_packages, setup

setup(
    name='brewblox-devcon-spark',
    use_scm_version={'local_scheme': lambda v: ''},
    description='Communication with Spark controllers',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/BrewBlox/brewblox-devcon-spark',
    author='BrewPi',
    author_email='Development@brewpi.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Framework :: AsyncIO',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Hardware',
    ],
    license='GPLv3',
    keywords='brewing brewpi brewblox embedded controller spark service',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'brewblox-service',
        'dpath',
        'pyserial-asyncio',
        'construct',
        'protobuf',
        'pint',
        'aiofiles',
        'aiohttp-sse',
        'schema',
    ],
    python_requires='>=3.7',
    setup_requires=['setuptools_scm'],
)
