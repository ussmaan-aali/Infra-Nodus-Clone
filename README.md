# Text Analysis using LLMs and Graphs

We are building a text analysis tool where users can perform the following: <br>

1. Upload their files whether Images or PDFs. <br>
2. Visualize the prominent entities in the text using graphs. <br>
3. Interact with the graph for better understanding. <br>
4. Graph shows relationships between different topics highlighted with different colors. <br>

## Project structure

There are two folders in the project. <br>

1. html_files : <br>
   This folder contains all of the HTML files which contain graph visualizations, produced by the code.

2. src : <br>
   All of the code to produce graphs from text is in this folder. <br>
   main.py is the file to run the project.
   This folder also contains a notebook called "Text_network_graph_KNN" which uses BERT and KNN to draw graphs.

3. input : <br>
   This folder contains the input dataset in the form of JSON for POC.
