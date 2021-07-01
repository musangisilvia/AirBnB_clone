# AirBnB_clone

![image](https://user-images.githubusercontent.com/27401241/123797101-816aac80-d8ee-11eb-8aac-13362397f7fa.png)


The AirBnB clone project is a simple copy of the [AirBnB website](https://alx-intranet.hbtn.io/rltoken/m8g02HcD2ovrl_K-zulYBw) that will be deployed on a server.

It implements only some of the features that cover fundamental concepts of the higher level programming track.

## Components

This project will be built step by step not all at once. It has different components.

### The console
-  creating a data model
-  manage (create, update, destroy, read) objects via a console / command interpreter
-  store and persists objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. The storage engine gives an abstraction between the objects and how they are stored an persisted. It will allow easy change in storage without need to update the entire codebase.

![image](https://user-images.githubusercontent.com/27401241/123797176-96dfd680-d8ee-11eb-9414-ee496ec466e3.png)

#### Usage

The console can be used both interactively and non-interactively.


#### *Interactive Mode*
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

 
#### *Non-Interactive Mode*
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

#### The commands

*Command*  |  *Function*                                 |  *Usage* 
-----------|---------------------------------------------|-----------
_create_   | Creates an instance of a class              | +create _classname_
_show_     | Prints string representation of an instance of a class | +show _classname_ _id_
_all_      | Prints string representation of all instances of a class | +all (classname is optional)
_update_   | Adds or updates attributes of an instance. | +update _classname_ _id_ _attributename_ _attributevalue_
_count_    | Prints the number of intances of a class. | +_classname_.count()
_help_     | Prints information about the different functionality of the console. | +help _command_. The command can be ommitted, this will output all commands for which a help function exists for.


## Bugs

No known bugs

## Authors

<p>Eugene Muthui - jmuthui70@gmail.com</p>
<p>Silvia Musangi - musangisilvia@gmail.com</p>






_23rd June 2021_
