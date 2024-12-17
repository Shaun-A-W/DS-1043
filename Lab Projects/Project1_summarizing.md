# TF-IDF Summarizing Algorithm

### DS-1043 - Project 1

### Shaun W. - 9 Nov. 2024

#

## Introducing the Purpose

This algorithm was designed to essentially "summarize" large documents or a corpus. Specifically, it will return the most "interesting" sentences in a document according to their TF-IDF values or ranking, which will be elaborated on later. The algorithm is fairly straightforward and simple. It lacks extreme complexity as it sends back original sentences rather than "newly constructed" ideas. However, this simplicity does not completely discredit the algorithm, as it is still fairly effective for many use cases.	

## Explaining TF-IDF

First of all, what do these acronyms even mean? TF and IDF stand for Term Frequency and Inverse Document Frequency respectively. Using both of these individual values together, a weight or value can be given to words and sentences. A concise yet thorough summary of TF-IDF was written by Rajaraman and Ullman. They said the following about it as the, "formal measure of how concentrated into relatively few documents are the occurrences of a given word is called TF.IDF (Term Frequency times Inverse Document Frequency)." [^1]

## Implementing the Algorithm

Approaching the code involved--which was written in Python--can be boiled down into five fundamental functions: clean_text(), calculate_tf(), calculate_idf(), score_sentences(), and threshold_inclusion().

To start and briefly cover, the clean_text(), score_sentences(), and threshold_inclusion() functions are essentially the skin of the algorithm. Their function names are apt enough of a description, but there are some minor details. The clean_text() function removes non-alphanumeric characters from the document sentences, such as periods, commas, etc. Further, the score_sentences() and threshold_inclusion() functions work together in order to rank and then return the most interesting sentences according to a predetermined multiplier of the average weight. 

Before discussing the calculation of TF-IDF, it is contextually important to walk through the structuring and manipulation of the data from input to output. As previously mentioned, this algorithm was written in Python. A basic, fundamental understanding of data types may be assumed, but a brief description will be supplied. The most important things to know are strings, lists, dictionaries, and the use of nested structures. Individual strings in the case of this algorithm can be associated with the individual words of the text. Lists are collections of items. Lists will be used in contexts such as each sentence being broken down into a list of individual strings (words) for ease of access and overall organization. Dictionaries are similar to lists, but each term (a key) is unique in each dictionary and has an associated value. These dictionaries will be used mostly in assignment of TF and IDF values to words. It is important to note that the data being used may be vast, hence the usage of nested lists and dictionaries. These nested structures will allow for ease of comprehension, organization, and data point accessibility.

Having discussed the data being used and the necessary functions, the handling of it can be addressed. This paragraph will only focus on the data and the structures used. A further explanation into the calculations is explored later. Starting from the input, we have a text file or other list of strings handed to the clean_text() function. This function will output a list of lists of strings. In other words, it gives back a collection of separated sentences that also each contain a collection of separated words. As mentioned previously, it also filters out any non-alphanumeric characters. Next, now that the data is cleaned up, calculate_tf() and calculate_idf() are executed. Calculate_tf() will return a list of dictionaries. This list of dictionaries can be considered a collection of the sentence groupings with each grouping broken down into their words (keys) and associated Term Frequency values. Calculate_idf() will return a single dictionary containing every term in the document as a key alongside its Inverse Document Frequency value. With these data structures returned, score_sentences() is finally executed. It will use these structures to go through the sentences and provide weights through a list of numbers. Finally, the algorithm will come together, using these scores to determine which sentences to output from the original document. 

Now, we can get into the muscle of the algorithm. TF is gathered by computing the number of repetitions of a term in a document--in this case, individual sentences--and dividing each terms repetition value by the number of terms--in this case, the length of the sentence. [^1] This process is completed by the calculate_tf() function. Next, we can find the IDF by determining the number of appearances across all sentences in the document. Dividing this by the length of the document--number of sentences in this case--will give us our IDF value. [^1] Again, this process is performed by the calculate_idf() function.

