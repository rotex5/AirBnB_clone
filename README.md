# AirBnB Clone

## 1. Description of the command line interpreter

The console is where the objects are created and file serialization and deserialization begins. Also, the console contains our first storage engine before a database is implemented. It uses the cmd python library and works in both interactive and non interactive mode. 

### 1.1 Files
* **console**: This module activates the HBnB console and contains all console functions
*  **init file** __init__py
### models
* **base_model**:  contains the model for our base class
#### models/engine
* **file_storage**: this module contains the sotarage engine that serializes and deserializes files in python
### tests
* in this folder are contained the tests for all project modules. The standard used for is the one that add the word test before the name of the file to indicate which module it is testing, preserving the hierarchy that the source files have. ex: models/base_model has its test in tests/test_models/test_base_model

### 1.2 How to start:
The executable console activates the HBnB console. In Linux execute like so:

    ```
    $ ./console.py
    (hbnb)
    ```

### 1.3 How to use it:
The console contains prebuilt commands that which can be listed using the comand help. Most of the commands expect arguments in order to work properly. To check what arguments are expected and to view a description of each command, type help and the name of the command. ex: help reload. 

To quit the console, type the commands quit or EOF.

### Commands can be used

    create [args] - used to create Objects

    show [args] - to display an object created

    destroy [args] - to destroy objects created previously

    update [args] - to update an object was created previously

    all [args] - to display all objects were created previously by an specific Class

    count [args] - to know the number of instances were created from a Class

### Also you can use it by this way

    (hbnb) BaseModel.all()
	(hbnb) BaseModel.show()
    (hbnb) BaseModel.destroy()
	(hbnb) BaseModel.count()

#### Examples

	```
	(hbnb) create BaseModel
    (hbnb) show BaseModel 1234-5sdf-4589
	(hbnb) destroy BaseModel 4565a-asdas1a2
	(hbnb) all
	(hbnb) all BaseModel
	(hbnb) update BaseModel 789-465421-45115
	(hbnb) quit
	```

# Authors
Jeremy John John <johnjerry012@gmail.com>
Rotex <dantejake48@gmail.com>