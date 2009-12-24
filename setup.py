from os.path import join
from setuptools import setup, find_packages


version = '0.1'
history = open(join("docs", "HISTORY.txt")).read()
readme = open(join("src", "menhir", "library", "tablesorter", "README.txt")).read()

setup(name='menhir.library.tablesorter',
      version=version,
      description="Table sorting javascript resources for Grok",
      long_description="%s\n%s" % (readme, history),
      keywords='Table sorting javascript',
      author='Souheil Chelfouh',
      author_email='trollfot@gmail.com',
      url='',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['menhir', 'menhir.library'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'hurry.jquery',
          'megrok.resource',
          ],
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
