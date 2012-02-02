import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="Grenada_geonode",
    version="0.1",
    author="Kenton Fletcher",
    author_email="kenflet@hotmail.com",
    description="Sample project",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: BSD',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://git@github.com:kenflet/Grenada_geonode.git',
    scripts = [
               'scripts/Grenada_geonode',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
