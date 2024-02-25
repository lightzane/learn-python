print('Hello World')

r'''
========================================================================
    Using a Python Virtual Environment
========================================================================

    virtualenv --version

    if not recognized, install via:
        
        pip install virtualenv

    Then create new virtual environment like so:

        virtualenv venv

    Activate virtual environment:
        - Linux or Mac:
            source venv/bin/activate
        - Windows
            .\venv\Scripts\activate

    Deactivate virtual environment:

        deactivate

    Install and freeze dependencies after development:

        pip freeze --local > requirements.txt

    Share nad re-install dependencies

        pip install -r requirements.txt


Learn more: https://github.com/lightzane/learn-python/tree/l-virtualenv-with-pip?tab=readme-ov-file#virtualenv
'''
