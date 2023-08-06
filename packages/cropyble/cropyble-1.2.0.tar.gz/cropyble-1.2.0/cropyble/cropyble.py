import os

from PIL import Image
import pytesseract


class Cropyble:
    """Container for OCR and cropping methods."""
    def __init__(self, input_image):
        """Initializes a Cropyble object."""
        self.input_image_path = os.path.join(os.getcwd(), input_image)
        self.box_data = {}
        self.height = 0
        self.width = 0
        self._image_to_data()

    def __repr__(self):
        """Returns a representation of a Cropyble object."""
        return f'<Cropyble image={self.input_image_path}>'

    def __str__(self):
        """Returns a verbose string representation of a Cropyble object."""
        string_representation = f'Cropyble Object for image: {self.input_image_path}\n'
        for key, value in self.box_data.items():
            string_representation += f'Word: {key} - Location: {value}\n'
        return string_representation

    def _image_to_data(self):
        """
        Utilizes pytesseract OCR to generate bounding box data for the image.
        Returns the bounding box data.
        """
        found_image = False
        while not found_image:
            try:
                input_image = Image.open(self.input_image_path)
                found_image = True
            except FileNotFoundError:
                raise FileNotFoundError(f'\nThe file [{self.input_image_path}] was not found.')
        
        image_string = pytesseract.image_to_string(input_image)
        word_box_data = pytesseract.image_to_data(input_image)
        char_box_data = pytesseract.image_to_boxes(input_image)
        self.width, self.height = input_image.size
        self._normalize_word_boxes(word_box_data)
        self._normalize_char_boxes(char_box_data)

    def _normalize_char_boxes(self, char_box_data):
        """
        Takes in bounding box data for characters from pytesseract.
        Stores the character and X,Y coordinates for its bounding box in self.box_data
        """
        char_box_data = char_box_data.split('\n')
        
        lines = [line.split(' ') for line in char_box_data]
        for line in lines:
            self.box_data[line[0]] = [int(line[1]), (self.height - int(line[4])), int(line[3]), (self.height - int(line[2]))]

    def _normalize_word_boxes(self, word_box_data):
        """
        Takes in bounding box data for words from pytesseract.
        Stores the word and X,Y coordinates for its bounding box in self.box_data
        """
        word_box_data = word_box_data.split('\n')
        word_box_data = word_box_data[1:]

        lines = [line.split('\t') for line in word_box_data]
        for line in lines:
            self.box_data[line[11]] = [int(line[6]), int(line[7]), 
                (int(line[6]) + int(line[8])), (int(line[7]) + int(line[9]))]

    def crop(self, text_query, output_path):
        """
        Takes in a text query string.
        Outputs an image of the query from the input image if present.
        """
        original_image = Image.open(self.input_image_path)
        box = self.box_data[text_query]
        
        new_image = original_image.crop((box[0], box[1], box[2], box[3]))

        output_path = os.path.join(os.getcwd(), output_path)
        new_image.save(output_path)

    def get_box(self, word):
        """
        Takes in a string representing a word that was recognized.
        Returns a tuple representing the bounding box for the word in (x1, y1, x2, y2) format.
        Remember, for images the origin (0, 0) is located in the top-left corner of the image.
        """
        return tuple(self.box_data[word])

    def get_words(self):
        """Returns a list of recognized words."""
        return [word for word in self.box_data]
