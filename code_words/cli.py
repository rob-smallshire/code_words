"""The command-line for code-words"""

import os
import sys

import docopt
import docopt_subcommands as dsc

from code_words import codec

from code_words.version import __version__


DOC_TEMPLATE = """{program}

Usage: {program} [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.
  -v --verbose  Use verbose logging

Available commands:
  {available_commands}

See '{program} help <command>' for help on specific commands.
"""


@dsc.command()
def list_alphabets(precommand_args, args):
    """usage: {program} list-alphabets

    List the available alphabets.
    """
    
    for name in codec.alphabet_names():
        print(name)
        
    return os.EX_OK


@dsc.command()
def encode(precommand_args, args):
    """usage: {program} encode <number> --separator=<separator> [--alphabet=<alphabet>]

    The number as a sequence of words

    Options:
      --separator=<sequence>  The word separator to used [default: k]
      --words                 The word list to use [default: words2048]
    """
    number = int(args["<number>"])
    separator = args["<separator>"]
    alphabet_name = args["<alphabet>"]
    
    representation = codec.encode(number, separator, alphabet_name)
    
    print(representation)
    return os.EX_OK



def main(argv=None):
    try:
        return dsc.main(
            program='code-words',
            argv=argv,
            doc_template=DOC_TEMPLATE,
            exit_at_end=False)
    except docopt.DocoptExit as exc:
        print(exc, file=sys.stderr)
        return os.EX_USAGE
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return os.EX_DATAERR


if __name__ == '__main__':
    sys.exit(main())
