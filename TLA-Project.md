Iran University of Science and Technology Theory of language and automata (Spring 2024) Dr. Reza Entezari-Maleki


**Course Project:**

**Finite State Automata and Usages in Picture Recognition**


1. **Overview**

In this project, we try to implement picture recognition tools in a newly discussed way using Finite automata. This project has five phases, which are:

0. DFA Implementation (This phase is the basis for the other phases)
0. Picture to DFA Conversion
0. Picture Recognition
0. Picture Classification
0. DFA to Picture Conversion


1. # **Details and Challenges**
   0. ### **DFA Implementation**

In this phase, we have to implement some tools that we learned in the course slides and the base class for DFA which will be used in other phases.

You have to implement the following parts in this phase:

0. DFA class and all its methods
0. Star function for the FAs
0. Union function for the FAs
0. Concat function for the FAs



pg. 1

0. ### **Picture to DFA Conversion**

1. **Converting pictures into Zeros and Ones**

In this phase, you should get a picture as an input and then convert it to its equivalent DFA. To achieve this, you have to convert the input image to an array of zeros and ones. This part has been implemented for you as a function named convert\_pictures\_to\_gray\_scale\_and\_binary\_array in the utils.py file.


1. ### **showing pixels using bit-addressing**
The next thing you should know in this phase is the bit addressing method, which results in a string that we use as input for our constructed DFA. For this approach, we have to consider that our picture's dimensions are powers of 2. At each step, we divide our picture into 4 equal parts and check which part we have our target pixel in. Then, we should concatenate the part number at the end of the address. We continue doing this until the result is only a pixel.



**Figure 1**

This is an example of this method. Consider our initial string as empty and the parts numbered as shown in Figure 1.




**Figure 2	Figure 3	Figure 4	Figure 5**




In the second figure, our pixel is in part 3 as we show with red line è S = ”3”.

In the third figure, our pixel is in part 2 as we shown è S = ”32”.

In the fourth figure, our pixel is in part 0 as we shown è S = ”320”.

In the fifth figure, our pixel is in part 3 as we shown è S = ”3203”.

Here because our picture isn’t dividable anymore, our process will terminate, and the pixel’s bit

address is equal to 3203.

1. ### **constructing our automata**
Consider the following definitions:

**For a given image I, we denote Iw the zoomed part of I in the square addressed w. The image represented by state number x is denoted by ux.**

Now you can construct the DFA using the pseudocode below.


pg. 2

0. ### **Picture Recognition**

In this phase, you have to implement a functionality to show if a given image is equivalent of the given DFA or not and how much similarity is by percentage.

You can use what you have implemented in the past phases to implement this.

For each black pixel of the given image check that its bit-address is accepted by the automata or not and compute the acceptance ratio for that image.





0. ### **Picture Classification**

This phase is really similar to the previous phase. In this phase at first, you give a set of pictures and a set of DFA’s. Then you have to check which of our DFA groups has the most similarity with each given input picture.



0. ### **DFA to Picture Array Conversion**

In the last phase of the project, you have to implement a function which can convert a given DFA to a picture array related to that.


3. # **Implementation notes**

To implement this project, you have to clone our project template first from this [URL ](https://github.com/TLAproject4022/project-template)which contains parts for visualizations and temporal files. then you have to create a virtual environment. You can do that by the below command.

` 	`Python3 -m venv [**virtual**-env-**name**]	

## To install the dependencies which you will need in this project, you should run the below command.
` 	`pip **install** -r requirements.txt	

To test your codes with given test modules for each phase, just run the test\_module[phase\_number].py.
3. # **Submission and Grading**
To submit your work, simply commit all your changes (adding new files as needed) and push your work to your GitHub repository. also, upload a zipped file of changed files on Quera. Make sure you sign the filename with your student IDs. If you don’t do this, we won’t be able to associate your submission with you!

- **Incremental Progress:** Focus on gradual development to maintain compilability. Debug each added functionality individually.


- **Make a private repository:** Keep your repository private till presentation day.

pg. 3

- **Implementation Language:** All the modules are implemented in python. If you want to use any other languages, you have to implement the functionalities that we have given in that language. So the best choice is Python.

- **Submission Readiness:** Perform a thorough compilation check before submission. Un-compilable code will not be scored.

- **Grading policy:** The policy of grading is as below
  - **Phase 0**: 85 pts
  - **Phase 1**: 70 pts
  - **Phase 2:** 50 pts
  - **Phase 3:** 35 pts
  - **Phase 4:** 60 pts



**References**:

## [Finite State Automata and Image Recognition (Marian Mindek)](https://ceur-ws.org/Vol-98/paper13.pdf)





































pg. 4
