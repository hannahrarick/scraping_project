# Scraping Project: Three Sports and Their Allegations

## Purpose of Project
The purpose of this project is to compare three popular, especially female popular, sports for their allegations ranging from sexual misconduct to criminal. These three sports include gymnastics, tennis and soccer. This is to shed light on allegations happening at national and local level that aren't publicized.

### Where Did This Idea Come From?
After the Larry Nassar confessions against gymnasts across the country spilled out, I decided to do more research into how much misconduct could be happening despite being on national level. Analyzing gymnastics, the one with the most reports, there had been one or two cases added in the span of working on the project.

## Steps in the Process
1. First, I had to install selenium and take the xpath in order to attach the page to the url source in the file.
2. Second, I wrote all of the table entries into a list with **for loops** in order to get the specific information nestled inside classes like **row** and **td**.
3. After the **for loops** were able to scrape the first page of the website, I had to repeat the same function for the next 22 pages. Thus, I wrote another **for loop** to click each page and scrape that information.
4. Finally, I wrote my scraped information into a CSV file with **c.writerow()**.

## Problems Throughout the Process
There were definitely some hiccups along the road. I struggled mostly with getting my page to click to the next page since it didn't have its separate URLs. Once I got it to click with choosing the correct **class name**, it was then a struggle to scrape that information. I solved this by looking at previous examples in class and writing a **for loop**.

A problem I didn't expect was the trouble in writing it to a csv file. I couldn't write the information into separate rows. This really was just an indent error on my part. I needed to align **cs.writerow()** to the **for td in td_list**.
