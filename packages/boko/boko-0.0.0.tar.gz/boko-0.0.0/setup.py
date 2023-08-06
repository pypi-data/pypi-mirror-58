from setuptools import setup, find_packages

PACKAGE_NAME = 'boko'
AUTHOR = 'HoangTien Le (SamKunio)'
AUTHOR_EMAIL = 'samkunio@gmail.com'
DESCRIPTION = ''
LONG_DESCRIPTION = ''
VERSION = '0.0.0'
LICENSE = 'BSD'
URL = ''
DOWNLOAD_URL = ''
PROJECT_URLS = {
    'Bug Tracker': 'https://github.com/samkunio/boko/issues',
    'Source Code': 'https://github.com/samkunio/boko',
}
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Cython',
    'Topic :: Scientific/Engineering',
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,    
    packages=find_packages(),  
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",    
    url=URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,    
    classifiers=CLASSIFIERS,
    platforms='any',
    python_requires='>=3.6.1',    
)