import re
from os import path
from setuptools import setup

VERSIONFILE = "initpkg/__init__.py"
with open(VERSIONFILE, "rt") as versionfle:
    verstrline = versionfle.read()
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(version_re, verstrline, re.M)
if mo:
    ver_str = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='initpkg',
      version=ver_str,
      description='python package creator',
      url='http://github.com/wlongxiang/initpkg',
      author='Benjamin Wang',
      author_email='wlongxiang1119@gmail.com',
      license='MIT',
      packages=['initpkg'],
      package_dir={'initpkg': 'initpkg'},
      package_data={'initpkg': ['template/**/*', "template/*", ]},
      include_package_data=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      entry_points={
          'console_scripts': [
              'initpkg=initpkg.cli:main',
          ],
      },

      )
