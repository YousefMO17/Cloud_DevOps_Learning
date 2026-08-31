Objective

Understand Linux pipelines and combine multiple commands to process data efficiently.

Pipe Concept

The pipe operator is:

|

A pipe sends the standard output of one command to the standard input of another command.

command1
   |
   | stdout
   v
command2

Syntax:

command1 | command2
Pipe vs Redirection

Redirection sends output to a file:

command > file.txt
Command
   |
   v
File

A pipe sends output to another command:

command1 | command2
Command 1
   |
   v
Command 2
Count Errors in a Log

Display error messages:

grep ERROR server.log

Count them:

grep ERROR server.log | wc -l

Process:

server.log
    |
    v
grep ERROR
    |
    v
wc -l
Git with Pipes

Display Git history:

git log --oneline

Display only the first five commits:

git log --oneline | head -n 5

Search commits containing the word Linux:

git log --oneline | grep -i linux
Shell History with Pipes

Display Git commands used in the shell:

history | grep git

Count them:

history | grep git | wc -l

This is a pipeline containing three commands:

history
   |
   v
grep git
   |
   v
wc -l
Combining Pipes and Redirection

A pipeline result can also be saved to a file.

Example:

grep ERROR server.log | wc -l > error-count.txt

Process:

server.log
    |
    v
grep ERROR
    |
    v
wc -l
    |
    v
error-count.txt
Unix Philosophy

Linux tools are commonly designed to perform small specific tasks.

More complex operations can be created by combining commands using pipes.

What I Learned
| connects commands.
stdout from the first command becomes stdin for the next command.
Multiple commands can form a pipeline.
Pipes can process logs and command output.
Pipes work very well with commands such as grep, wc, head, and Git commands.
Pipes and redirection can be combined.