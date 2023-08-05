# robotframework-propertyfile
An utility package for exposing Java-style properties from property-files as variables in Robot Framework

# Usage

You need to download the file `propertyfile.py` from here:

https://gist.githubusercontent.com/AdamHepner/bc3e754fb2e808bce190e6e24dff8225/raw/5ef13029dbf04ae1bd68f9bd84afbd61a9406b0c/PropertyFile.py

and make it available in your Robot Framework library search path

Then you can point your .robot file towards any properties file using:

```robotframework
| Settings | | | |
| Variables | propertyfile | path_to_your_propertyfile.prop | variable_prefix |
```

This will make sure, that all properties from the file `path_to_your_propertyfile.prop` are available in your .robot file, prefixed with `variable_prefix` followed by underscore. So, the following entry in property file:

```
http.proxyHost = 192.168.0.1
```

becomes `${variable_prefix_http_proxyHost}`.

**All available environment variables are expanded!**