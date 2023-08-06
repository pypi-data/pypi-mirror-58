[![Downloads](https://pepy.tech/badge/saenews)](https://pepy.tech/project/saenews)

# Quickstart

### Installation


Install via pip

```bash
pip install saenews
```

or install a specific version

```bash
pip install saenews==0.3.9
```

### Downloading utilities

#### Update : No need to download from version 1.1.0 - utilites come with the repository itself

The code will assume the fonts are available in the `./fonts/` directory. You can change it by passing `text_font` argument in everyfunction

Download the utilities like fonts and social media icons from https://github.com/dheerajmpai/saenews/raw/master/utils.zip

```bash

wget https://github.com/dheerajmpai/saenews/raw/master/utils.zip
unzip utils.zip

```
# Issues and feature requests

If you find any bug or if you find any feature missing. Raise an issue ![here](https://github.com/dheerajmpai/saenews/issues)


# Example

Download the image you want to modify 

example code to add a title and tagline to the image (Here Image is saved as `image.jpg`)

```python

from saenews.utils import *
title_tagline_news(title='Title',tag_line='Tag Line',input_file='image.jpg')

```

Original Image 

![alt text](http://sae.news/developer_tools/qq.jpg)

Final Image

![alt text](http://sae.news/developer_tools/qq.png)

### Features

### Updates

### Bugfixes

Do Visit our website <a href="https://sae.news"> SAE NEWS</a>
