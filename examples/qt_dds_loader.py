import os
import py_dds
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication
from PySide6.QtGui import QImage, QPixmap, qRgb, qRgba, QPainter
from PySide6.QtCore import QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # load the DDS image
        filename = os.path.join("..", "example_images", "DXT1 firefox_logo.dds")  # <- try loading other example images!
        filename = os.path.join("..", "example_images", "Uncompressed24 firefox_logo.dds")  # <- try loading other example images!
        self.load_dds(filename)
        # display the loaded image on a QLabel
        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap.fromImage(self.final))
        self.setCentralWidget(self.lbl)

    def load_dds(self, filename):
        """
        This method loads a DDS file. It will draw each Mip map in the DDS file to a separate QImage, and then
        arrange all the separate QImages into a final QImage which shows all the Mip maps in descrending order,
        from biggest to smalles Mip map.
        """
        # load the DDS image
        dds = py_dds.DDSImage(filename)
        # print DDS image information
        print("file:   ", filename)
        print("width:  ", dds.width(0))
        print("height: ", dds.height(0))
        print("mips:   ", dds.mip_count())
        print("format: ", dds.format())
        # gather all Mip map widths
        widths = [dds.width(i) for i in range(0, dds.mip_count())]
        # prepare a new QImage to draw to
        self.final = QImage(sum(widths), dds.height(0), QImage.Format_ARGB32)
        self.final.fill(qRgb(255, 0, 255))  # fill background with purple to make DDS image transparency obvious
        x_offset = 0
        for i in range(0, dds.mip_count()):
            # create a new QImage to draw to
            img = QImage(dds.width(i), dds.height(i), QImage.Format_ARGB32)

            # use py_dds to draw to the just created QImage
            def set_pixel_callback(x, y, r, g, b, a):  # callback for drawing onto a QImage
                img.setPixel(x, y, qRgba(r, g, b, a))
            dds.draw(set_pixel_callback, i)

            # add the QImage to the final output image
            painter = QPainter(self.final)
            painter.drawImage(QPoint(x_offset, 0), img)
            painter.end()
            x_offset += dds.width(i)


if __name__ == "__main__":
    app = QApplication()
    mw = Window()
    mw.show()
    app.exec()
