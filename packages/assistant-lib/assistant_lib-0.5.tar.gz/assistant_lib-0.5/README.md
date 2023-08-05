# Assistant library

This Python 3.x library is used to write programs that can interact with the Assistant. 

Assistant : https://gitlab.com/goassistant/assistant

Pypi webpage : https://pypi.org/project/assistant-lib

# Changelog

TODO

# License

The license choosen for this project it the LGPLv3. It was choosen instead of the GPLv3 because : 

> The license allows developers and companies to use and integrate a software component released under the LGPL into their own (even proprietary) software without being required by the terms of a strong copyleft license to release the source code of their own components. However, any developer who modifies an LGPL-covered component is required to make their modified version available under the same LGPL license. 

See [Wikipedia](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) for more informations.

# Installation

pip3 install assistant-lib

# Usage

Here is a simple test :

```
$ python3
Python 3.7.4 (default, Jul 11 2019, 10:43:21) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from assistant_lib import assistant
>>> assistant.get_hostname()
'ambre'
```

# Local tests

If you plan to make some upgrades and test them, here is how to process :

* Edit your changes in the code
* Run the clean and build command: 

```
make
```

* Check the dist/ folder
* Install the builded package from the dist/ folder:

```
pip3 install dist/assistant_lib-<version>.tar.gz
```

# Releasing 

The version number is automatically get from git thanks to the setuptools_scm library. So you have no version to set in the code.

To create a new release, just create a tag and push it to Gitlab. The CI/CD pipeline will build a release and publish it to Pypi. This is just magic ;). You can check the .gitlab-ci/yml file to understand how it works.





