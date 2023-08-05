from .VERSION import __version__, VERSION

from .core.api import Dsl, Dataset
from .core.dsl_grammar import G 


try:
    # if run outside iPython, the magic fails so we use this as a test
    # https://stackoverflow.com/questions/32538758/nameerror-name-get-ipython-is-not-defined
    get_ipython()
    ipython_env = True
except:
    ipython_env = False

if ipython_env:
    from .jupyter import magics


#
# determine if we are in Google Colab or Jupyter
try:
    from google.colab import files
    # load table plugin => %load_ext google.colab.data_table
    get_ipython().run_line_magic("load_ext", "google.colab.data_table")
    COLAB_ENV = True
except:
    COLAB_ENV = False



def login(username="", password="", endpoint="https://app.dimensions.ai", instance="live", verbose=True):
    """
    Login into the Dimensions API and obtain a query token. 
    - If credentials are not passed, we attempt to login using the local dsl.ini credentials file. 
    - If COLAB is detected and user/psw is not available, try running the interactive login

    Args: 
    * username
    * password
    * endpoint (defaults to "https://app.dimensions.ai")
    * instance (defaults to "live")
    """
    from .core.auth import do_global_login, get_connection

    try:
        do_global_login(instance, username, password, endpoint)
    except Exception as e:
        print(str(e))
        print("Login failed: please ensure your credentials are correct.")

    CONNECTION = get_connection()

    if CONNECTION['token']:
        if username and password:
            if verbose: print("DimCli %s - Succesfully connected to <%s> (method: manual login)" % (str(VERSION), CONNECTION['url'])) 
        else:
            # try to use local init file using instance parameter
            if verbose: print("DimCli %s - Succesfully connected to <%s> (method: dsl.ini file)" % (str(VERSION), CONNECTION['url']))


def logout():
    """
    Reset the connectiont to the Dimensions API. This allows to create a new connection subsequently, eg to a different endpoint.
    """
    from .core.auth import reset_login, get_connection
    CONNECTION = get_connection()
    if CONNECTION['token']:
        reset_login()
        print("Logging out... done") 
    else:
        print("Please login first") 



def login_status():
    """Simply output info on whether we are logged in or not"""
    from .core.auth import get_connection
    CONNECTION = get_connection()
    if CONNECTION['token']:
        print("DimCli %s - Succesfully connected to <%s>" % (str(VERSION), CONNECTION['url'])) 
        return True
    else:
        print("Status: not logged in") 
        return False