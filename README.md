# Image editing through CLI

## About
This repo has many functionalities that can be used to edit/manipulate your images.
Libraries/modules such as Pillow are being used to get most of the work done.

Also interested in video editing? Check out [python_cli_video_editor](https://github.com/YassinAO/python_cli_video_editor)

## Prerequisite
* Python v.3+
* Pillow

## Install
```
$ git clone https://github.com/YassinAO/python_cli_image_editor
$ cd python_cli_image_editor
$ pip install -r requirements.txt 
```
## Usage / Examples
You can leave the -o OR --output argument out of the command to use the default location. Folder named 'output' within this project. 
### change extension
```
(WIP)
```
### change dimensions
```
(WIP)
```
### blur images
```
(WIP)
```

```
## Commands
The main arguments are used in combination with the subcommands/arguments

required main arguments:
    -i, --input            absolute path to file, tip [drag & drop a file in the terminal to get the path]
                           (e.g.) --input C:\Users\John\Desktop\Intro.mp4

optional main arguments:
    -o, --output           absolute path to folder, tip [drag & drop a folder in the terminal to get the path]
                           (e.g.) --output C:\Users\John\Desktop\
                           default = output folder within project

    -h, --help             show this help message and exit
                           (e.g.) --help

    --overwrite            overwrite existing file with new file [no values needed]
                           (e.g.) --overwrite

(WIP)

optional arguments gif subcommand:

(WIP)
