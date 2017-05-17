[![Build Status](https://travis-ci.org/peterpaints/room-allocator.svg?branch=task_0)](https://travis-ci.org/peterpaints/room-allocator)
# Andela BootCamp 18 Week 2 Project
### Office Space Allocator

This is a project to model a room allocation command line program for Andela's
facilities at the Dojo.
When either a new fellow or member of staff joins Andela, they are allocated space at the Dojo.

Both fellows and staff are allocated an office, randomly.
Fellows can opt for accommodation at the Dojo, but members of staff do not have this option.
Each office at the Dojo has a maximum occupancy of 6 people, while each living space has a maximum
occupancy of 4.

##### Commands:

###### The app has a user-friendly usage guideline.

Command | Arguments | Examples
------- | --------- | --------
create_room | <room_type> <room_name>... | create_room office Kinshasa
add_person | <person_name> <person_surname> <person_type> [<wants_accommodation>] | add_person Peter Musonye fellow Y


##### Installation:

> Clone this repo to your local machine using git clone https://github.com/peterpaints/room-allocator/

> Switch to the develop branch using `git checkout develop`

> Create a virtualenv on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

> From the main folder, in terminal, run `python allocator.py`

##### License:

###### The MIT License.

