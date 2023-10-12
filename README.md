For the moment,
Use a source-code editor such as vscode

In the terminal, create a venv using the terminal in the source code editor

(py or python3) -m venv env
source env/bin/activate (on mac)
.\env\Scripts\activate (windows)

install numpy and pillow, usually with pip install or (py or python3) pip install

In Main.py, run and open a terminal
input the required parameters

the dimensions are x, then y in pixels, for an image of x times y resolution

the step is the distance between lines in pixels, one for each set of lines

the width is the width of the lines

you can choose to have an angle, this is not fully finished yet, answer yes or no
and if so, specify the angle in degrees

the output in the terminal will print out the given parameters

It should create 3 pngs, reseau1.png, which is the png of the first set of lines
moire.png, the moire pattern resulting by the combination with the second set of lines
zones.png, the moire pattern with the middle of the light areas highlighted as well as the middle
of the dark areas highlighted
