![](https://github.com/okawo80085/lose/workflows/unit%20tests/badge.svg)
# lose

lose, but in particular `lose.LOSE`, is a helper class for handling data using `hdf5` file format and `PyTables`

```python
>>> from lose import LOSE
>>> LOSE()
<lose hdf5 data handler, fname=None, atom=Float32Atom(shape=(), dflt=0.0)>
generator parameters: iterItems=None, iterOutput=None, batch_size=1, limit=None, loopforever=False, shuffle=False
```

## installation
```python
pip3 install -U lose
```
or
```python
pip install -U lose
```

---

## TOC
1. [Structure](#structure)
	* [vars](#vars)
	* [methods](#methods)
2. [Example usage](#example-usage)
3. [Generator details](#generator-details)
4. [Bugs or problems](#bugs-or-problems)
5. [Unit tests](#unit-tests)
6. [Change log](#change-log)

## structure
#### vars
`LOSE.fname` is the path to the `.h5` file including the name and extension, default is `None`.

`LOSE.atom` recommended to be left at default, is the `dtype` for the data to be stored in, default is `tables.Float32Atom()` which results to arrays with `dtype==np.float32`.

***

**`LOSE.generator()` related vars:**

`LOSE.batch_size`: batch size of data getting pulled from the `.h5` file, default is `1`.

`LOSE.limit`: int limits the amount of data loaded by the generator, default is `None`, if `None` all available data will be loaded.

`LOSE.loopforever`: bool that allows infinite looping over the data, default is `False`.

`LOSE.iterItems`: list of X group names and list of Y group names, default is `None`, required to be user defined for `LOSE.generator()` to work.

`LOSE.iterOutput`: list of X output names and list of Y output names for `LOSE.iterItems`: to be mapped to, default is `None`, required to be user defined for `LOSE.generator()` to work.

`LOSE.shuffle`: bool that enables shuffling of the data, default is `False`, shuffling is affected by `LOSE.limit` and `LOSE.batch_size`.

`LOSE.mask_callback`: `None` by default, if `None` or is not a function the mask functionality is disabled, see [`LOSE.generator()` details](#generator-details) for more details.

---

#### methods
```
Help on LOSE in module lose.dataHandler object:

class LOSE(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self, fname=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  generator(self, mask_callback=None)
 |
 |  getShape(self, arrName)
 |
 |  getShapes(self, *arrNames)
 |
 |  load(self, *args, batch_obj=':')
 |
 |  makeGenerator(self, layerNames, limit=None, batch_size=1, shuffle=False, mask_callback=None, **kwards)
 |
 |  newGroup(self, fmode='a', **kwards)
 |
 |  removeGroup(self, *args)
 |
 |  renameGroup(self, **kwards)
 |
 |  save(self, **kwards)
 |
 |  ----------------------------------------------------------------------
 ```

`LOSE.newGroup(fmode='a', **groupNames)` is used to append/write(depends on the `fmode` keyword argument, default is `'a'`) group(s) to a `.h5` file.


`LOSE.removeGroup(*groupNames)` is used for to remove group(s) from a file, provided the group(s) name.


`LOSE.renameGroup(**groupNames)` is used to rename group(s) within a `.h5` file, see examples below.


`LOSE.save(**groupNamesAndSahpes)` is used to save data(in append mode only) to a group(s) into a `.h5` file, the data needs to have the same shape as `group.shape[1:]` the data was passed to, `LOSE.get_shape(groupName)` can be used to get the `group.shape`.


`LOSE.load(*groupNames)` is used to load data(hole group or a slice, to load a slice change `LOSE.batch_obj` to a string with the desired slice, default is `"[:]"`) from a group, group has to be present in the `.h5` file.


`LOSE.getShape(groupName)` is used to get the shape of a single group, group has to be present in the `.h5` file.


`LOSE.getShapes(*groupNames)` is used to get the shapes of group(s), group(s) have to be present in the `.h5` file.


`LOSE.generator()` check [Generator details](#generator-details) section, `LOSE.iterItems` and `LOSE.iterOutput` have to be defined.


`LOSE.makeGenerator(self, layerNames, limit=None, batch_size=1, shuffle=False, mask_callback=None, **data)` again check [Generator details](#generator-details) for more details.

---

## example usage
here is some usage examples of how to save and use data

##### creating/adding new group(s) to a file
```python
import numpy as np
from lose import LOSE

l = LOSE()
l.fname = 'path/to/your/save/file.h5' # path to the save file

exampleDataX = np.arange(20)
exampleDataY = np.arange(3)

l.newGroup(fmode='w', x=exampleDataX.shape, y=exampleDataY.shape) # creating new groups(ready for data saved to) in a file, if fmode is 'w' all groups in the file will be overwritten
```
##### saving data to a group(s)
```python
import numpy as np
from lose import LOSE

l = LOSE()
l.fname = 'path/to/your/save/file.h5'

exampleDataX = np.arange(20)
exampleDataY = np.arange(3)

l.save(x=[exampleDataX, exampleDataX], y=[exampleDataY, exampleDataY]) # saving data into groups defined in the previous example
l.save(y=[exampleDataY], x=[exampleDataX]) # the same thing
```
##### loading data from a group(s) within a file
for this example, file has data from the previous example
```python
import numpy as np
from lose import LOSE

l = LOSE()
l.fname = 'path/to/your/save/file.h5'

x, y = l.load('x', 'y') # loading data from the .h5 file(has to be a real file) populated by previous examples
y2compare, x2compare = l.load('y', 'x') # the same thing

print (np.all(x == x2compare), np.all(y == y2compare)) # True True

x, y = l.load('x', 'y', batch_obj=np.s_[:2]) # ':2' will also work, only loads first 2 rows from the data arrays
```
##### getting the shape of a group(s)
for this example, file has data from previous examples
```python
import numpy as np
from lose import LOSE

l = LOSE()
l.fname = 'path/to/your/save/file.h5'

print (l.getShape('x')) # (3, 20)
print (l.getShape('y')) # (3, 3)

print (l.getShapes('y', 'x')) # [(3, 3), (3, 20)]
```
##### renaming group(s) in a file
for this example, file has data from previous examples
```python
import numpy as np
from lose import LOSE

l = LOSE('path/to/your/save/file.h5')
x2compare, y2compare = l.load('x', 'y')
print (l) # file structure before renaming any group(s)
l.renameGroup(y='z', x='lol')
lol, z = l.load('lol', 'z')
print (l) # file structure after renaming group(s)
print (np.all(x2compare == lol), np.all(y2compare == z)) # True True
```
##### removing group(s) from a file
for this example, file has data from previous examples
```python
from lose import LOSE

l = LOSE(fname='path/to/your/save/file.h5')

l.removeGroup('lol', 'z') # removing the group(s)

x = l.load('lol') # now this will result in an error because group 'lol' was removed from the file
```
## generator details
`LOSE.generator(mask_callback=None)` is a python generator used to access data from a `hdf5` file in `LOSE.batch_size` pieces without loading the hole file/group into memory, also works with `tf.keras.model.fit_generator()`, __have__ to be used with a `with` context statement(see examples below).


`LOSE.iterItems` and `LOSE.iterOutput` __have__ to be defined by user first.


`mask_callback` accepts a function, that will be used a mask on each batch of data before it's yielded by the generator on every step. example of mask callback:
```python
def mask(data): # data = tuple({'input_1':batch_inputarray_1, ..., 'input_n':batch_inputarray_n}, {'output_1':batch_outputarray_1, ... 'output_n':batch_outputarray_n})
	x, y = data
	# process the data, without changing any of the keys
	return (x, y)
```

---

`LOSE.make_generator(layerNames, limit=None, batch_size=1, shuffle=False, mask_callback=None, **data)` has the same rules as `LOSE.generator()`. however the data needs to be passed to it each time it's initialized, data is only stored temporarily, the parameters are passed to it on initialization, `layerNames` acts like `LOSE.iterOutput` and `LOSE.iterItems`, but every name in it has to match to names of the data passed(see examples below), if file `temp.h5` exists it will be overwritten and then deleted.

---

### example `LOSE.generator(mask_callback=None)` usage
for this example lets say that file has requested data in it and the model input/output layer names are present.
```python
import numpy as np
from lose import LOSE

l = LOSE('path/to/your/file/with/data.h5')

l.iterItems = [['x1', 'x2'], ['y']] # names of X and Y groups, all group names need to have batch dim the same and be present in the .h5 file
l.iterOutput = [['input_1', 'input_2'], ['dense_5']] # names of model's layers the data will be cast on, group.shape[1:] needs to match the layer's input shape
l.loopforever = True
l.batch_size = 20 # some batch size, can be bigger then the dataset, but won't output more data, it will just loop over or stop the iteration if LOSE.loopforever is False

l.limit = 10000 # lets say that the file has more data, but you only want to train on first 10000 samples

l.shuffle = True # enable data shuffling for the generator, costs memory and time

with l.generator() as gen:
	some_model.fit_generator(gen(), steps_per_epoch=50, epochs=1000, shuffle=False) # model.fit_generator() still can't shuffle the data, but LOSE.generator() can
```

### example `LOSE.make_generator(layerNames, limit=None, batch_size=1, shuffle=False, **data)` usage
for this example lets say the model's input/output layer names are present and shapes match with the data.
```python
import numpy as np
import random
from lose import LOSE

def mask(data):
	x, y = data
	for key in x.keys():
		x[key] += random.random()

	return (x, y)

l = LOSE()

num_samples = 1000

x1 = np.zeros((num_samples, 200)) # example data for the model, x1.shape[1:] == model.get_layer('input_1').output_shape[1:]
x2 = np.zeros((num_samples, 150)) # example data for the model, x2.shape[1:] == model.get_layer('input_2').output_shape[1:]
y = np.zeros((num_samples, 800)) # example data for the model, y.shape[1:] == model.get_layer('dense_5').output_shape[1:]

with l.make_generator([['input_1', 'input_2'], ['dense_5']], batch_size=10, mask_callback=mask, shuffle=True, input_2=x2, input_1=x1, dense_5=y) as gen:
	del x1 #remove from memory
	del x2 #remove from memory
	del y #remove from memory

	some_model.fit_generator(gen(), steps_per_epoch=100, epochs=10000, shuffle=False) # again data can't be shuffled by model.fit_generator(), shuffling should be done by the generator
```

# unit tests
to get the current unit test version run
```
python3 -m lose.test --version
```
or
```
python -m lose.test --version
```

to actually test the code run
```python
python3 -m lose.test
```
or
```python
python -m lose.test
```

# bugs or problems
if you find any, raise an issue.

# change log
[change log](changeLog.md)
