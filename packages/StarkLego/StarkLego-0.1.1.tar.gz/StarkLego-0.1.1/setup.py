from distutils.core import setup
setup(
    name = 'StarkLego',         # How you named your package folder (MyLib)
    packages = ['StarkLego', 'StarkLego.environments', 'StarkLego.lego_builders'],   # Chose the same as "name"
    version = '0.1.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Library used to create lego builds',   # Give a short description about your library
    author = 'Petar Kenic',                   # Type in your name
    author_email = 'kenicpetar@yahoo.com',      # Type in your E-Mail
    url = 'https://github.com/peken97/StarkLego',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/peken97/StarkLego/archive/0.2.1.zip',    # I explain this later on
    keywords = ['LEGO', 'BUILD', 'LDRAW'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'gym',
            'pyldraw',
            'numpy',
      ],
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',      #Specify which pyhton versions that you want to support
    
  ],
)