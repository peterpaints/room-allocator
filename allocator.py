"""
Office Space Allocator.

Usage:
  allocator create_room <room_type> <room_name>...
  allocator add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  allocator create_room office Blue
  allocator add_person Nelly Armweek Fellow Y

"""

import cmd
from docopt import docopt, DocoptExit
from classes.dojo import Dojo

dojo = Dojo()


def deco(f):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return

        return f(self, opt)

    fn.__name__ = f.__name__
    fn.__doc__ = f.__doc__
    fn.__dict__.update(f.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to the Office Space Allocator!' \
        + ' (Type help for a list of commands.)'
    prompt = '(allocator) '

    @deco
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        arguments = arg
        # print (arguments)
        if arguments['<room_name>'] and arguments['<room_type>']:
            for room_name in arguments['<room_name>']:
                dojo.create_room(arguments['<room_type>'], room_name)

    @deco
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]"""
        arguments = arg
        # print (arguments)
        if arguments['<person_name>']:
            if arguments['<person_type>'] and arguments['<person_type>'].lower() == 'staff':
                dojo.add_person(arguments['<person_type>'], arguments['<person_name>'], arguments['<person_surname>'])
                new_staff = dojo.all_persons[-1]
                dojo.allocate_rooms()
            elif arguments['<person_type>'] and arguments['<person_type>'].lower() == 'fellow':
                if arguments['<wants_accommodation>']:
                    dojo.add_person(arguments['<person_type>'], arguments['<person_name>'], arguments['<person_surname>'], arguments['<wants_accommodation>'])
                    new_fellow = dojo.all_persons[-1]
                    dojo.allocate_rooms()
                else:
                    dojo.add_person(arguments['<person_type>'], arguments['<person_name>'], arguments['<person_surname>'])
                    new_fellow = dojo.all_persons[-1]
                    dojo.allocate_rooms()


if __name__ == '__main__':
    MyInteractive().cmdloop()
