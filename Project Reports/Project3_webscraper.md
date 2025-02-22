
# Web Scraping -- Books to Scrape

### DS-1043 - Project 3

### Shaun W. - 9 Dec. 2024

#

## Purpose of Web Scraping

Web scraping is a process in the field of data that extracts information from websites. Particularly, these scraping programs will grab HTML code from a website, search for specific tags/data, and collect then store the data for other purposes. There are many reasons that people may program a web scraper. From a side project to real research, it is a useful tool that helps automate an otherwise strenuous process. A real world example of web scraping can be found in meteorology. From the abstract in a paper about supporting access and use of weather data, the following is stated,

"Currently, end users can not efficaciously extract the desired weather values. Thus, the data is not fully utilised by end users. This work contributes with an open source Web Scraping Application Programming Interface (WebSAPI) through an interactive dashboard. The objective is to extend functionalities of the SASSCAL Weathernet for: data extraction, statistical data analysis and visualisation."[^1]

While the particular use case in this project does not have any real world benefit, this paper helps show the power of web scraping as a tool to better utilize the data available for optimized usage.

## The Goal

The web scraper built in this project is meant to grab data from the following website and its associated items (books): https://books.toscrape.com/. In this lab assignment, we learned a variety of new functions through new libraries. Particularly, this assignment helped to fully introduce the use of the `requests` and `BeautifulSoup` libraries as it relates to grabbing data from websites. The data we gathered with `BeautifulSoup` involved multiple different types of tags and location methods. In my scraper, I utilized table tags, breadcrumbs, and URL tags. The specific data meant to be grabbed for each book included the following: the title, the category, the UPC, the price and tax data, availability, and number of reviews. A specific table can be found through the aforementioned website on any book.

One can see the importance and benefit from programming a web scraper once navigating a website like this manually. From the number of books alone, there exists 1000 links one would have to manually visit and note the data down from. This method of data collection is simply far too inefficient and requires too much time and effort to be worth the energy. Instead, building this scraper allows the data to be neatly collected for us in an automated fashion. Additionally, the scraper will be far more consistent than a human, assuming its instructions are written well. Simply said, the choice between human and program for this type of task is clear.

## Constructing the Scraper

Approaching this assignment, I was admittedly overwhelmed at first. `BeautifulSoup`? `Requests`? I'd never heard of one of them and I'd barely used the other. So, my first stop was the documentation, especially for `BeautifulSoup`. As I began to build the scraper, I littered print() statements all over my code to see what was going on, and I frequently revisited the library documentation. Slowly, but surely, I became more and more comfortable with the functionality of `BeautifulSoup`.

As far as the task pipeline goes, I started with the collection of links only on the home page. Then, I continued furthering the functionality by visiting the links and adding the ones visited to the `data` variable. To elaborate, two main variables exist throughout the scraping process: `data` and `to_visit`. First, `to_visit` is a list of strings, those being the links that need to be visited. Secondly, `data` is a dictionary which contains keys as visited links and values as further dictionaries. These nested dictionaries will contain the book information we are collecting. These structures were utilized as they are compatible with JSON files and are appropriate for the structure of the data we are collecting. In the main block, a `while` loop exists where the loop of this link and data extraction occurs continuously until `to_visit` is empty. Once this traversal was fully implemented, and the data could be properly collected across the website, I moved on to file management.

After the `while` loops ends, or a `KeyboardInterrupt` error occurs, the main block checks for the state of the program. It can be seen as follows: 


    while len(to_visit) > 0:
        
        try:
            
            # HTML Link And Data Extraction
            

        except KeyboardInterrupt: ## Prematurely end program
            save_state(STATE_FILENAME, to_visit, data) ## Save current data and to_visit to JSON file
            is_finished = False ## Declare progression state
            break
            
    else:
        is_finished = True ## Declare finished state if links are all visited
        
    if is_finished:
        save_state(STATE_FILENAME, to_visit, data) ## Saves data/to_visit to JSON
        write_spreadsheet(OUTPUT_FILENAME, data) ## Compiles data to CSV sheet

Compiling the data to the CSV output was done using the `csv` library and the associated `csv.DictWriter` function. Saving and loading the current state of progression is done through JSON files and the `to_visit` and `data` variables. While the final save_state is not necessary after finishing and it was not apart of the originally assigned code, I considered it useful in case of errors that may disrupt the CSV writing process to ensure that the data is not lost after the time is spent running the program. The CSV file contains a header (top row) with the following fieldnames inputted into `csv.DictWriter`: ['Title', 'Category', 'UPC', 'Product Type', 'Price (excl. tax)', 'Price (incl. tax)', 'Tax', 'Availability', 'Number of reviews']. Only links with these data fields filled out are written to the sheet, which prevents non-book entries from existing.

## The Scraps

As I have written it, this web scraper will produce two files at the end: a JSON file and a CSV file. The JSON file will contain the `to_visit` and `data` variables. Naturally, assuming the program finishes properly, it will contain an empty list (due to the fact that `to_visit` will contain no more links) and the `data` dictionary. For links inside `data` that do not correlate to a book title, the value associated with the string is 'None' or 'null' inside the JSON file. For book URLs, the dictionary associated with the link contains values as described before. 

The real product, though, is the CSV file. This sheet will contain only the books and the associated data collected. Due to the nature of CSV files, it is essentially a large spreadsheet with the data collected as columns and each book as a row. The expected count of rows is 1000 books, but some HTTPS request problems or other errors may impact the final number negatively in some cases.

## Potential Modification

After completing this lab and project, the skills and topics learned from here will allow for further development on the web scraper and future programs. If I were to expand on the current state of the scraper, I would make additions to handle HTTP errors that may affect the final result. Additionally, it could be possible to gather the data in a cleaner way as I do not believe I did so in the most effective manner. Specifically, the methods I used to grab the title and category differed from the table data, causing data to be grabbed from other non-book links. While I was able to solve this by only adding entries with specific counts of data, this is not quite as elegant as I would have hoped.

## Final Thoughts

This project and lab in its entirety was an amazing experience that allowed me to dive into the `requests` and `BeautifulSoup` libraries in depth. These libraries and their applications can prove to be useful and I am certain I will use them again for future programs or projects. Overall, despite the length and difficulty I had completing it, this project was very rewarding and gratifying once it all came together.

[^1]:Thapelo, T S, et al.. “SASSCAL WebSAPI: A Web Scraping Application Programming Interface to Support Access to SASSCAL’s Weather Data”. <i>Data Science Journal</i>, vol. 20, no. 1, 2021, p. 24, doi:10.5334/dsj-2021-024. 