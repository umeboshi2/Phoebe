import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'colander>=0.9.9.1dev',
    'deform>=0.9.6dev',
    'trumpet>=0.1dev',
    'hubby>=0.0dev',
    ]

setup(name='Phoebe',
      version='0.0',
      description='Phoebe',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='phoebe',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = phoebe:main
      [console_scripts]
      initialize_Phoebe_db = phoebe.scripts.initializedb:main
      """,
      dependency_links=[
        'https://github.com/umeboshi2/trumpet/archive/master.tar.gz#egg=trumpet-0.1.1dev',
        'https://github.com/umeboshi2/hubby/archive/master.tar.gz#egg=hubby-0.0dev',
      'https://github.com/umeboshi2/deform/archive/master.tar.gz#egg=deform-0.9.6dev',
      'https://github.com/Pylons/colander/archive/master.tar.gz#egg=colander-0.9.9.1dev',
        ],
      )

