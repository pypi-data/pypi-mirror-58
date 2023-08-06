from setuptools import setup
from image2html import __package_name__, __version__, __author__, __email__, __url__, __description__

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    packages=[__package_name__],
    install_requires=["huster", "dominate", "numpy"],
    # scripts=['utils/build_server_scripts'],
    entry_points = {
              'console_scripts': [
                  'image2html = image2html.image2html:image2html',
                  'make_flist = image2html.flist:make_flist',
              ],
          },
    url=__url__,
    description=__description__,
    # long_description=open('./README.md', 'r').read(), 
    # long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)