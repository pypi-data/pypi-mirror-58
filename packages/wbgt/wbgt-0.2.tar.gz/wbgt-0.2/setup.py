from distutils.core import setup
setup(
  name = 'wbgt',
  packages = ['wbgt'],
  version = '0.2',
  license='',
  description = 'calculate WBGT',
  author = 'satotake',
  author_email = 'doublequotation@gmial.com',
  url = 'https://github.com/satotake/wbgt-py',
  download_url = 'https://github.com/satotake/wbgt-py/archive/v_01.tar.gz',
  keywords = ['climate', 'WBGT', 'meteorology'],
  install_requires=[
       'numpy',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
