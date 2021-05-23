Command | use | extras 
--------|-----|-------
who | displays all the variable names you have used |
whos | displays a little more about the variables | type, size, class 
clear x | deletes variable **x** from the workspace |
clear | clears all the variables from the workspace |
clc | clear command window |
save filename | saves the variable in the current workspace |
load filename | loads the variables saved previously to use in the current workspace |
special variables and constants | ans, pi, inf, (i,j) , eps, NaN |
% | one line comment |
%{ %} | multi line comment |
format ---- | short:4, long:16, short e, long e, bank:2, rat:nearest rational |
vectors: one dimensional array | row_vector = [1 2 3], coulmn_vactor = [1; 2; 3] |
matrices | [1 2 3; 4 5 6; 7 8 9] | 
disp | Displays contents of an array or string. |
input(PROMPT_String) | RESULT = input(PROMPT) displays the PROMPT string on the screen, waits for input from the keyboard, evaluates any expressions in the input, and returns the value in RESULT. If you press the return key without entering anything, input returns an empty matrix. |
STR = input(PROMPT,'s') | returns the entered text without evaluating expressions. |
; | suppresses screen printing |
Detailed commands related to matlab command window | [Visit this](https://www.tutorialspoint.com/matlab/matlab_commands.htm)|


### Points 
* Every variable in Matlab enviornment is either an Array or Matrix.
* MATLAB allows writing two kinds of program files −
  * __Scripts__ − script files are program files with .m extension. In these files, you write series of commands, which you want to execute together. Scripts do not accept inputs and do not return any outputs. They operate on data in the workspace.
  * __Functions__ − functions files are also program files with .m extension. Functions can accept inputs and return outputs. Internal variables are local to the function. 
