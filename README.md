# teragron.github.io


# Webui for Blog Posting

## Demo

[!](blog)[https://youtu.be/6mGIGsPa9Ww]

## How it works
This code generates a Markdown blog post with a title, content, and image input. 
It uses the Gradio library to provide a user interface for entering the required data.

## Functions

-The generate_markdown_post() function takes three inputs: title, content, and image. 
It then generates a unique ID and formats the date and time. The function uses this information to generate a filename and write the Markdown content to the file. 
The Markdown content is then committed to Git and pushed to a remote repository.
-The commit_and_push() function adds the generated file to Git, commits the changes with a message containing the unique ID, and pushes the changes to the remote repository.

## WEBUI
The user interface is defined using Gradio. It consists of three input fields: one for the title, one for the content, and one for uploading an image. When the user submits the data, the generate_markdown_post() function is called and the output is displayed.

Overall, this code provides an easy way to generate a Markdown blog post with an image and push it to a remote repository using Git.
