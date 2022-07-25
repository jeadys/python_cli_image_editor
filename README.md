# Image editing through CLI

## About

This repo has many functionalities that can be used to edit/manipulate your images.
Libraries/modules such as Pillow are being used to get most of the work done. <br />
Image manipulation can be done in singular or bulk!

Also interested in video editing? Check out [python_cli_video_editor](https://github.com/YassinAO/python_cli_video_editor)

## Prerequisite

- Python v.3+
- Pillow

## Install

```
$ git clone https://github.com/YassinAO/python_cli_image_editor
$ cd python_cli_image_editor
$ pip install -r requirements.txt
```

## Usage / Examples

**You can leave the -o OR --output argument out of the command to use the default location. Folder named 'output' within this project.** <br />

**The examples below use a single file.** <br />

**Using the --bulk argument will require a folder directory as input so each image file within the folder will be targeted.**

### Add watermark

```
    $python editor.py watermark --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --position top_right --size large
```

### change extension

```
    $python editor.py convert --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --extension .png
```

### change dimension

```
    $python editor.py dimension --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --rotate 90

    $python editor.py dimension --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --scale 300

    $python editor.py dimension --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --flip vertical
```

### blur image(s)

```
    $python editor.py filter --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --blur 2
```

### change hue

```
    $python editor.py hue --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --contrast 2

    $python editor.py hue --input C:\Users\John\Desktop\Thumbnail.jpg --output C:\Users\John\Desktop --monochrome
```

## Commands

```
The main arguments are used in combination with the subcommand arguments

required main arguments:
    -i, --input            absolute path to file, tip [drag & drop a file in the terminal to get the path]
                           (e.g.) --input C:\Users\John\Desktop\Thumbnail.jpg

optional main arguments:
    -o, --output           absolute path to folder, tip [drag & drop a folder in the terminal to get the path]
                           (e.g.) --output C:\Users\John\Desktop\
                           default = output folder within project

    -h, --help             show this help message and exit
                           (e.g.) --help

    --overwrite            overwrite existing file with new file [no values needed]
                           (e.g.) --overwrite

    --optimize             good quality and smaller file size [no values needed]
                           (e.g.) --optimize

    -b, --bulk             manipulate multiple images at once [no values needed], requires folder directory for the --input argument
                           (e.g.) --bulk
```

```
optional arguments watermark feature:

    watermark              allows use of the watermark feature and the subcommands
                           watermark <subcommands>

    -p --position          position of watermark, options [top_left, top_right, bottom_left, bottom_right]
                           (e.g.) --position top_left
                           default = bottom_right

    -s --size           size of the watermark, options [small, medium, large]
                           (e.g.) --size large
                           default = small
```

```
optional arguments dimension feature:

    dimension              allows use of the dimension feature and the subcommands
                           dimension <subcommands>

    --scale                scaling the image down to a new size.
                           (e.g.) --scale 200
                           default = None

    --rotate               rotate the image in degree.
                           (e.g.) --rotate 90
                           default = None

    --flip                 flip the image(s) vertically or horizontally
                           (e.g.) --flip vertical
                           default = None
```

```
optional arguments hue feature:

    hue                    allows use of the hue feature and the subcommands
                           hue <subcommands>

    --contrast             change contrast of the image(s)
                           (e.g.) --contrast 2
                           default = None

    --monochrome           turn image(s) black and white
                           (e.g.) --monochrome
```

```
optional arguments convert feature:

    hue                    allows use of the hue feature and the subcommands
                           hue <subcommands>

    -e --extension         change file format of image(s)
                           (e.g.) --contrast .png
                           default = None
```

```
optional arguments filter feature:

    filter                 allows use of the filter feature and the subcommands
                           filter <subcommands>

    --blur                 add blur to image(s)
                           (e.g.) --blur 2
                           default = None
```

## Current functionalities

- Add watermark to image(s) [option to choose size & position of watermark]
- Change dimension of image(s), such as scale, rotate & flip
- Change coloring of image(s), such as contrast & monochrome
- Change file format of image(s)
- Add filter to image, such as blur
- Multiprocessing for every feature to speed up process time

## Future functionalities

- A lot...
- Error handling for bulk manipulation (if one fails, keep going and create log for the ones that didn't finish)
- A progress bar
- Better image compression
- More will be added to the list...
