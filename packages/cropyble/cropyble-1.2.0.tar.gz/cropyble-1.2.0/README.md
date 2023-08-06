# Cropyble

**Author**: Skyler Burger
**Version**: 1.2.1

## Overview
Cropyble is a class that allows a user to easily perform crops on an image containing recognizable text. This class utilizes optical character recognition (OCR) with the assitance of Tesseract OCR and Pytesseract. Images containing clear, printed, non-decorative text work best with the OCR capabilities.

This is :sparkles: my first package on PyPI :sparkles: and I welcome feedback. Feel free to submit issues if you spot an area that could use improvement. 

## Architecture
### Packages
- [**pillow**](https://python-pillow.org/): a Python package for manipulating images
- [**pytesseract**](https://github.com/madmaze/pytesseract): Python bindings for Tesseract
- [**tesseract**](https://github.com/tesseract-ocr/tesseract): a command-line program and OCR engine

## Getting Started
### Linux & Mac OS
- This class requires an additional piece of software that is not available through PyPI. Install [tesseract](https://github.com/tesseract-ocr/tesseract) on your machine with `sudo apt-get install tesseract-ocr`
- Install Cropyble with either `pip3 install cropyble` or preferably with a environment manager such as [`pipenv`](https://pipenv.readthedocs.io/en/latest/)
- Place the following import statement at the top of your file: `from cropyble import Cropyble`
- Create Cropyble instances and get to cropping!

### Example:
````python
# example.py

from cropyble import Cropyble

my_img = Cropyble('demo.jpg')
my_img.crop('world', 'output.jpg')
````
In the above example, imagine that `demo.jpg` is an image that contains the words 'hello world' and is located in the same directory as `example.py`. An instance of Cropyble is created with a path to the input image. Cropyble then performs OCR on the image and stores information regarding the characters and words recognized, as well as their bounding boxes, within the instance of the class. By calling the `.crop()` method of the instance with a word contained in the image and a path to an output file, a cropped image of the word is created. The output file is created if it does not exist, or is overwritten if it already exists.

## API
- **Cropyble(*input_path*)**: Takes in a string representing the input image location. Cropyble runs OCR on the image using `pytesseract` and stores the bounding boxes for recognized words and characters for future crops.
- **.crop(*word*, *output_path*)**: Takes in a string representing the word or character you'd like cropped from the image and a second string representing the output image path. Generates a cropped copy of the query text from the original image and saves it at the specified location.
- **.get_box(*word*)**: Takes in a string representing a word that was recognized in the image. Returns a tuple representing the bounding box of the word in the format (x1, y1, x2, y2). The origin (0, 0) for images is located in the top-left corner of the image.
- **.get_words()**: Returns a list of words that were recognized within the input image.

## Change Log
07/22/2019 - 0.1.0
- Corrected bounding box math. Images are being properly cropped.

07/27/2019 - 0.2.0
- Refactored cropping functions into a class to minimize work needed to perform multiple crops on a single image.

07/30/2019 - 0.3.0
- Cropyble can now accept a path for the input image and crop() accepts a path for the output image.

08/02/2019 - 1.1.0
- Cropyble can now crop words and characters recognized within an image using the same crop() method.

10/08/19 - 1.1.4
- Refactored for packaging
- Uploaded to PyPI, bumpy ride

01/06/20 - 1.2.0
- Added `__repr__` and `__str__` magic methods to Cropyble class.
- Added `.get_box()` and `.get_words()` methods to Cropyble class

01/07/20 - 1.2.1
- Re-released to PyPI
