# -*- coding: UTF-8 -*-
from presentation.formatter.formatter import Formatter


class Max7219AsciiFormatter(Formatter):
    def format(self, value):
        """
        Unicode values of the characters:
        ¡ a8
        ¿ ad
        á a0
        é 82
        í a1
        ó a2
        ú a3
        Á 41
        É 45
        Í 49
        Ó 4f
        Ú 55
        ü 81
        Ü 9a
        ñ a4
        Ñ a5
        ç 80
        Ç 43
        ' 60 or 27
        :param value: text to format
        :return: the formatted value
        """
        return value \
            .replace("‘", u"\x60") \
            .replace("’", u"\x27") \
            .replace("“", u"\x22") \
            .replace("”", u"\x22") \
            .replace("¿", u"\xad") \
            .replace("¡", u"\xa8") \
            .replace("á", u"\xa0") \
            .replace("é", u"\x82") \
            .replace("í", u"\xa1") \
            .replace("ó", u"\xa2") \
            .replace("ú", u"\xa3") \
            .replace("Á", u"\x41") \
            .replace("É", u"\x45") \
            .replace("Í", u"\x49") \
            .replace("Ó", u"\x4f") \
            .replace("Ú", u"\x55") \
            .replace("ü", u"\x81") \
            .replace("Ü", u"\x9a") \
            .replace("ñ", u"\xa4") \
            .replace("Ñ", u"\xa5") \
            .replace("ç", u"\x80") \
            .replace("Ç", u"\x43") \
            .replace("à", "a") \
            .replace("è", "e") \
            .replace("ì", "i") \
            .replace("ò", "o") \
            .replace("ù", "u") \
            .replace("â", "a") \
            .replace("ê", "e") \
            .replace("î", "i") \
            .replace("ô", "o") \
            .replace("û", "u")
