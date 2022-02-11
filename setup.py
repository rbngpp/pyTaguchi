from distutils.core import setup
setup(
  name = 'pyTaguchi',         
  packages = ['pyTaguchi'],   
  version = '0.1',      
  license='MIT',       
  description = 'Taguchi Tables made easy',   
  author = 'Giuseppe Rubino',                   
  author_email = 'giusepperubino@hotmail.co.uk',     
  url = 'https://github.com/rbngpp/pyTaguchi', 
  download_url = 'https://github.com/rbngpp/pyTaguchi/archive/refs/tags/v0.1.tar.gz',
  keywords = ['DOE', 'TAGUCHI', 'DESIGN', 'EXPERIMENT', 'R&D'],  
  install_requires=[           
          'numpy',
          'pandas',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha" | "4 - Beta" | "5 - Production/Stable"
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.9.4'
  ],
)