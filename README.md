# python-JIRA-BE
|                                                                     Development                                                                     
| :--------------------------------------------------------------------------------------------------------------------------------------------------:


## How to get started

# Installation of Python 3.10 

- Please download the installer for your OS from the official Python site.
 [official Python website](https://www.python.org/downloads/).

## Installation of Poetry

- Install Poetry by executing the following command in the terminal or command prompt.

```bash
pip install poetry
```

## Setting up the Poetry Environment

- Use Poetry to build the Python environment. Please execute the following commands in order.

```bash
poetry shell
poetry install
```

## Configuration of the Pre-commit Hook

- Set up a pre-commit hook to automatically check the code before committing.

```bash
poetry run poe install_pre_commit
```

- This command will automatically perform the necessary checks at commit time.

## Starting the Development Environment

- Use the following command to launch the development server, etc.

```bash
poetry run poe dev
```

_This project uses [poe the poet](https://poethepoet.natn.io) for running scripts as task runners. It also works with .env files._ 

## Environment variables

_Because we are still using the free version of GitHub, application public environment variable should be set in the repository `Actions` environment variables. Please suffix your environment variables with the following suffix:_ /


- `_DEV`: For environment variables that should only be set for `Development` environment.
- `_GLOBAL`: For environment variables that should be set for all environment.


Example: `DB_HOST_DEV`, `LOG_LEVEL_PRD`, `APP_SERVER_PORT_GLOBAL`.




As for secret variables, the application should be retrieved directly from a secret store manager. In our case, most of our secrets are in Azure Key Vault, so we are using [Azure's SDK](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli).



🎉 Happy coding! 🎉



# Commit message rules

*Written in English 
*Prefix (as a type)
*Describe the contents

Prefix must be one of the following:

| prefix   | Explanation                                                                                                 | 
| -------- | ----------------------------------------------------------------------------------------------------------- | 
| build    | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)         | 
| chore    | Miscellaneous commits                                                                                       | 
| ci       | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) | 
| docs     | Documentation only changes                                                                                  |
| feat     | A new feature                                                                                               | 
| fix      | A bug fix                                                                                                   | 
| perf     | A code change that improves performance                                                                     | 
| refactor | A code change that neither fixes a bug nor adds a feature                                                   | 
| revert   | Change cancellation                                                                                         | 
| style    | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)      | 
| test     | Adding missing tests or correcting existing tests                                                           | 

## Example 

- `test: Add unit test of YYYYMMDD()`
- `fix: Change verifyToken to verifiedToken due to naming rule`

## Reference URL 

- [github commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines)
- [gitlab commit guidelines](https://gitlab.com/gogotanaka/items/b65e1b081fa97e6e5754)


# branch strategy
/ Multiple types of branches (feature, develop, release, hotfix, main) are utilized.
/ The "develop" branch acts as the main axis of development, with new features being developed in "feature" branches and then merged into "develop".
/ When ready for release, a "release" branch is created from "develop", where final testing and bug fixes are performed before being merged into "main" and tagged.
/ In cases where urgent bug fixes are needed, a "hotfix" branch is created from "main", and after the fixes, it is merged back into both "main" and "develop".
