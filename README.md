# AirBnB_clone

![HBNB](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T114301Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f6cbb41d4fcda0dde3bea6f4ce6c774f3fd21be7c9e6339f9bae343c323455cf)

The AirBnB clone project is a simple copy of the [AirBnB website](https://alx-intranet.hbtn.io/rltoken/m8g02HcD2ovrl_K-zulYBw) tat will be deployed on a server.

It implements only some of the features that cover fundamental concepts of the higher level programming track.

## Components

This project will be built step by step not all at once. It has different components.

### The console

This step consists of:

	- creating a data model
	- manage (create, update, destroy, read) objects via a console / command interpreter
	- store and persists objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. The storage engine gives an abstraction between the objects and how they are stored an persisted. It will allow easy change in storage without need to update the entire codebase.

![Storage Engine](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T114301Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=657dc581d0719cea4a5448201f3779fb620119579dfeda17b0a1621d5d6ae393)

#### The commands

*Command*  |  *Function*                                 |  *Usage* 
-----------|---------------------------------------------|-----------
_create_   | Creates an instance of a class              | create <class name>
_show_     | Prints string representation of an instance of a class | show <class name> <id>
_all_      | Prints string representation of all instances of a class | all (class name is optional)
_update_   | Adds or updates attributes of an instance. | update <class name> <id> <attribute name> <attribute value>
_count_    | Prints the number of intances of a class. | <class name>.count()


## Bugs

No known bugs

## Authors

Eugene Muthui - joemuthui@gmail.com
Silvia Musangi - musangisilvia@gmail.com


_23rd June 2021_
