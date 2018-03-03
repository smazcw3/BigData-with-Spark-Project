# BigData with Spark Lab Project

This Lab project was implemented to understand the programming of the dataflow for Big Data analytics using apache spark. It was part of the coursework for ``Data intensive Computing" coursework in Spring 2017.

----------------------
INSIDE THIS REPOSITORY
----------------------
The Lab5 folder comprises of several subfolders as described as below:

1. code             :: This contains the source code required for this lab.
2. input            :: This contains the input required for running the code.
3. sample.output    :: This contains the sample output gathered by running the code.
4. R.code.for.plots :: This contains the plots for generating the plot describing the scalability for bigrams and trigrams with respect to multiple documents.


------------
REQUIREMENTS
------------
1. Code is run on a newer version of Hadoop VM (provided to us for this coursework) that is used for running Spark.
2. This Code is written in python.


------------
INSTRUCTIONS
------------
The following instructions are described as below:

1. Place the "Lab5" folder in (/home/hadoop/) directory. 

2. Copy all the files residing in the "code" folder to the (/home/hadoop/) directory by running:
   cp ~/Lab5/code/* ~

For n = 2 (bigrams)
-------------------
3. Run the following to execute the code for bigrams:
   ./spark/bin/spark-submit wordCoOccurSpark.py ~/Lab5/input/input.bigrams/

4. The output will be created as "spark_bigram_output" folder in the hadoop directory (/home/hadoop/).

Output Description
------------------
(('tantus', 'audio'), u'<luc. 1.519>.<ambrose.ap_david_altera.47>')

('tantus', 'audio')                       ::  2-word Pair CoOccurrence
<luc. 1.519>                              ::  <docid.ChapterNo.LineNo>  <=> <loc>
<luc. 1.519>.<ambrose.ap_david_altera.47> ::  <loc1>.<loc2>


For n = 3 (trigrams)
--------------------
5. Run the following to execute the code for trigrams:
   ./spark/bin/spark-submit wordCoOccurTgramSpark.py ~/Lab5/input/input.trigrams/

6. The output will be created as "spark_trigram_output" folder in the hadoop directory (/home/hadoop/).

Output Description
------------------
(('primus', 'lumen', 'solus'), u'<verg. aen. 6.255>.<verg. aen. 7.130>')

('primus', 'lumen', 'solus')              ::  3-word Pair CoOccurrence
<verg. aen. 6.255>                        ::  <docid.ChapterNo.LineNo>  <=> <loc> 
<verg. aen. 6.255>.<verg. aen. 7.130>     ::  <loc1>.<loc2>


----------
DISCUSSION
----------
Scalability is described in the plot residing in "R.code.for.plots" folder. The plot suggests that 2-word cooccurrence scales quite well as compare to 3-word cooccurrence for latin texts with respect to processing of number of documents. This is primarily because of memory limitations and choice of implementation design.


