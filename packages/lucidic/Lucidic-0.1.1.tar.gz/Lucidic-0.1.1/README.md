# Lucidic Python3 Dictionary Utility Package [STILL IN DEV 12/27/2019]

## Description

Using Python dictionaries within a project is a very common practice. A majority of the web speaks in JSON, a data structure similar to, and often constructed with dictionaries if written in Python. A common use case that is encountered often is the need to compare an incoming request payload, which is generally received in JSON against a previously received payload to calculate what changes to the data have been made. It was this very use case that inspired the development of this little project. Working with AWS's NoSQL Dynamo DB as of late, has given way to quite a few instances where the important data from an incoming request is transformed in-flight into, and stored as, a Map data structure within Dynamo. When updates to that payload come in, there is generally a need to be able to quickly pull that data back from Dynamo, and compare it to the incoming request in order to calculate the changes in data that have occurred in order to create an update request to Dynamo, based on those changes. The last time this very use case was encountered, the decision to create a library that would easily handle the comparision between a pair of dictionaries that would be both, reusable and effective in auto generating a request to update only the change delta, gave birth to this library, Lucidic (Lucid-Dict). Hopefully others will find Lucidic as useful as intended. In addition to simple key by key, value by value recursive comparisions, other methods such as a recursive keyword search and construction of a dict from an ordered list have also been built into the library with usage of those methods documented below. Enjoy, and please feel free to submit or request any changes/bugs/features etc. As with all things, the world is full of smart people, and there are inevitably better ways to perform the same tasks that have been constructed within this library. If things can be done more efficiently, those suggestions are more then welcome.

<br><br>

## Python Version

This library is compatible with Python 3.6 and higher. It may work with earlier versions of Python3 but was not tested against anything earlier then 3.6. As Python 2.x is soon to be end of life, backward compatibility was not taken into consideration.

<br><br>

## Installation

This library has been published to [PyPi](https://pypi.org/project/lucidic/) and can be installed via normal python package manager conventions such as [pip](https://pip.pypa.io/en/stable/) or [poetry](https://pypi.org/project/poetry/).

<br>

```python
pip3 install lucidic
```

 <br>

 In order to use the library simply import it into your project once installed via pip or poetry.

 ```python
from lucidic import Lucidic
 ```

<br><br>

## Instantiating a Lucidic class object

A lucidic object can be instantiated via an existing Python dictionary, or as a stand alone instance resulting in an empty dictionary. The latter option's use case is for a new dictionary instance created from a list or comma separated string value.

<br>

```python
TestDict = {"Record": {"Name": "Test Dictionary", "Type": "SomeRecordTypeName"}}
TestDict = Lucidic(TestDic)
NewDict = Lucidic()
```

<br><br>

## Attributes

`.dict` = The dictionary object used to instantiate the class instance.

<br>

```python
print(TestDict.dict)

{'Record': {'Name': 'Test Dictionary', 'Type': 'SomeRecordTypeName'}}
```

<br><br>

## Methods

### `.search(keyword, strict)`

The search method allows the ability to recursively search for a keyword throughout the entire dictionary object. The method takes 2 arguments, one of which is required, the other optional.

<br>

- `keyword` (Required): The string value that will be searched for recursively within the lucidic instance.
- `strict` (Optional): Flag to toggle between default loose search and exact search

<br>

The strict flag toggles the difference between a loose substring search `if keyword.lower() in key/value/item.lower()` vs an exact match search `if keyword == key/value/item`.

The search utility recursively searches through nested dictionary objects as well as lists and nested lists.

<br>

```python
print(TestDict.search("Name"))

[
    {'keypath': ['Record'], 'match': {'Name': 'Test Dictionary'}},
    {'keypath': ['Record'], 'match': {'Type': 'SomeRecordTypeName'}}
]
```

<br>

```python
print(TestDict.search("Name", strict=True))

[
    {'keypath': ['Record'], 'match': {'Name': 'Test Dictionary'}}
]
```

<br>

As you can see, the search results come back as a list of dict objects. Each dict object contains the keypath of the keyword match occurrence as well as the match occurrence itself. So in the example above, during the loose search, 2 results were returned. Both results were found nested in the 'Record' key, and the match shows the key:value pair where the match was found. If your dictionary object contains nested lists as well, then the result will take that into account as in the the example:

<br>

```python
TestDict = {
    "Records": [
        {"Name": "Record1", "Keywords": ["one", "two", "three"]},
        {"Name": "Record2", "Keywords": ["three", "four", "five"]},
        {"Name": "Record3", "Keywords": [
            {"ListItem": "One"},
            {"ListItem": "Two"},
            {"ListItem": "Three"},
            {"ListItem": [["One"], ["One", "Two"], ["One", "Two", "Three"]]}
        ]}
    ]
}
TestDict = Lucidic(TestDict)
print(TestDict.search("Three"))
```

<br>

```python
[
    {'keypath': ['Records[0]'], 'match': {'Keywords[2]': 'three'}},
    {'keypath': ['Records[1]'], 'match': {'Keywords[0]': 'three'}},
    {'keypath': ['Records[2]', 'Keywords[2]'], 'match': {'ListItem': 'Three'}},
    {'keypath': ['Records[2]', 'Keywords[3]', 'ListItem[2]'], 'match': {'ListItem[2][2]': 'Three'}}
]
```

<br>

In this example we have a variety of nested structures within our referenced dict. In the event that the search term is found within a list item, the keypath will contain both the list item parent dict key, as well as a path through the list to the matched keyword occurrence.

Looking at the last result as an example we can see that the path to the matched keyword is as follows:

`TestDict` = Dict Object, with 'Records' key that contains list as a value. <br>
`TestDict.Records[2]` which is the list's index, or 3rd item in the list contains a nested dict object containing 'Name' key and a 'Keywords' key that has another list object as the value. <br>
`TestDict.Records[2].Keywords[3]` is the 4th item within that list, that contains another nested dict object that contains a 'ListItem' key, that holds a list of lists as the value. <br>
`TestDict.Records[2].Keywords[3].ListItem[2]` or the 3rd list within the list of lists that contains string value items. <br>
`TestDict.Records[2].Keywords[3].ListItem[2]` contains our keyword match for the string value within that nested list at `index [2]`. <br>

<br>

The keypath returns were constructed this way so that other methods within the library could be passed this format and easily construct a matching dict schema, which is useful when constructing a comparison update dict, as we will see in our compare methods.
