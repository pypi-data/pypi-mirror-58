
from distutils.core import setup
setup(
  name = "the_rapid",         # How you named your package folder (MyLib)
  packages = ["the_rapid"],   # Chose the same as "name"
  version = "0.2",      # Start with a small number and increase it with every change you make
  license="MIT",        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Utilizes the Google Directions API to get route information between any two supported locations",   # Give a short description about your library
  author = "Kyle Ronayne",                   # Type in your name
  author_email = "kyleronaynep@gmail.com",      # Type in your E-Mail
  url = "https://github.com/kyleronayne",   # Provide either the link to your github or to your website
  download_url = "https://github.com/kyleronayne/TheRapid/archive/Beta.tar.gz",    # I explain this later on
  keywords = ["Bus", "Route", "Directions", "Google", "API", "Grand Rapids", "GVSU", "Grand Valley State University"],   # Keywords that define your package best
  package_data={"": ["stops.txt"]},
  include_package_data=True,
  install_requires=[            # I get to this in a second
          "requests"
      ],
  classifiers=[
    "Development Status :: 3 - Alpha",      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    "Intended Audience :: Developers",      # Define that your audience are developers
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",   # Again, pick a license
    "Programming Language :: Python :: 3",      #Specify which pyhton versions that you want to support
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
  ],
)