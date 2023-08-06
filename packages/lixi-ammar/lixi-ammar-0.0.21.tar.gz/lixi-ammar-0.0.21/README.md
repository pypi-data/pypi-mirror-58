LIXI
====

``lixi`` is a python package providing functions to manipulate a valid LIXI message.


Installation
============

Requirements
------------

``lixi`` requires the following libraries as dependencies:

* [boto3](https://github.com/boto/boto3)
* [isodate](https://github.com/gweis/isodate/)
* [jsonschema](https://github.com/Julian/jsonschema)
* [lxml](https://lxml.de/)
* [xmljson](https://github.com/sanand0/xmljson)

Install with pip
----------------
Head over to the cmd or bash window on your machine and type the following command. Note, however, that you need to have pip installed.

```python
pip install lixi-ammar
```


Assumptions
-----------

* A valid LIXI schema has already been obtained(available to LIXI members) and can be accessed by the program via an absolute path, cloud link, etc.
* JSON messages are considered to be in the [BadgerFish](http://badgerfish.ning.com/) convention.

Using the LIXI package
----------

Import the library into your Python project, like so:
```python
import lixi
```

and that's it! You're ready to go.

Fetching a LIXI schema
----------------------

All good things in LIXI start with your own copy of a LIXI schema. You can obtain a LIXI schema from the website.  

Alternatively, you can message the LIXI team to obtain LIXI access and secret key to automatically obtain your own copy of schema online. Which you can use to obtain schemas like so.
```python
lixi.set_credentials('######', '######')
```

Having specified the source (folder or credentials), you can fetch the schema for use in tool by:
```python
xml_schema = lixi.get_xml_schema(lixi_transaction_type='CAL')
```
Or:
```python
json_schema = lixi.get_json_schema(lixi_transaction_type='CAL')
```

You can use the same function to **convert** a schema to JSON or XSD.
```python
xml_schema = lixi.get_xml_schema(schema_string=json_schema_string)
```
Or:
```python
json_schema = lixi.get_json_schema(schema_string=xml_schema_string)
```

**Note:** It should be noted that for all functionality in this package you would need to use the Annotated version of the XML schema.

Referencing the LIXI schema
-------------------

To be able to work with the schema, the package requires you to specify the location of the schema,

As a path to the schema in the appropriate function :
```python
lixi.read_message(schema_path='C:/Path/to/Schema-Annotated.xsd')
```

Or, as a path to the folder that contains the schema (this instruction is used before using any functions that use a schema):
```python
lixi.set_schema_folder('C:/Path/to/Schema/Folder')
```

Reading a LIXI message
-------------------

You can read a LIXI message (XML or JSON) from a string:
```python
test_message = lixi.read_message(message=xml)
```

If you have a LIXI message on file you can read like so:
```python
test_message = lixi.read_message(message_path='C:/Path/to/Message.xml')
```
**Note:** It is recommended to use an absolute (complete) path to avoid confusion. A relative path will look for a folder relative to the code that invokes the ``lixi`` library function.  


Converting a message
------------------

After reading a LIXI XML message, you can convert it to an equivalent JSON like so:
```python
test_message.to_json()
```

Or if you started reading a LIXI JSON message, you can convert it to XML:
```python
test_message.to_xml()
```


Getting element paths
-------------

Element Paths are the XML paths of an item in the LIXI schema: So Person Applicant has the following element path in the LIXI Schema:

``Package.Content.Application.PersonApplicant``

An element path can be used to automate modification of an element, to generate a [customised schema](https://standards.lixi.org.au/lixi2/CustomisationByRestriction) and it can be searched on the [LIXI schema documentation](https://smedia.lixi.org.au/standards-docs.html?standard=master&version=current&component=element&item=Package) to get a host of information like definition, correct use, etc among other things. 


After reading a LIXI message, you can get a list of its element paths:
```python
paths = test_message.get_message_paths()
```

You can save these element paths to a file:
```python
test_message.get_message_paths(output_path='C:/Path/to/Element_Paths.txt')
```

You can also get a list of all element paths of the schema:
```python
test_message.get_schema_paths()
```

Or if you don't want to read a message but want to obtain all schema element paths:
```python
lixi.get_schema_paths('CAL','2.6.19')
```

Getting a customized subschema
---------------------

LIXI provides its members a [tool](https://standards.lixi.org.au/lixi2/CustomisationByRestriction) to derive a subschema that only uses sub set of elements available in the full LIXI schema.

The above tool utilises a instructions file which the library can provide.

After reading a message, you can derive a customisation instructions file from a sample correct message by:
```python
instructions_xml = test_message.get_restriction_paths_for_schema()
```

Or, you can output the same to a file by specifying the output path:
```python
test_message.get_restriction_paths_for_schema(output_path="C:/Path/to/Customisation_instructions.xml'")
```

The generated instructions_xml is used to generate a customisation instructions. You can now use it generate your own set of customised subschemas:
```python
lixi.get_custom_schema(instructions=instructions_xml, schema_path='Path/To/Schema_Annotated.xsd', output_name='DEMO_CAL', output_folder='C:/Store/It/Here')
```

Finally, a message can also be used to generate a custom schema. This would use the element paths of the message to derive a restricted version of the schema:
```python
customised_schema = test_message.generate_custom_schema()
```

Validating with Schematron
---------------------

[Schematron](http://schematron.com/) is a rule-based validation tool for making business rules assertions. LIXI messages can easily be validated with schematron provided the proper business rules schema is specified.
```python
valid, message = test_message.validate_schematron(schematron_schema_text=schematron_as_string)
```

Transforming message to a different version
---------------------

You can transform the message to bring it up to date/or down grade with a different version through the package:
```python
test_message.transform_message(to_version='2.6.24')
```

if you don't specify a TO version, the most updated version is automatically chosen:
```python
test_message.transform_message()
```

As expected this transformation is not loss-less, you can a list of items removed per version jump in warnings file:
```python
test_message.get_transform_warnings(to_version='2.6.15', output_path=path)
```

Saving and pretty printing
------------

You can save a message any time by:
```python
test_message.save()
```

And finally, you can pretty print a message at any time with:
```python
test_message.pretty_print()
```

Bug reports
===========

Please report bugs and feature requests at
(lixilab@lixi.org.au).


Contributing
============

You can contribute to the project in multiple ways:

* Suggest new features
* Implement features
* Fix bugs
* Add unit and functional tests
* Everything else you can think of!