# custom-validator-packaging

This repo describes a quick process for packaging up NetBox Custom Validator classes into python wheels, for import via pip,uv etc. 

## HOWTO

* Clone the REPO

```python
git clone https://github.com/cruse1977/custom-validator-packaging
```

 * Create a python venv, activate and install build

 ```python
 python3 -m venv .venv
 source .venv/bin/activate
 pip install build
 ```

 * Insert your custom validator classes into a file into the custom_validation directory (see example)
 * Import your python file in custom_validation/__init__.py
 * Finally build with:

 ```python
  python -m build
 ```

  This will create both a tar.gz and .whl file within dist.  Use one of these files to import via pip or wheelhouse (NetBox Enterprise)

  To activate, in configuration.py

  ```
  from custom_validation import YourClass


CUSTOM_VALIDATORS = {
    'dcim.site': (
        YourClass(),
    )
}
```

 The repo contains a working example. 
 