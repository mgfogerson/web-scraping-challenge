# web-scraping-challenge

For this project, I used the Beautiful Soup and Splinter libraries in Python to scrape NASA's Mars websites for recent headlines and a featured image, which I then stored in a Mongo Database as a dictionary of dictionaries, which was then parsed and displayed using an HTML layout. 

  This project was one of the first times I became really aware of how to navigate HTML's structure, as I tried to create a set of rules that consistently scraped the right information from the source used for the text and images. As well, the button at the top of the site had to responsively create an instance of the browser, which was closing before it scraped until I discovered how to make the program set an interval on opening the page. The final result is an up-to-date website with a feature allowing it to scrape even more recent information, although the Splinter windows create a cluttered interface for everyday use. 



![image](https://user-images.githubusercontent.com/79113826/142300194-b6c509f7-85de-4787-a005-dab5ebee83b9.png)
