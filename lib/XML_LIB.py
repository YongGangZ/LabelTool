#-*- coding:utf-8 -*-

import codecs
from lxml import etree
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


class XMLWrite:

    def __init__(self,folder_path,file_name):
        self.folder_path = folder_path
        self.file_name = file_name
        self.top = Element('Images')
        self.object = None

    def create_object(self,path,object_name = 'objectName',tag_name = 'FilePath'):
        self.object = SubElement(self.top, object_name)
        self.object.set(tag_name, path)

    def set_lable_info(self, lable ,lable_name='LableName'):
        if self.object == None:
            raise Exception('没有创建object对象，create_object方法')
        plate = SubElement(self.object, lable_name)
        plate.text = lable

    def set_object_info(self,tag_name = 'Size',**args):
        if self.object == None:
            raise Exception('没有创建object对象，create_object方法')

        size = SubElement(self.object, tag_name)
        for key in args:
            sub = SubElement(size, key)
            sub.text = str(args[key])

        # width = SubElement(size, 'width')
        # width.text = '500'
        # heigth = SubElement(size, 'heigth')
        # heigth.text = '400'
        # depth = SubElement(size,'width')
        # depth.text = '3'

    def set_position_rect(self,tag_name = 'Position',**args):
        if self.object == None:
            raise Exception('没有创建object对象，create_object方法')
        point = SubElement(self.object, tag_name)

        for key in args:
            sub = SubElement(point, key)
            sub.text = str(args[key])

    def set_position_scat(self, tag_name = 'Position',info = None):
        if self.object == None:
            raise Exception('没有创建object对象，create_object方法')
        point = SubElement(self.object,tag_name)
        for key in info:
            sub = SubElement(point, key)
            sub.set('x',str(info[key][0]))
            sub.set('y', str(info[key][1]))

    def prettify(self, elem):
        rough_string = ElementTree.tostring(elem, 'utf8')
        root = etree.fromstring(rough_string)
        return etree.tostring(root, pretty_print=True, encoding='utf-8').replace("  ".encode(), "\t".encode())


    def save(self,targetFile=None):
        #root = self.genXML()
        out_file = None
        if targetFile is None:
            out_file = codecs.open(self.file_name + '.xml', 'w', encoding='utf-8')
        else:
            out_file = codecs.open(targetFile, 'w', encoding='utf-8')
        prettifyResult = self.prettify(self.top)
        out_file.write(prettifyResult.decode('utf8'))
        out_file.close()
