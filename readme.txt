Allen Jackson 
jaxon@uga.edu

Alexander Ashkeboussi
boussi@uga.edu

Joel Scott
jascott@uga.edu

Assignment 1

Included with this readme are the python programs Hello.py and grep.py. 

To run Hello.py on nike
	-make sure you are in the same directory as the Hello.py file
	-type "python Hello.py"
	
To run grep.py on nike
	-make sure you are in the same directory as the grep.py file
	-type "python grep.py [-flags] searchText [filename]"
	-here [-flags] can be -x, -v, or left blank
		-using -v, the grep program will search and return all lines without the associated searchText string 
			i.e. if searchText = "dog", all files without dog will be returned
		-using -x, the grep program will search and return files including the entire associated searchText string 
			i.e. if searchText =  "the dog is happy", only files with the whole line "the dog is happy" will be returned
		-without using flags, the program will return any file in which the searchText is included
			i.e. if searchText = "a", all files with an "a" in them will be returned
		-filename can be a full filename or a wild card may be used such as *.txt