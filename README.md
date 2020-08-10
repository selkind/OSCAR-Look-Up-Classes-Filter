# Georgia Tech OSCAR Registration helper
### **This is a work in progress** If you'd like to contribute, please fork the repo and open up a PR with your suggested changes. I'll try to review it as quickly as I can.
## A quick description of what the script and notebook do.
### If you are and OMSCS student, I would recommend trying the script first and if it doesn't do what you want, use the Notebook to change how the table is filtered and sorted.
#### The intended input is an html file resulting from an advanced search on the Look Up Classes page.
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

## Script Usage: 
1. Clone the repository
1. Run "python3 -m pip install -r script_requirements.txt" to install dependencies
1. Navingate to "Registration" then click "Look Up Classes".
1. Do an advanced search with subjects = ["Computational Science & Engr", "Computer Science", "Industrial & Systems Engr", "Public Policy"] and campus = "Online"
1. Use CTRL + S to save the webpage as a local .html file
1. Run the main.py script with the absolute /path/to/the/file as a the first argument and the path you want the filtered table to be saved to as the second argument.

## Notebook usage
1. Clone the repository
1. Run "python3 -m pip install -r requirements.txt"
1. Do an advanced search with subjects = ["Computational Science & Engr", "Computer Science", "Industrial & Systems Engr", "Public Policy"] and campus = "Online"
1. Use CTRL + S to save the webpage as a local .html file
1. Run "Jupyter Lab" in a terminal to start the server.
1. Copy and paste the url provided in the output from running "Jupyter Lab" into a web browser
1. Open the notebook and enjoy!

