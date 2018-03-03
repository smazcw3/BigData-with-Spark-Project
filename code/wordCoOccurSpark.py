from __future__ import print_function
import time
import sys, csv, string
from pyspark import SparkContext, SparkConf
from pprint import pprint
from pyspark.rdd import RDD

csv_dict = dict()
first_word_list = []

def read_csv():
	csv_file_name = "new_lemmatizer.csv"
	first_row = True
	with open(csv_file_name, 'rb') as csv_file_to_read:
		csv_reader = csv.reader(csv_file_to_read, delimiter=' ', quotechar='|')
		for row in csv_reader:
			csv_inner_array = row[0]
			arr = csv_inner_array.split(",")
			first_word = arr[0]
			first_word_list.append(first_word)
			lemmas_list = list(filter(None, arr[1:len(arr)-1]))
			csv_dict[first_word] = lemmas_list


def combinatorics(list1):
    result = []
    for i in range(0, len(list1)):
        for j in range(i+1, len(list1)):
            listb = []
            listb.append(list1[i])
            listb.append(list1[j])
	    result.append(listb)
    return result

def getLemmasList(word1):
    if word1 in csv_dict:
        lemmas_list1 = csv_dict[word1]
        return lemmas_list1
    else:
        return [word1]

def normalize(word):
    result = word.decode('utf-8')
    result = str(result).translate(None, string.punctuation)
    result = result.lower()
    result = result.replace("j","i")
    result = result.replace("v","u")
    return result.decode('utf-8')

def lemma_combinatorics(lemma_list1, lemma_list2):
    result = []
    for i in lemma_list1:
	for j in lemma_list2:
	    result.append((i,j)) #returning tuple
    return result

def test_map(tokenized):
    result_rdd = []
    convert_tokenized = tokenized.encode('ascii','ignore')
    if convert_tokenized.startswith("<luc.") or convert_tokenized.startswith("<verg."):
        token_split = tokenized.split("\t")
        location = token_split[0]
        line = token_split[1]
        combined_list = combinatorics(line.split())

        for j in range(0, len(combined_list)):
            normalized_word1 = normalize(combined_list[j][0])
            normalized_word2 = normalize(combined_list[j][1])
            lemmas_for_word1 = getLemmasList(normalized_word1)
            lemmas_for_word2 = getLemmasList(normalized_word2)
            lemma_combinations_list = lemma_combinatorics(lemmas_for_word1, lemmas_for_word2)        
        
            for every_word_pair in lemma_combinations_list:
                result_rdd.append((every_word_pair, location))     
        return result_rdd

    else:       
        token_split = convert_tokenized.split()
        location = token_split[0] + token_split[1] + token_split[2]
        line = token_split[3:len(token_split)]
        combined_list = combinatorics(line)

        for j in range(0, len(combined_list)):
            normalized_word1 = normalize(combined_list[j][0])
            normalized_word2 = normalize(combined_list[j][1])
            lemmas_for_word1 = getLemmasList(normalized_word1)
            lemmas_for_word2 = getLemmasList(normalized_word2)
            lemma_combinations_list = lemma_combinatorics(lemmas_for_word1, lemmas_for_word2)        
        
            for every_word_pair in lemma_combinations_list:
                result_rdd.append((every_word_pair, location))     
        return result_rdd


if __name__ == "__main__":
    start_time = time.time()
    conf = SparkConf().setAppName("Spark test")
    sc = SparkContext(conf=conf)    
    read_csv()    
    file_to_read = sc.textFile(sys.argv[1]).filter(lambda x: x is not u'')
    mapper_output = file_to_read.map(test_map)    
    flattened_list = mapper_output.flatMap(lambda c: c)
    reducer_output = flattened_list.reduceByKey(lambda v1, v2: v1 + "." +v2)
    #print (reducer_output.collect())
    reducer_output.saveAsTextFile("spark_bigram_output")
    print("Time taken is--- %s seconds ---" % (time.time() - start_time))
    