Finally, once the algorithm has determined all TF and IDF values, a weight can be given to each individual sentence. This sentence weight is found by multiplying the TF-IDF values of the terms in the sentence then finding the summation of each term's final TF-IDF value. One must be cautious in thinking about this, though, as any identical term may have different values depending on the length of the sentence it appears in due to the steps in calculating TF-IDF. This entire value and weight process is done by score_sentences() after the execution of both calculate_tf() and calculate_idf()

## A Test Run

Before going through a small test sample by hand, note the following: strings will be represented by quotation marks (''), lists will be notated by brackets ([ ]), and dictionaries will be shown with braces ({ }).

Consider the following "text file" or list which will be given to clean_text(): ["Name?", "My name is Shaun."]. Clean_text() will return the following, removing the non-alphanumeric characters: [ ['name'], ['my', 'name', 'is', 'shaun'] ].

Next, calculate_tf() will take this clean_text() output and do the following:
First, create a dictionary for each sentence of the sentence terms and their repetition value. This will construct the following list of dictionaries: [ {'name':1}, {'my':1, 'name':1, 'is':1, 'shaun':1} ].
Finally, it will go through this same list of dictionaries to adjust the repetition values according to the length of the sentences (number of terms in the dictionary/sentence). This ends up returning: [ {'name':1}, {'my':0.25, 'name':0.25, 'is':0.25, 'shaun':0.25} ] since the first "sentence" contained one word and the second contained four words.

After that, calculate_idf() will take the same clean_text() output and do the following: 
First, count the number of sentences (two in this case). Then, go through the entire document or collection, adding the term if it has not appeared yet. If it has already been added, add one to the numerator. All denominators for each term's value will be the number of sentences (again, two in this case.) This will return the following: 
{'name':1, 'my':0.5, 'is':0.5, 'shaun':0.5}.

Now, we can score the two sentences. Score_sentence() will accomplish by doing the following:

* The first sentence will have a TF-IDF value of: 1 * 1 = 1.
* The second sentence will have a TF-IDF value of: (0.25 * 0.5) + (0.25 * 1) + (0.25 * 0.5) + (0.25 * 0.5) = 0.125 + 0.25 + 0.125 + 0.125 = 0.625. 

With this calculation, the following list of numbers is returned: [1, 0.625]

In a larger sample, this example would continue by creating a threshold with threshold_inclusion() and the final output of the algorithm would only return sentences with values above the threshold. Unfortunately, going through even a slightly larger example by hand, much less an entire document, would take pages. However, this example is solely meant to illustrate the step-by-step process executed by the algorithm in order to understand what is going on under the hood.

## Improving the Algorithm

If more time were to be spent on improving the effectiveness of my algorithm, a couple of ideas can be explored. First, I would further modify the filtering of clean_text(). While it was already modified to filter out non-alphanumeric characters, the filter implemented is extremely basic and could result in minor inaccuracies in the overall output of the algorithm. This can be demonstrated by filtering through words such as "it's" and other contractions. When filtered, the output of clean_text() provides ['its'] instead of the original intent ['it', 'is'] that the word demonstrates. While this may not affect the quality of the algorithm to a high degree, it is something to keep in mind. Additionally, I would further modify the threshold_inclusion() function or create a secondary option which utilizes a numerical count versus a comparison. To elaborate, I would implement an option to return a maximum amount of sentences versus any sentence above the set multiple of the average weight.

## Final Notes

Working through creating a summary algorithm using TF-IDF was a unique experience for me. The concept of TF-IDF was simple enough to understand that it allowed me to focus on the programming and data aspects of it completely. It was enjoyable to work through understanding and fully comprehending the data used both structurally and their purposes. It goes without saying, though, that there was not zero challenge involved in the process, but the challenge involved was "fun" not frustrating. Overall, I am content with how it turned out and the satisfaction of completing a more thorough project is matched with the learning experience itself.

[^1]:Rajaraman, A.; Ullman, J.D. (2011). ”Data Mining” (PDF). Mining of Massive Datasets. pp. 1–17. https://doi.org/10.1017/CBO9781139058452.002. ISBN 978-1-139-05845-2.

