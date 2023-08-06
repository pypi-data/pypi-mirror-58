from distutils.core import setup
setup(
  name = 'sqlToDf',         # How you named your package folder (MyLib)
  packages = ['sqlToDf'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package utilize the bcp bulk functionality available in mssql-tools to import the the mssql data into pandas dataframe for analysis purposes',   # Give a short description about your library
  author = 'Sehan Ahmed Farooqui | Arsal Rahim',                   # Type in your name
  author_email = 'sehan_ahmed@live.com',      # Type in your E-Mail
  url = 'https://github.com/sehanfarooqui',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sehanfarooqui/sqlToDf/archive/SqlToDf_0.1.tar.gz',    # I explain this later on
  keywords = ['bcp', 'mssql', 'pandas dataframe','mssql-tools','mssql tables to Dataframes'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support

  ],
)
