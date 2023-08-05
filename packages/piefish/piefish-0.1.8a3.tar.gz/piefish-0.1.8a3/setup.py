from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='piefish',
      version='0.1.8a3',
      description='A 2D graphics API that mimics the Processing API',
      url='http://github.com/pb2002/PyVis',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Pepijn Bakker',
      author_email='bakker.pepijn@gmail.com',
      license='MIT',
      packages=find_packages(),
	  install_requires=[
          'pygame',
		  'colorama'
      ],
      zip_safe=True)
      