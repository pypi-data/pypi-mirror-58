# Sejings

Sejings is meant to be a quick and simple tool to rapidly integrate 
project sejings. The problem I've seen many times with libraries is that
it's often hard to have a way for the user to change aspects or functionality 
deep in a library. Libraries can often have arguments for a function 
that are unavailable to a developer because they're hidden behind three function calls.

One attempt that evolves as a codebase grows is to pass along keyword 
arguments, which leads to documentation and maintainability issues. 
This is evident by the popularity of **kwargs in many data science libraries. 
The only solution I've seen that tries to solve this problem is to work 
with dictionaries similar to matplotlib's rcParams. Yet this leads to 
a tedious and time consuming developer experience by forcing 
`if xxx is None` statements at the top of method calls.

To show you my solution let's first start of with a rcParams style 
function example:

```python
def add(*nums, cache=None, cache_path=None):
    
    if cache is None:
        cache = dict_settings['cache']
    if cache_path is None:
        cache_path = dict_settings['cache.path']
    
    result = sum(nums)
    
    if cache:
        save_to_cache(result, cache_path)
    
    return result
```

Obviously this would be computationally the fastest way to 
accomplish sejings but leaves a lot of work to the developer. 
That's why this project is meant to be friendly to developers 
consuming packages and to encourage rapid development.

# Usage

Import sejings and create the sejings you need:

```python
from sejings import sejings

sejings.cache = True
sejings.cache.path = '/some/dir/path'

```
 
To evaluate sejings passed into a function as an argument 
use the @extract_sejings decorator. This will evaluate all 
sejings in the function definition and in the arguments
being passed into the function:

```python
from sejings import extract_sejings

@extract_sejings
def add(*nums, cache=sejings.cache, cache_path=sejings.cache.path):
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result
```

A branch is also evaluated when an endpoint is called.

```python
assert sejings.cache()
assert sejings.cache.path() == '/some/dir/path'

def add(*nums, cache=sejings.cache, cache_path=sejings.cache.path):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache_path()) #'/some/dir/path'
    
    return result
```

In some cases defining arguments as a Sejings object may be
desired. This is accomplished by adding the argument name to the 
@extract_sejings arguments.

```python
@extract_sejings('cache')
def add(*nums, cache=sejings.cache):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache.path()) #'/some/dir/path'
    
    return result
```

# Integrating Into Your Project

I chose sejings as a close to settings word that wouldn't conflict with
a potentially very common word in programming. Therefore you are encouraged
to import Sejings as a name you see fit. To use matplotlibs rcParams again
as an example we could look at an fictional file settings.py:

```python
from pathlib import Path
from sejings import (
    extract_sejings as extract_settings,
    Sejings
)

my_settings = Sejings(name='rcParams')

my_settings.cache = True
my_settings.cache.path = Path(r'/some/dir/path')

@extract_settings
def add(*nums, cache=my_settings.cache, cache_path=my_settings.cache.path):
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result

```

## @TODO

* Context manager
* __getitem__, __setitem__