Objective

Learn how to find Linux command documentation without depending on external search engines.

Topics Covered
--help
Manual pages
whatis
apropos
Searching inside manual pages
Git built-in help
Command Help

Most commands provide quick help using:

command --help

Example:

ls --help
Manual Pages

Linux manual pages can be opened using:

man command

Example:

man ls

Useful controls inside man:

Space    Move forward
b        Move backward
/word    Search for a word
n        Next search result
q        Quit
whatis

whatis displays a short description of a command.

Example:

whatis ls
apropos

apropos searches command descriptions.

Example:

apropos directory

This is useful when I know what I want to do but do not know the command name.

Man Sections

Linux manual pages are organized into sections.

Common sections include:

1   User commands
2   System calls
3   Library functions
5   File formats
8   System administration commands

Example:

man passwd

displays documentation for the passwd command.

While:

man 5 passwd

displays documentation about the /etc/passwd file format.

Git Help

Git also includes built-in documentation.

Quick help:

git status -h

Full help:

git help status

Another example:

git log -h
What I Learned
Linux administrators do not need to memorize every command option.
--help provides quick command information.
man provides detailed documentation.
whatis gives a short command description.
apropos helps discover commands.
Git also provides built-in command documentation.