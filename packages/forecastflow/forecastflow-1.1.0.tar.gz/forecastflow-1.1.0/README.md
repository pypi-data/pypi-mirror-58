# ForecastFlow_PyPI
This project aims to register the forecast flow python package to PyPI.

[What is PyPI?](https://pypi.org/)

## :triangular_flag_on_post: How to register your python package?

### Requirements
- PyPI user account
    - https://pypi.python.org/
- setup.py
    - setup.py indicates basic information about a package such as package name, version, author and etc.
- MANIFEST.in
    - If your package depends on other python packages like Numpy, you need MANIFEST.in when registration 

### Work flow
```
1. Develop your package
2. Make setup.py
3. Make MANIFEST.in if you need
4. Test on your local environment
5. Register to TestPyPI and check whether or not work properly
6. Register to PyPI
```
### References
- [PyPIデビューしたい人の為のPyPI登録の手順](https://qiita.com/kinpira/items/0a4e7c78fc5dd28bd695)


## :calendar: Deployment Schedule
| Date       | Description         | Is Done            |
| :--------: | :------------------ | :----------------: |
| 2019-09-26 | Start Project       | :heavy_check_mark: |
| 2019-10-31 | Release version 1.0 |                    |


## :hammer: Working Logs (Colaboratory Notebook)
| ID   | Name                                         | Last Update | Description         |
| :--: | :------------------------------------------- | :---------: | :------------------ |
| 1    | [FF_PyPI_#1.ipynb]()                         | 2019-09-26  | Sample              |
