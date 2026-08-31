Objective

Practice navigating the Linux file system and understand the difference between absolute and relative paths.

Topics Covered
Linux File System Hierarchy
Root Directory /
Home Directory ~
Current Directory .
Parent Directory ..
Absolute Paths
Relative Paths
Navigating Directories
Important Linux Directories
Directory	Purpose
/	Root of the Linux file system
/home	Home directories for normal users
/root	Home directory for the root user
/etc	System configuration files
/var	Variable data such as logs
/var/log	System and application logs
/tmp	Temporary files
/usr	Programs, libraries, and utilities
/dev	Device files
/proc	Process and kernel information
/boot	Boot-related files
Important Commands
pwd
ls
ls -l
ls -la
cd
cd ..
cd ~
cd -
Absolute Path

An absolute path starts from the root directory /.

Example:

cd /etc

This command works regardless of the current directory.

Relative Path

A relative path starts from the current working directory.

Example:

cd ../logs

The result depends on the current location.

Special Path Symbols
.   Current directory
..  Parent directory
~   User home directory
/   File system root
Git Connection

Git repositories also exist inside the Linux file system.

The root directory of the current Git repository can be displayed using:

git rev-parse --show-toplevel

The hidden .git directory can be displayed using:

ls -la
What I Learned
Linux uses one hierarchical file system starting from /.
Absolute paths start from /.
Relative paths depend on the current working directory.
pwd shows the current location.
cd .. moves to the parent directory.
cd ~ moves to the user's home directory.
cd - returns to the previous directory.
A Git repository contains a hidden .git directory.