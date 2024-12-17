
# N-Grams and "Fuzzy Matching" Algorithm

### DS-1043 - Project 2

### Shaun W. - 15 Nov. 2024

#

## Introducing the Algorithm and N-Grams

The term n-gram refers to a segment or piece of data, typically a word or sentence. A specific n-gram for a word or sentence usually follows the original sequence of adjacent letters in the text or data. For example, an n-gram of length n = 3 for the word 'stop' could be 'sto' or 'top.' Many common systems frequently utilize n-grams for string approximation, which will be explained later. This approximation is colloquially known as "fuzzy matching" or "fuzzy searching" and is used in many tools, such as some auto-correct systems. Overall, this technique has two main advantages: it is "language-neutral and error-tolerant." [^1]

## Explaining String Approximation

This fuzzy matching algorithm utilizes an "n-gram index" to sort through the possible matches for a term and identifies the best possible match(es). It does this by utilizing a list of strings--perhaps words or sentences--and returning a dictionary for which each word option--dictionary key--is associated with a list of strings, this being the n-grams for the word and the value for the key.

For instance, consider the list of string options: ['cop', 'tap']. Now consider the "query" or term we are searching with: 'top'. First, the n-gram index is built for the options. This index will be shown further in a more elaborate example. Then, the n-grams for 'top' are determined: ['top', 'to', 'op', 't', 'o', 'p']. The n-grams for top ['top', 'to'] are not found, but ['op', 't', 'o', 'p'] are. Then it returns the longest n-gram match along with its suggestion. So, this would return the dictionary: {'cop': 'op', 'tap': 't'}. It is important to note that while 'o' and 'p' also match, they do not exceed the length of the current n-gram associated with the suggestion.

## Implementing the Algorithm

Implementation of the algorithm used a few simple functions: ngrams(), add_to_index(), build_index(), fuzzy_pick(), and comp().

The ngrams() function is self explanatory, as it simply returns the list of n-gram strings for a given input. It takes a string input, usually a word, and will output a list of strings like so: ngrams('car') returns ['car', 'ca', 'ar', 'c', 'a', 'r']. The use of strings and lists is done for simplicity and due to the nature of the problem as it is related to language and words. The concise code involved is shared below.


`def ngrams(word: str) -> list[str]:`  
`return [word[i:i+n] for n in range(len(word), 0, -1) for i in range(0, len(word) - n + 1)]`

