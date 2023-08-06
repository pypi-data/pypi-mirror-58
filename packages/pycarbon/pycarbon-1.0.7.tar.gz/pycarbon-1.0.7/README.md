# PyCarbon

A YAML-based configuration system for Python projects supporting tiered environments and files.

`pip install pycarbon`

PyPi Package

https://pypi.python.org/pypi/pycarbon
 
PyCarbon is easy to use, highly configurable, and capable of real-world deployment scenarios that balance settings across multiple files and deployed environments. 

## Release History

All public releases may be found here: https://pypi.org/manage/project/pycarbon/releases/

* 2018-03-04: v1.0.0: Initial release
* 2018-03-05: v1.0.1: Bugfixes and additional unit tests.
* 2018-03-06: v1.0.2: Added support for OS environment variable overrides.
* 2018-06-20: v1.0.3: Bugfix where values were not loaded correctly when the `configuration.environment` field was set outside of the `get` method.
* 2018-06-21: v1.0.4: Updated readme.md, release history, and release instructions.
* 2018-09-05: v1.0.5: Require PyYAML>=3.12 rather than PyYAML==3.12 to compensate for incompatible dependencies in larger projects.
* 2018-09-05: v1.0.6: Updated setup.py to require PyYAML>=3.12 rather than PyYAML==3.12.
* 2019-12-21: v1.0.7: Specify a loader when loading YAML, per PyYAML docs https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation

## Key Concepts

* Environments: [`production`, `staging`, `development`] - Define environments where various settings differ.
* Files: [`config.yml`, `localhost.yml`, `secrets.yml`] - Define files that allow you to isolate various settings, across environments.
* Supports multiple YAML documents per file, namespaced by an `environment`. Each providing a baseline for the next.
* Supports multiple config files, with the opinion that some settings are not fit for source control and should be isolated.
* All settings are merged at runtime, allowing for easy querying.
* Setting keys may be simple or complex (i.e., `path/to/your/setting`, `path.to.your.setting`, `MY_SETTING`)
* Configurable via constructor injection or environment variables.
* Setting values may have defaults, fallback on environment variable values, or be configured to throw exceptions if not found.
* Simple to use, easy to customize

## Usage

The only required setting is the `CONFIG_DIR` or `directory` value. PyCarbon needs to know where to look for your config files.

Set it using an environment variable, or in the constructor.

```
from pycarbon import Configuration

# load files from specified directory
config = Configuration(directory='/path/to/your/config/files')

# alternatively use environment variables
os.environ['CONFIG_DIR'] = '/path/to/your/config/files' # or export it
config = Configuration()
```

Reading setting values.

```
# load a setting
print(config.get('demo.setting'))

# load a setting, throw an exception if it doesn't exist
print(config.get('demo.setting', exception=True))

# load a setting, with a default
print(config.get('demo.setting', default=42))

# use a complex key path to the setting (delimiters supported: comma, slash, colon)
print(config.get('path.to.your.setting'))
print(config.get('path:to:your:setting'))
print(config.get('path/to/your/setting'))

# allow os overrides via environment variables
# if os.environ['setting'] exists, it will override what is defined in the config. handy for ci/cd or containers.
print(config.get('path.to.your.setting', allow_os_override=True))
```

**Sample Config**

Settings should be nested beneath the environment name. The default environment is `development`.

```
production:
  foo: production-value

staging:
  foo: staging-value

development:
  foo: dev-value
```

The assumption is that your CI/CD tool will be setting the `CONFIG_ENV` to one of the pre-defined environments, such that isolating deployment settings is simple.

## Environments

The following `environments` are supported by default, each inheriting or overriding values from the previous environment.

**Default Environments**

* `production`: Default baseline config. If a value is not set for an environment, these are the last fallback values.
* `staging`: Inherits and overrides `production` values.
* `development`: Inherits and overrides `staging` then `production` values.
* `testing`: Inherits and overrides `development` then `staging` then `production` values.

Environments may be overriden by setting the `CONFIG_ENVS` environment variable, or by constructor injection.

```
# separate each environment name with a space
export CONFIG_ENVS=production staging development
```

```
# python
config = Configuration(environments=['prod`, `stage`, `development`]
```

Feel free to define your own environment hierarchy. The first in the list is the baseline. 

Settings will be looked up from the most specific, to the baseline.

If a setting is not found in one environment, it will fallback to the environment before it, continuing to look for a value.

## Files

PyCarbon loads YAML from these files by default, each inheriting or overriding values from the previous file.

Overrides: `secrets.yml` overrides `localhost.yml` overrides `config.yml`

* `config.yml`: Default config file, commit this to your source control.
* `localhost.yml`: Developer config file, likely contains secrets for local development and is ignored by your VCS.
* `secrets.yml`: Top-most secrets file. This file should never be committed to VCS, and contains secrets needed for deployments (i.e., dev, staging, or production).

Files may be overridden by setting the `CONFIG_FILES` environment variable, or by constructor injection.

```
# separate each filename with a space
export CONFIG_FILES=config.yml localhost.yml secrets.yml
```

```
# python
config = Configuration(files=['config.yml`, `localhost.yml`, `secrets.yml`]
```

Feel free to define your own file hierarchy. The first file in the list is the baseline, the last file is the last one that can override a setting.

## Release Instructions

Releasing to PyPi can be a bit of a hurdle. Here is a summary of the steps required.

* Register for an account on https://pypi.org/
* Configure your `~/.pypirc` file with your `username` and `password`
* Make any code changes you'd like, then increment the version number found within `setup.py`

Releasing to PyPi can be done using a variety of ways. `twine` https://pypi.org/project/twine/ is the preferred method, as it uses `https` rather than `http` for the uploading.

*Using twine*

Detailed instructions may be found here: https://pypi.org/project/twine/

```
# create the source distribution
python3 setup.py sdist

# install twine (if it isn't already)
python3 -m pip install twine

# upload the dist folder
twine upload dist/*
```

*Using setuptools*

This is unsafe as it uploads over HTTP, sending your username and password in clear text. I do not recommend this approach, as it leaves your credentials open to sniffing.
```
# create the source distribution locally and upload
python3 setup.py sdist upload
```

## Naming

Why is it called `PyCarbon`? That's a horrible name...

* Naming things is the hardest task in programming. (opinion)
* There are a lot of modules already listed in PyPi, so I needed something.
* Carbon is the building block of life as we know. A good configuration system is the bulding block of any application.
* ...
* That's all I've got. Open to suggestions!

## Credits

This code based upon concepts and original source material from members of Karmic Labs, Inc. engineering group.

Kudos and many thanks for allowing me to publish this derived work!
