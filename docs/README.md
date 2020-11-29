# py-package-test
[![GitHub license](https://img.shields.io/badge/licence-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-package-test/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v1.0-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-Linux,%20Windows%20&%20Mac%20OS-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/py-package-test)

# Description
Package test

## Required
 - python3
 - docker
 - Flask(>=1.1.1) pip3 install Flask
 
## Directories structure
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
   - workflows
     - python-test.yml
 - bin
   - package-test.py
   - test_package-test.py
 - docs
   - LICENSE
   - README.md
 - log
   - trace.log
 - requirements
   - requirements.txt
   
### Execution examples
 - locally project
   - docker build -t package-test .; docker run -d -p 5000:5000 package-test; docker ps
   - docker build -t package-test . && docker run -d -p 5000:5000 package-test && docker ps
 - project on Docker (if exist)
   - docker pull castellanidavide/package-test; docker run -d -p 5000:5000 package-test; docker ps
   - docker pull castellanidavide/package-test && docker run -d -p 5000:5000 package-test && docker ps
Than you can open [http://localhost:5000/](http://localhost:5000/) on a browser
    
# Changelog
 - [Version_1.0_2020-09-14](#Version_10_2020-09-14)

## Version_1.0_2020-09-14
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/package-test/issues)
