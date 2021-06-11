from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent.parent / 'README.md'
if readme_file.exists():
    with readme_file.open() as f:
        long_description = f.read()
else:
    # When this is first installed in development Docker, README.md is not available
    long_description = ''

setup(
    name='django-rgd-imagery',
    version='0.1.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    url='https://github.com/ResonantGeoData/ResonantGeoData',
    keywords='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python',
    ],
    python_requires='>=3.8',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-rgd',
        'large-image>=1.6.0',
        'large-image-source-gdal>=1.6.0',
        'large-image-source-pil>=1.6.0',
        'numpy',
        'pystac[validation]',
        'rasterio',
        'shapely',
    ],
    extras_require={
        'worker': [
            'kwarray>=0.5.10',
            'kwcoco',
            'kwimage[headless]>=0.6.7',
            'large-image-converter',
        ],
    },
)