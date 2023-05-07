[![Showcase]()]([](https://teragron.github.io/))


# Web UI for Blog Posting

You can check out how the Web UI looks like on HuggingFace:

[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/teragron/blogui)


## Showcase

[![Showcase](https://img.youtube.com/vi/6mGIGsPa9Ww/0.jpg)](https://youtu.be/6mGIGsPa9Ww)


## How it works
This code generates a Markdown blog post with tne given title, content, and image input. 
It uses the Gradio library to provide a user interface for entering the required data.
Double click on the app.bat file to run the Web UI after installing the packages inside the requirements.txt file.

## Functions

-The generate_markdown_post() function takes three inputs: title, content, and image. 
It then generates a unique ID and formats the date and time. The function uses this information to generate a filename and write the Markdown content to the file. 
The Markdown content is then committed to Git and pushed to a remote repository.
-The commit_and_push() function adds the generated file to Git, commits the changes with a message containing the unique ID, and pushes the changes to the remote repository.

## Web UI
The user interface is defined using Gradio. It consists of three input fields: one for the title, one for the content, and one for uploading an image. When the user submits the data, the generate_markdown_post() function is called and the output is displayed.

Overall, this code provides an easy way to generate a Markdown blog post with an image and push it to a remote repository using Git.

To run the app locally, I've created a desktop shortcut and connected to a batch file with the following content:

```
@echo off
"C:\Users\ahmet\anaconda3\envs\valley\python.exe" "C:\Users\ahmet\Desktop\teragron.github.io/app.py"
start http://127.0.0.1:7861
pause
```

