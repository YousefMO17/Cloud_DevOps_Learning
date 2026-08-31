bjective

Understand Linux standard streams and practice redirecting command input, normal output, and error output.

Standard Streams

Linux processes normally use three standard streams:

0   stdin
1   stdout
2   stderr
Standard Input - stdin

Standard input is the data provided to a program.

By default, this commonly comes from the keyboard.

File descriptor:

0
Standard Output - stdout

Standard output contains the normal result produced by a command.

Example:

ls

The result normally appears in the terminal.

File descriptor:

1
Standard Error - stderr

Errors are sent to a separate stream.

Example:

ls /directory-that-does-not-exist

File descriptor:

2
Output Redirection

Redirect standard output to a file:

command > file.txt

Example:

echo "Linux" > report.txt

> overwrites the existing file contents.

Append Redirection

Append output without removing previous contents:

command >> file.txt

Example:

echo "Git" >> report.txt
Redirect stdout

These commands are equivalent:

ls > files.txt
ls 1> files.txt

Because file descriptor 1 represents stdout.

Redirect stderr

Redirect errors:

ls /fake-directory 2> errors.txt

Only the error output is saved in errors.txt.

Separate stdout and stderr
ls /etc /fake-directory > output.txt 2> errors.txt

Normal output goes to:

output.txt

Errors go to:

errors.txt
Redirect stdout and stderr Together
command > all-output.txt 2>&1

This sends stdout to the file and then sends stderr to the same destination.

Input Redirection

Input can be read from a file using:

wc -l < report.txt

Instead of reading from the keyboard, wc receives its input from report.txt.

Git Connection

Git output can also be redirected.

Save Git status:

git status > git-status.txt

Save commit history:

git log --oneline > git-history.txt
Redirection Summary
>      stdout to file, overwrite
>>     stdout to file, append
2>     stderr to file
<      file to stdin
What I Learned
stdin uses file descriptor 0.
stdout uses file descriptor 1.
stderr uses file descriptor 2.
> overwrites a file.
>> appends to a file.
Normal output and errors can be redirected separately.
Git command output can also be redirected.