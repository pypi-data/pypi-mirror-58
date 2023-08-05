from jproperties import Properties
from os.path import expandvars
from re import sub

valid_var_name = lambda varStr: sub('\W|^(?=\d)','_', varStr)

def get_variables(property_file, prefix):
    """
    Usage in Robot Framework is as following:
    
    *** Settings ***
    Variables  PropertyFile  path/to/your/file.properties  myprefix

    So if, for example, the property file contains, say, "version = 1.0.0", it will load it up
    and provide the value of:
    ${myprefix_version}=1.0.0

    If any value in property file contains environmental variables (as they probably will), those will be automatically expanded!
    """
    prop_file = Properties()
    with open(property_file, "rb") as f:
        prop_file.load(f, "utf-8")

    return {valid_var_name(prefix+"_"+k):expandvars(prop_file[k].data) for k in prop_file}
