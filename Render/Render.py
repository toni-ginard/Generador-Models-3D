from OpenGL.GL import *
import os
from PIL import Image


class Render:

    @staticmethod
    def render_to_jpg():

        os.chdir("/Users/toniginard/Desktop")

        x, y, width, height = glGetDoublev(GL_VIEWPORT)
        width, height = int(width), int(height)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        data = glReadPixels(x, y, width, height, GL_RGB, GL_UNSIGNED_BYTE)
        image = Image.frombytes("RGB", (width, height), data)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image.save("escena.jpg", "JPEG")