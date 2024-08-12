<h1>Turing Machine Simulator</h1>




This is a Python program that simulates a Turing Machine. The program reads in two files, "tm.txt" and "input.txt"; and exports the result as "output.txt".<br />
The structure of tm.txt will be as follows: <br />
Line 1: the states of the Turing machine (separated by commas, and ‘accept’ and ‘reject’ will always be states)<br />
Line 2: the input alphabet (separated by commas, if there is more than one symbol)<br />
Line 3: the tape alphabet (separated by commas, if there is more than one symbol, and assume that ‘_’ represents a blank space on the tape)<br />
Line 4: the starting state of the Turing machine<br />
Line 5 and onward: the transition rules, where each rule takes the form a,b,c,d,e (where being in state ‘a’ and reading symbol ‘b’ on the tape will write a ‘c’ to that location, move to new state ‘d’, and move the read/write head in direction ‘e’)<br />

After the program constructs a Turing machine, "input.txt" is read in, where each line in the file is a string that will be loaded onto the Turing machine tape.<br />

Each line in input.txt is handled as a different string to be tested, and the outputs (‘accept’ or ‘reject’) are exported into a new file, "output.txt.".<br />
This simulator operates under the assumption that each Turing Machine provided always halt.
