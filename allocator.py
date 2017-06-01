doc = """
Office Space Allocator.

Usage:
  allocator create_room <room_type> <room_name>...
  allocator add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]
  allocator print_room <room_name>
  allocator print_allocations [--o=<filename>]
  allocator print_unallocated [--o=<filename>]
  allocator reallocate_person <person_identifier> <new_room_type> <new_room_name>
  allocator help
  allocator exit

Options:
    --o=filename                      Optional filename to write output to.

Examples:
  allocator create_room office Blue
  allocator add_person Nelly Armweek Fellow Y
  allocator print_room Blue
  allocator print_allocations
  allocator print_allocations --o=myfile
  allocator print_unallocated --o=myfile
  allocator reallocate_person 1 office Red

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
    intro = '\n' + ' ' \
        + '\n' + ' ' \
        + (' ' * 10 + '* ' * 11) + 'WELCOME TO THE OFFICE SPACE ALLOCATOR!' + (' *' * 10)\
        + '\n' + ' ' \
        + '\n' + ' ' \
        + '\n' + ' ' \
        + '\n' + (' ' * 11 + '= ' * 7) + 'the easiest way to handle all your room allocation.' + (' =' * 7) \
        + '\n' + ' ' \
        + '\n' + ' ' \
        + '\n' + ' ' \
        + '\n' + (' ' * 12 + ' ' * 23) + 'Type help for a list of commands' \
        + '\n' + ' ' \
        + '\n' + '- ' * 53
    prompt = '(allocator>>) '

    @deco
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        if arg['<room_name>'] and arg['<room_type>']:
            for room_name in arg['<room_name>']:
                dojo.create_room(arg['<room_type>'], room_name)
                dojo.allocate_rooms()

    @deco
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <person_surname> <person_type> [<wants_accommodation>]"""
        if arg['<wants_accommodation>'] is None:
            arg['<wants_accommodation>'] = "N"
        if arg['<person_name>'] and arg['<person_surname>'] and arg['<person_type>']:
            dojo.add_person(arg['<person_type>'], arg['<person_name>'], arg['<person_surname>'], arg['<wants_accommodation>'])
            dojo.allocate_rooms()

    @deco
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        if arg['<room_name>']:
            dojo.print_room(arg['<room_name>'])

    @deco
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=<filename>]"""
        if arg['--o']:
            dojo.print_allocations(arg['--o'])
        else:
            dojo.print_allocations()

    @deco
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=<filename>]"""
        if arg['--o']:
            dojo.print_unallocated(arg['--o'])
        else:
            dojo.print_unallocated()

    @deco
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_type> <new_room_name>"""
        if arg['<person_identifier>'] and arg['<new_room_type>'] and arg['<new_room_name>']:
            dojo.reallocate_person(arg['<person_identifier>'], arg['<new_room_type>'], arg['<new_room_name>'])

    @deco
    def do_help(self, arg):
        """Usage: help"""
        print (doc)

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
