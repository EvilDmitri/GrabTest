#!/usr/bin/python
# -*- coding: utf-8 -*-

# Программа для пробы библиотеки Grab
# http://grablib.org/docs/grab/tutorial.html

import wx
import os, sys
import random

from grab import Grab

from lxml.html import fromstring



class MyFrame(wx.Frame) :

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Grabber", size=(350, 350))
        panel = wx.Panel(self, -1)

        self.addressCtrl = wx.TextCtrl(panel, -1, "http://bash.im", pos=(10, 30), size=(230, 30), style=wx.TE_PROCESS_ENTER)

        startButton = wx.Button(panel, -1, "Start", pos=(250,30))
        startButton.Bind(wx.EVT_BUTTON, self.OnButtonStartCLick)

        self.outCtrl = wx.TextCtrl(panel, -1, "", pos=(10, 70), size=(230, 250), style=wx.TE_MULTILINE)



    def OnButtonStartCLick(self, event):
    # Взять строку адреса (TODO проверить на валидность), и сграбить)))
        g = Grab()
        address = self.addressCtrl.GetLineText(0)
        g.go(address)
        #g.go('http://bash.im/')
        #print g.xpath_text('//title')


        # Возвращает ПЕРВЫЙ!!! найденный элемент
#        Quote = g.xpath_text('//div[@class="text"]')
#        self.outCtrl.AppendText(Quote)


        # Составляем список, содержащий все цитаты
        ListOfQuotes = g.xpath_list('//div[@class="text"]')

        for elem in g.xpath_list('//div[@class="text"]'):
            print "- - - - - - - - - - -"
            print elem.text







        # И выбираем из него случайный элемент
        RandomQuote = ListOfQuotes[random.randint(1,len(ListOfQuotes))]

        print "- - - - - - - - - - -"

        # Почему печатается только первая строка????
        #print RandomQuote.text
        self.outCtrl.AppendText(RandomQuote.text)












if __name__ == '__main__':

    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()