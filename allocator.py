"""
Office Space Allocator.

Usage:
  allocator create_room <room_type> <room_name>...
  allocator add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]
  allocator print_room <room_name>
  allocator print_allocations [-o=filename]
  allocator exit

Options:
  -h --help                         Show this screen.
  -o=filename                       Optional filename.
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
        """
        The DocoptExit is thrown when the args do not match.
        We print a message to the user and the usage block.
        The SystemExit exception prints the usage for --help
        """
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            return

        return f(self, opt)

    fn.__name__ = f.__name__
    fn.__doc__ = f.__doc__
    fn.__dict__.update(f.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = ('* ' * 10) + 'WELCOME TO THE OFFICE SPACE ALLOCATOR!' + (' *' * 10)\
        + '\n' + ('= ' * 7) + 'the easiest way to handle all your room allocation.' + (' =' * 7) \
        + '\n' + (' ' * 23) + 'Type help for a list of commands'
    prompt = '(allocator) '

    @deco
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        try:
            if arg['<room_name>'] and arg['<room_type>']:
                for room_name in arg['<room_name>']:
                    dojo.create_room(arg['<room_type>'], room_name)
                    dojo.allocate_rooms()
        except Exception as e:
            print (e)

    @deco
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]"""
        try:
            if arg['<person_name>']:
                if arg['<person_type>']:
                    dojo.add_person(arg['<person_type>'], arg['<person_name>'], arg['<person_surname>'], arg['<wants_accommodation>'])
                    new_fellow = dojo.all_persons[-1]
                    dojo.allocate_rooms()
        except Exception as e:
            print (e)

    @deco
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        try:
            if arg['<room_name>']:
                dojo.print_room(arg['<room_name>'])
        except Exception as e:
            print (e)

    @deco
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o=filename]"""
        try:
            # if arg['-o=filename']:
            dojo.print_allocations()
        except Exception as e:
            print (e)

    @deco
    def do_exit(self, arg):
        """Usage: exit"""
        print ('Have a nice day!')
        exit()

if __name__ == '__main__':
    try:
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        print ('Have a nice day!')
        exit()
