# dastr

## Motivation

Open-source datasets often aren't organized according to a standard directory structure. This means that, if your analysis code expects a particular format, either you have to create a new version of it that loops through files differently or you have to manually move and rename the files to match your code's expected format. `dastr` automates the latter approach.

## How to use

`dastr` can be installed through pip (`pip install dastr`).

There are 3 steps to convert between directory structures: (1) reading, (2) translating, and (3) writing.

### 1. Reading

There will generally be metadata encoded in a dataset's folder and file names. For example, maybe each participant's data are stored in a separate folder and these are called "p01", "p02", etc. Maybe it's a longitudinal EEG study and within each participant-specific folder are files called "pre.edf" and "post.edf". 

`dastr` uses regular expression captures (with Python's `re` library) to read this data into a table (a `list` of `dict`s) where each row (element) is a file and each column (key) is an attribute of that file (for example, participant ID and session).

To read in the data from the above example, you would do the following:

```python
import dastr
data_path = '/path/to/data/'
files = dastr.read(
	path=data_path,
	params=[
		("p(.+)", "participant ID"),
		("(.+)\.edf", "session")])
```
The function will start from the folder specified by the `path` argument and go down from there. The action to take at each level of the directory structure is specified by each elements of the `params` argument (a list of tuples, the elements of which will be strings). The first element of each tuple will be a regular expression. If there are any captures in the regular expression, they will be recorded as the attributes specified by the remaining elements of the tuple. For example: `("(.+)\.edf", "session")` in the above means that, once the program gets to the file `/path/to/data/p01/pre.edf` it should run something equivalent in this case to:
```python
curr_file["session"] = re.findall("(.+)\.edf", "pre.edf")[0]
```
If the current file/folder doesn't match the regular expression, this file is skipped. If the tuple is empty, the regular expression defaults to the wildcard character (`.`).

`dastr.read()` returns a `list` of `dicts`s with keys `attrs` and `path`. `path` specifies the path to the actual file while `attrs` contains another dictionary that stores the attributes. I.e., in the above example, `files[0]["path"]` would be `"/path/to/data/p01/pre.edf"` while `files[0]["attrs"]` would be `{"participant ID": "01", "session": "pre"}`.

In some cases, this might be all you need. You could use `dastr.flatten()` to get a new `list` of `dict`s with key-value pairs copied from `files[:]["attrs"]`, plus an additional key-value pair specifying the path of the file. This makes perfect input for `DictWriter` from Python's `csv` library. The resulting csv table could be read in by your analysis code, point it to each data file, and take its outputs as new columns. Or maybe you don't want to change your analysis code.

### 2. Translating

Suppose instead of "pre" and "post", you want to call the sessions "01" and "02". The function to use then is `dastr.translate()`:
```python
translation = {
	"session": {
		"pre": "01",
		"post": "02"
	}
}

translated = dastr.translate(
	files=files,
	translation=translation)

original = dastr.translate(
	files=translated,
	translation=translation,
	direction="reverse") # Or equivalently "backward", or actually anything other than "forward"
```

### 3. Writing

Actually moving the files is very similar to `dastr.read()`ing them. The difference is that, instead of reading attributes in using `re` captures, you're writing them out using string formatting. For example
```python
new_path = "/new/data/path/"
destinations = dastr.write(
	files=files,
	path=new_path
	params=[
		"alldata",
		("sub-%s", "participant ID"),
		("sub-%s_ses-%s.edf", "participant ID", "session")])
```
creates the variable `destinations`, a `list` of `str`ings specifying the new locations of the files (though they haven't been deleted from their old locations):
```
/new/data/path/alldata/sub-01/sub-01_ses-01.edf
/new/data/path/alldata/sub-01/sub-01_ses-02.edf
/new/data/path/alldata/sub-02/sub-02_ses-01.edf
/new/data/path/alldata/sub-02/sub-02_ses-02.edf
```
If you did want to delete the old files, you could add the optional argument `key="x"` to use Python's `shutil.move()` (by default, `key` is `"c"` which uses Python's `shutil.copy()`). You can also set `key` to any function that takes `old_path, new_path` as its arguments, or you can set it to `"n"` which doesn't touch the files at all (in which case you'd probably also want to set `disp=True`).

## How to use with JSON

To avoid hard-coding the parameters and translations, you can instead specify them in .json files (thanks to [Gabi Herman](github.com/gabiherman) for the suggestion):

### Reading and writing with JSON

Instead of running
```python
dastr.[read/write](
	...,
	params=params,
	...)
```
you would run
```python
dastr.[read/write](
	...,
	params=dastr.json_to_params("path/to/file.json"),
	...)
```
Where `file.json` is formatted in one of 3 ways:

1. a `list` of `dict`s
```json
[
	{
		"pattern": "p(.+)",
		"attrs": "participant ID"
	},
	{
		"pattern": "(.+)\.edf",
		"attrs": "session"
	}
]
```
2. a `dict` of `list`s
```json
{
	"patterns": [
		"p(.+)",
		"(.+)\.edf"
	],
	"attrs": [
		"participant ID",
		"session"
	]
}
```
3. a `list` of `list`s and `str`ings
```json
[
	"alldata",
	["sub-%s", "participant ID"],
	["sub-%s_ses-%s.edf", "participant ID", "session"]
]
```

### Translating with JSON

Here all you need to do is copy and paste your hard-coded `translation` variable into a `.json` file (replacing single quotes with doubles), and pass the location of this file to `dastr.translate`:
```python
translated = dastr.translate(
	...,
	translation="path/to/translation.json")
```
Running `dastr.json_to_params` wouldn't work here.