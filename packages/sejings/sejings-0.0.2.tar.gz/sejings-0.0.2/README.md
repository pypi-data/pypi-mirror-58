# Settings

Sejings is meant to be a quick and simple tool to rapidly integrate 
project settings. This was inspired by a desire to work with a 
solution similar to MatPlotLib's rcParams and to improve on the 
developer experience and developing speed by avoiding None checks.

This is the development experience I'm trying to avoid:
```python
def add(*nums, cache=None, cache_path=None):
    
    if cache is None:
        cache = settings['cache']
    if cache_path is None:
        cache_path = settings['cache.path']
    
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result
```

Obviously dictionaries would be computationally the fastest way to 
accomplish settings. This project is meant to be friendly to developers 
consuming packages and to encourage rapid development over absolute 
runtime speed. We're using Python after all, right?

# Usage

Import settings and create the settings you need:

```python
from sejings import settings

settings.cache = True
settings.cache.path = '/some/dir/path'

```
 
To evaluate settings passed into a function as an argument 
use the @extract_settings decorator. This will evaluate all 
settings in the function definition and in the arguments
being passed into the function:

```python
from settings import extract_settings

@extract_settings
def add(*nums, cache=settings.cache, cache_path=settings.cache.path):
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result
```

A branch is also evaluated when an endpoint is called.

```python
assert settings.cache()
assert settings.cache.path() == '/some/dir/path'

def add(*nums, cache=settings.cache, cache_path=settings.cache.path):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache_path()) #'/some/dir/path'
    
    return result
```

In some cases defining arguments as a Settings object may be
desired. This is accomplished by adding the argument name to the 
@extract_settings arguments.

```python
@extract_settings('cache')
def add(*nums, cache=settings.cache):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache.path()) #'/some/dir/path'
    
    return result
```

## @TODO

* I'm exploring options right now to allow methods to be called directly
    on self._val but am weighing the pros and cons. The SettingsNumber
    class published is something I'm exploring and should not be 
    depended on as it may change. 
* Context manager
* Copy functionality
* Iteration
* __getitem__, __setitem__
* IO to file. Look into integration with configparser.