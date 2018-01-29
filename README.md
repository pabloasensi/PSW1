# Problem Solving Workshop Plagiarism Detector

JPlag is a system that finds similarities among multiple sets of source code files.
This way it can detect software plagiarism. JPlag does not merely compare bytes of text,
but is aware of programming language syntax and program structure and hence is robust 
against many kinds of attempts to disguise similarities between plagiarized files. 
JPlag currently supports Java, C#, C, C++, Scheme and natural language text.

With the help of python and its Html Parser, we can display JPlag's html output in 
order to rapidly view from console all of the code similarities of each student's 
code submission and the percentage of plagiarism. 

## Getting Started

To use the software you simply have to extract the contents of the zip package wherever 
you see necessary.

### Prerequisites

Python 2.7

HTMLParser for Python 2.7

Java Runtime Environment

### Use

To use the program, the shell script must be called through unix bash 
simply by typing:

```
bash shell.sh
```

The shell has two options which require their own arguments:

If option -c is selected, JPlag will perform a full comparison on each 
pair of programs found in a folder and return a list of percentages 
of similarity listed from highest to lowest.

The arguments for option -c are:

* Language of the code that's being checked (java17 (default), 
java15, java15dm, java12, java11, python3, c/c++, c#-1.2, char, text, scheme) 

* Destination of the folder containing the results

Code example:

```
bash shell.sh -c java17 ./ex1/
```


If option -s is selected, JPlag will perform a comparison between a specified 
pair of programs and return not only the percentage of similarity, but also 
the chunks of code that are the same in both programs.

The arguments for option -s are:

* Language of the code that's being checked (java17 (default), 
java15, java15dm, java12, java11, python3, c/c++, c#-1.2, char, text, scheme) 

* Destination of the first program

* Destination of the second program

Code Example:

```
bash shell.sh -c java17 ./ex1/student1 ./ex1/student2
```

Once executed the program will ask you if you desire to eliminate certain leftover 
files.

### Files

The program consists of the following files:

* Jplag.jar
* batchparse.py
* codedisplay.py
* parse.py
* shell.sh

The Jplag jar file is the core jplag module with all of its java dependencies stored 
into one package. This allows us to execute it anywhere as long as we have the 
Java Runtime Environment. The .py files are python scripts that are executed once 
JPlag has finished performing the code comparison. It goes through the html files 
left over by JPlag in the "result" folder and looks for the appropriate tags 
containing the information we wish to display on screen. Specifically, batchparse.py 
shows the list of percentages of similarity of every pair of submissions in descending 
order. Naturally, this one is executed by the -c option of the shell script. On the other 
hand, parse.py and codedisplay.py belong to the -s option, parse.py showing the percentage 
of similarity and the line numbers where the code of both submissions are the same and 
also said lines of code. Shell.sh is the unix shell script that the user must call in 
order to use the program. It's the one that calls both the JPlag.jar and the rest of 
the python scripts.