The two index functions work together to produce a data structure containing all potential suggestion options and their n-grams. The build_index() function takes an input of a list of strings and utilizes the add_to_index(), which calls ngrams(), to produce a dictionary. The dictionary returned contains all n-grams as its keys with the associated values being a list of the options associated with it. For example, build_index(['car', 'cat]) returns the dictionary {'car': ['car'], 'ca': ['car', 'cat'], 'ar': ['car'], 'c': ['car', 'cat'], 'a': ['car', 'cat'], 'r': ['car'], 'cat': ['cat'], 'at': ['cat'], 't': ['cat']}. A dictionary is utilized here in order to have quicker look-ups as the index functions handles duplicate n-grams. Take note that the set of keys in the dictionary is all n-grams while each n-gram may be associated with multiple words. For instance, 't' is only associated with 'cat' while 'ca' is associated with both 'car' and 'cat' in the options list.

Fuzzy_pick() is the final brains of the entire operation. This function utilizes a string query and an n-gram index as its inputs, which comes from build_index(). Then it will output a dictionary for which the keys are the suggestions and the values are the longest query n-gram found for the suggestion. It will take the n-grams of the query and search for potential matches in the index dictionary. Once finding a match, it will check if the match is already added. If it is not already present, it will add the match to dictionary. Else, it will check if the query n-gram for the suggestion is longer than the current one in place. If it is, it will replace it, otherwise it will pass over it. Again, a dictionary is used because each suggestion (key) in the dictionary should not be repeated. It also needs to be associated with the respective n-gram matches that correspond to the suggestion. This allows simplicity and avoids using overly-nested structures.

The comp() function, while not critical for usage, can be used to bring the entire algorithm together. It utilizes two additional functionalities alongside the functions described above. First, it will compile its own options list from all objects in the current Python session. Secondly, it utilizes a "FUDGE" variable which allows the comp() function to only return suggestions of lengths greater than or equal to the longest match - FUDGE. For instance, if the longest match was length n = 5 and FUDGE was set to 2, then the suggestions would only be return if their n-gram length was greater than or equal to 5 - 2 = 3.

## A Play by Play

For this example, we will focus on the fuzzy_pick() function and the functions it calls rather than comp(). 

First, consider a list of possible words. This will be our options. For instance, options = ['clap', 'lap', 'tea']. Our query will be query = 'apt'. Calling fuzzy_pick() will look like the following: 

`fuzzy_pick(query, build_index(options))`

Notice that fuzzy_pick calls build_index(options). This is because we have not built the index yet and thus do not have an index to input. This index will be returned by build_index(options). When build_index(options) is called, it will initialize an "index" variable as an empty dictionary. Then, for every option in options, it will call add_to_index(option, index). Add_to_index() will add every n-gram of the option to the dictionary as keys using ngrams() along with adding the original option to each n-gram as a value for the dictionary key.

Eventually, this returns the following:  

`index = {'clap': ['clap'], 'cla': ['clap'], 'lap': ['clap', 'lap'], 'cl': ['clap'], 'la': ['clap', 'lap'], 'ap': ['clap', 'lap'], 'c': ['clap'], 'l': ['clap', 'lap'], 'a': ['clap', 'lap', 'tea'], 'p': ['clap', 'lap'], 'tea': ['tea'], 'te': ['tea'], 'ea': ['tea'], 't': ['tea'], 'e': ['tea']})`  

Recall the description prior and notice that each n-gram key in the dictionary is associated with a list of the associated "options."

Now, fuzzy_pick(query, index) is called. This function will find the n-grams for the query first, these being: ['apt', 'ap', 'pt', 'a', 'p', 't']. Then, it will go through all of these query n-grams and cross reference them with the dictionary index. Since 'ap' is the longest matching n-gram for both 'clap' and 'lap', the word suggestions are added as keys to the dictionary with 'ap' as their value. Additionally, 'a' is an n-gram of 'apt' and 'tea', so this is added as well. 

The final result: {'clap': 'ap', 'lap': 'ap', 'tea': 'a'}.

Note that every option here was found in the final fuzzy match, but this will not always be the case. In a larger set of options, an auto-correct or other program would likely suggest the words with the longest matches, 'clap' and 'lap' in this case. Though, these programs are often more sophisticated than using this alone.

## Potential Modification

This program and algorithm is not perfect, but it does its intended purpose. With further work on it, some modifications or tweaks could be added in order to improve both the overall quality and functionality of the program. For instance, fuzzy_pick() could utilize the FUDGE variable as well with some simple modification, in which case it would appear similar to the current comp() function. Additionally, it would be a good idea to easily allow the input of other large sets of options, rather than the Python session objects. In my mind, I could see the utilization of a common words list, such as from "https://www.gutenberg.org/files/3201/files/COMMON.TXT". One particular reason to do this instead of the Python session alternative is because many of the Python objects share n-grams and it results in a confusing list of suggestions. As such, the program does not quite perform in a way that is usable in an legible manner.

## Final Thoughts

This algorithm was not very difficult to implement, though the comp() function was confusing at times. This made it somewhat hard to test the program as is and instead required the individual testing of the fundamental functions: ngrams(), build_index(), add_to_index(), and fuzzy_pick(). Other than that, fuzzy matching can be a useful tool in data processing. Notably, it can have significant usage in systems other than auto-correct. One particularly impactful usage of fuzzy matching is in DNA sequencing. Overall, the experience was enjoyable and unique to "mess around" with.

[^1]:Min-Soo Kim, Kyu-Young Whang, Jae-Gil Lee, and Min-Jae Lee. 2005. Ngram/2L: a space and time efficient two-level n-gram inverted index structure. In Proceedings of the 31st international conference on Very large data
bases (VLDB ’05). VLDB Endowment, 325–336.
