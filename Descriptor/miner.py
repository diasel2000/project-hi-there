from PIL import Image
from pytesseract import image_to_string, image_to_boxes


class TextMiner:
    def __init__(self):
        pass

    def check_text(self, text):
         """Check mined text from image"""
        # TODO: implement checker...

    def get_text(self, path_to_image, lang='eng', check_text=False):
        """Mine text from input image

        Parameters
            image : PIL image
                Image from camera or from downloaded from user phone

        Returns
            result : dict
                Results of text mining. If text is found status=True and return mined text.
                Else return status=False and result=None.

        """
        image = Image.open(path_to_image)
        text = image_to_string(image=image, lang=lang)

        if check_text:
            text = self.check_text(text)

        if text == None:
            result = {'status': False, 'info': 'Any text on the image have not been detected.',
                      'result': None}
            return result
        else:
            result = {'status': True, 'info': 'Text have been detected.',
                      'result': text}
            return result


