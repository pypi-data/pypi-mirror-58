from distutils.core import setup
setup(
  name = 'devcon_win',         # How you named your package folder (MyLib)
  packages = ['devcon_win'],   # Chose the same as "name"
  version = '0.2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'With devcon_win, you can access all functions of devcon.exe. In addition, you can see all available drivers as a function.',
  # Give a short description about your library
  author = 'Shivanshu Srivastava',                   # Type in your name
  author_email = 'shivanshu26shiv@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Shivanshu26shiv/devcon_win',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Shivanshu26shiv/devcon_win/archive/v_02.2.tar.gz',    # I explain this later on
  keywords = ['devcon', 'hardware drivers', 'device drivers', 'drivers'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
