Objective

Practice managing Linux files and directories and understand file properties, inode numbers, hard links, and symbolic links.

Topics Covered
Creating files
Creating directories
Copying files
Moving and renaming files
Removing files and directories
File properties
Inode numbers
Hard links
Symbolic links
Important Commands
touch
mkdir
mkdir -p
cp
cp -r
mv
rm
rm -r
ls -l
ls -li
stat
ln
ln -s
Creating Files
touch file.txt

Creates an empty file.

Creating Directories
mkdir directory

Nested directories can be created using:

mkdir -p project/config/nginx
Copying Files
cp source.txt copy.txt

A copied file is a new file and normally has a different inode.

Directories can be copied recursively using:

cp -r source-directory backup-directory
Moving and Renaming

Move a file:

mv file.txt directory/

Rename a file:

mv old-name.txt new-name.txt
Removing Files
rm file.txt

Remove a directory recursively:

rm -r directory

rm should be used carefully because deleted files are not normally moved to a recycle bin.

File Properties

Detailed file information can be displayed using:

ls -l

More detailed metadata can be displayed using:

stat file.txt
Inodes

Linux files are associated with inode numbers.

Display inode numbers:

ls -li

Conceptually:

Filename
   |
   v
Inode
   |
   v
File Data

An inode stores metadata about a file such as:

Permissions
Owner
Group
Size
Timestamps
References to file data
Hard Links

Create a hard link:

ln original.txt hardlink.txt

A hard link references the same inode as the original file.

original.txt ----\
                  >---- inode ---- data
hardlink.txt ----/

Deleting one filename does not delete the data while another hard link still exists.

Symbolic Links

Create a symbolic link:

ln -s original.txt softlink.txt

A symbolic link has its own inode and references another file by path.

softlink.txt
     |
     v
original.txt
     |
     v
inode
     |
     v
data

If the target is removed, the symbolic link can become broken.

Hard Link vs Symbolic Link
Hard Link	Symbolic Link
Same inode	Different inode
References the same file data	References a path
Can survive deletion of another filename	Can break if target is deleted
Created using ln	Created using ln -s
What I Learned
touch creates files.
mkdir creates directories.
cp creates a copy.
mv can move or rename files.
rm removes files.
Linux uses inodes to manage file metadata.
Hard links share the same inode.
Symbolic links reference another path.