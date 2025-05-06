# Unit Converter in Python
## Badges
[![Cross-Platform Release](https://github.com/palaashatri/unitconverter-py/actions/workflows/cross-platform-release.yml/badge.svg)](https://github.com/palaashatri/unitconverter-py/actions/workflows/cross-platform-release.yml)
[![Code Coverage [PyTest-Cov]](https://github.com/palaashatri/unitconverter-py/actions/workflows/code-coverage-term.yml/badge.svg)](https://github.com/palaashatri/unitconverter-py/actions/workflows/code-coverage-term.yml)
[![Lint [Flake8]](https://github.com/palaashatri/unitconverter-py/actions/workflows/flake8-lint.yml/badge.svg)](https://github.com/palaashatri/unitconverter-py/actions/workflows/flake8-lint.yml)
[![Unit Test [PyTest]](https://github.com/palaashatri/unitconverter-py/actions/workflows/unit-test.yml/badge.svg)](https://github.com/palaashatri/unitconverter-py/actions/workflows/unit-test.yml)

### Screenshots
<img width="643" alt="Screenshot 2024-09-01 at 4 13 34 PM" src="https://github.com/user-attachments/assets/6590c542-c032-4dc2-af08-3356d4efa5e9">


### Folder Structure
| Folder | Description |
| --- | --- |
| / | Root directory contains `app.py` file |
| src | Contains modules for each implementation |
| test | Contains tests implemented using pytest framework |

### How to run
* Install Python 3 : [Download](https://www.python.org/downloads/)
* The Windows Python3 installer already comes with Tkinter setup built in. For other platforms (Linux/macOS) please read the [official installation docs for Tkinter](https://tkdocs.com/tutorial/install.html).
* Clone this repository
* Run  `app.py` in root directory using : `python app.py` (for Windows) | `python3 app.py` (for Linux/macOS)

### How to build platform-specific binary
* Install pyinstaller : `pip install pyinstaller`
* Build with pyinstaller : `pyinstaller --onefile app.py`
> Note : Windows Defender might show the built file as a trojan. This is a false positive. Heuristic based scanning will detect anything not digitally signed and packed, or has keyboard access as a trojan dropper. You can ignore the warning.


### Testing
* Install pip iff you don't already have it installed using the [official documentation](https://pip.pypa.io/en/stable/installing/)
* Install pytest framework : `pip install -U pytest`
* In root directory, run tests using : `pytest`

 ### Resources
 * [Python Tutorial](https://www.tutorialspoint.com/python/index.htm)
 * [TKinter Tutorial](https://www.tutorialspoint.com/python/python_gui_programming.htm)
 * [GitHub Docs](https://docs.github.com/en/actions/guides/building-and-testing-python)
 * [Article - How to Configure Github Actions the Easy Way](https://towardsdatascience.com/setting-up-python-environment-using-github-actions-9a81936be5c9)
 * [Official Tkinter Documentation](https://tkdocs.com/index.html)

#### Extras
##### Setup tkinter on macOS/linux using `brew` package manager
* Install `brew` package manager : ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
* Install latest version of `python3` : ```brew update && brew install python3```
* Install latest version of `python-tk`: ```brew update && brew install python-tk```
