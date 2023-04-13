# Equity Analysis Suite
## Description:
This repository houses the source code for the equity-analysis suite of applications (EAS). The purpose of the EAS is to
provide speculators with a toolset to help them make inference in relation to picking equities they wish to purchase.
The EAS is _**NOT**_ designed to give purchases recommendations and is merely a means to perform various types of stock 
analysis in a more rapid manner. No data returned should be taken as financial advice, please consult with a certified 
professional if you are seeking assitance with how to manage your capital.

## Directory Breakdown:
```
Equity_Analysis
└───Apps
│   └───SubApp
│   |   │-sub_app_name.py
│   |   │-RUN-sub_app_name.py
│   │-README.md (Explains all current Sub Applications)
│   
└───Databases
│   └───Database
│   |   │-database_name.csv
│   |   │-UPDATE-database_name.py  
│   │-README.md (Explains all current local CSV 'Database' files, MongoDB/Flask Set Up)
│   
└───Util
│   └───SubUtil
│   |   │-sub_util_name.py
│   │-README.md (Explains all current Sub Utilities) 
│
│-.gitignore
│-README.md (Root Level)
│-requirements.txt (Required pip packages)
```

## Useful Links:
- [Download: Git](https://git-scm.com/downloads)
    - [Git Documentation](https://git-scm.com/doc)
    - [Github Git Guides](https://github.com/git-guides)
    - [Full Github Documentation](https://docs.github.com/en)
- [Download: VSCode](https://code.visualstudio.com/Download)
    - [VSCode Tips & Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
    - [Full VSCode Documentation](https://code.visualstudio.com/docs)







## Setting Up Project: 
- Open Terminal Window
- Clone Local Copy of Repository
- Navigate into _'Equity_Analysis'_ directory
- Run the following terminal command:  `pip install -r requirements.txt`

## Creating a New Branch:
- Open Terminal Window
- Navigate into _'Equity_Analysis'_ directory
- [Fetch/Pull](https://github.com/git-guides/git-pull) latest version of _'Equity_Analysis'_ repository
- Spin up a new working branch off of 'developer' by running the following terminal command:  `git checkout -b <prefix>/<Name>-<BranchDescription>`
    - Official Prefixes: _'feature'_, _'bugfix'_, _'emergency'_
    - Punctuation should follow a similar pattern as the generic example above (all lowercase _prefix_, first letter uppercase **N**_ame_ & **B**_ranch_**D**_escription_)
    - i.e.:  `git checkout -b feature/Name-ReturnAndGrowthCalculatorUpgrade developer`
- Perform local changes
- [Stag](https://github.com/git-guides/git-add) & [Commit](https://github.com/git-guides/git-commit) all local changes you wish to save on Github
- [Push](https://github.com/git-guides/git-push) new working branch to Github by running the following terminal command: `git push -u origin <prefix>/<Name>-<BranchDescription>`
    - i.e.:  `git push -u origin feature/Name-ReturnAndGrowthCalculatorUpgrade`

## Submitting a Pull Request:
- Please follow the offical Github: [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) documentation to properly submit a Pull Request
    - **NOTE:** All Pull Requests should be opened against the current _'developer'_ branch (e.g. _'base:developer'_ <- _'compare:branchToBeMerged'_)

## Current Sub Applications:
### _ETF_Builder_
PLACEHOLDER
### _Return_And_Growth_Calculator_
PLACEHOLDER


## Current Utilities:
### _Get_Fundamental_Stock_Data_By_Exchange_
PLACEHOLDER
### _Scrub_Fundamental_Stock_Data_By_Exchange_
PLACEHOLDER

