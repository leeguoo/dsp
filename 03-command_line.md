# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> * pwd (show current working directory path)
>> * mkdir aaa (create a dirctory named aaa)
>> * rm -rf aaa (delete the directory named aaa)
>> * touch tmp (create a file named tmp using `touch command`)
>> * rm tmp (delete the file named tmp)
>> * move a b (rename the file a as b)
>> * ls -a (list all th files including hidden files)
>> * cp b ../ (copy file b to the upper directory)
>> * ln -s ../tmp (creat a soft link of the file tmp in the upper directory)
>> * which python (show the path of python)

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> * ls (list the diretory contents)
>> * ls -a (including hidden files)
>> * ls -l (list in long format)
>> * ls -lh (use unit suffixes in the descriptions of file sizes)
>> * ls -lah (same as -lh, but including hidden files)
>> * ls -t (sort by time modified)
>> * ls -Glp (enable colorized output and add slashes after directory names)

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> -a	Displays all files.  
>> -b	Displays nonprinting characters in octal.  
>> -c	Displays files by file timestamp.  
>> -C	Displays files in a columnar format (default)  
>> -d	Displays only directories.  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> It is used to build and execute command lines from standard input  
>> Example: find /path -type f -print | xargs rm

 

