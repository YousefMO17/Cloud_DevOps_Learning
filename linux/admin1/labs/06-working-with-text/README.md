Objective

Practice reading, inspecting, searching, and analyzing text files from the Linux terminal.

Topics Covered
Displaying file contents
Reading large files
Displaying the beginning of files
Displaying the end of files
Counting lines
Searching text
Working with log files
Important Commands
cat
less
head
tail
wc
grep
cat

Display the complete contents of a file:

cat file.txt

cat is useful for small text files.

less

Open a file interactively:

less file.txt

Press:

q

to exit.

less is more suitable than cat for large files.

head

Display the first lines of a file:

head file.txt

Display the first three lines:

head -n 3 file.txt
tail

Display the last lines:

tail file.txt

Display the last three lines:

tail -n 3 file.txt

Follow a file as new lines are added:

tail -f application.log

This is especially useful for monitoring logs.

wc

Count information inside a file:

wc file.txt

Count only lines:

wc -l file.txt
grep

Search for text inside a file:

grep ERROR application.log

Display matching line numbers:

grep -n ERROR application.log

Ignore uppercase and lowercase differences:

grep -i error application.log
Log Analysis Example

Given a log file containing:

INFO Server started
ERROR Database timeout
WARNING CPU usage high
ERROR Authentication failed

Display only errors:

grep ERROR application.log

Count lines:

wc -l application.log
Git Connection

Git command output is also text and can be processed using Linux tools.

Example:

git log --oneline

Show only the first three commits:

git log --oneline | head -n 3
What I Learned
cat displays file contents.
less is useful for large files.
head displays the beginning of a file.
tail displays the end of a file.
tail -f can monitor changing log files.
wc -l counts lines.
grep searches text.
Linux text-processing tools can also process Git output.