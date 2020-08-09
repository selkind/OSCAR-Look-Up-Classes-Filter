# course_parser
## Usage: 
1. Do an advanced search with subjects = ["Computational Science & Engr", "Computer Science", "Industrial & Systems Engr", "Public Policy"] and campus = "Online"
1. use CTRL + A to highlight everyhing on the resulting page.
1. use CTRL + C to copy the highlighted contents to your clipboard
1. Open a text editor and use CTRL + V to paste the contents of the search into the text file
1. Save the text file as "oscar_raw.txt" anywhere (but note the location)
1. Run this notebook

#### With such a basic use of pd.read_html() some filtering is required to get at the table I'm interested in
- the course table is the 6th item of the returned object
- Pandas creates a multi-indexed dataframe for this item with the top-level index being the index of the table name
 - This will be different if searching by a different Subject or list of subjects with a different initial subject
- We then have to filter out the other table headers that have been mushed into this dataframe. 
 - I do this by indexing only the subject values that I want
 - This should be done before trying to convert values to numeric values to avoid pandas errors
- Next, I filter out the sections that I am not eligible for. In my case as an OMSCS student, I filter out the analytics, cybersecurity, etc.. sections
 - I should probably change this to see if the last two chars of the subject are numeric instead of filtering out specific values
- next I convert all the columns with numeric values to be interpreted numerically by pandas to facilitate column sorting
- Finally, I've manually identified the columns that I find useful and index on those. I'm sorting by subject to keep courses in different subjects separate, then by number of students on the waitlist to see which classes I have a chance to get into
