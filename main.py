print('Hello World')

r'''
========================================================================
    Use `pipenv` on every project
========================================================================

    pipenv --version

    if not recognized, install via:
        
        pip install pipenv

    If new project, then install dependencies or dev-dependencies:

        pipenv install <package_name>
        pipenv install <package_name> --dev

    For existing projects:

        pipenv install

    Activate virtual environment:
    
        pipenv shell

    Run command within virtual environment without activating:

        pipenv run <command>

    Exit pipenv shell and virtual environment:

        exit

    Lock dependencies for production

        pipenv lock

    Removing virtual environment

        pipenv --rm


Learn more: https://github.com/lightzane/learn-python/tree/l-pipenv?tab=readme-ov-file#learn-pipenv
'''
