from setuptools import setup

setup(name='graphio',
      version='0.0.2',
      description='Library to load data sets to Neo4j.',
      url='http://github.com/kaiser_preusse',
      author='Martin Preusse',
      author_email='martin.preusse@gmail.com',
      license='APACHE v2',
      packages=['graphio'],
      install_requires=[
          'neo4j', 'py2neo'
      ],
      keywords=['NEO4J'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers'
      ],
      )
