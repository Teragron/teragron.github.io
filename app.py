# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:30:31 2023

@author: ahmet
"""

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time in the required format
date_string = now.strftime("%Y-%m-%d %H:%M:%S %z")
subdate_string = now.strftime("%Y-%m-%d")


# Get the blog post title from the user
title = input("Enter the blog post title: ")

# Format the title and date in the filename
filename = f"teragron.github.io/_posts/{subdate_string}-{title.replace(' ', '-').lower()}.markdown"

content = input("Please enter content: ")
# Define the Markdown content with the updated title and date
markdown_content = f"""---
layout: post
title:  "{title}"
date:   {date_string}+200
categories: jekyll update
---
{content}
"""

# Write the Markdown content to the file with the formatted filename
with open(filename, "w") as f:
    f.write(markdown_content)