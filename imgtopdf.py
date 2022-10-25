import os, img2pdf, wx, sys
from PIL import Image


def pdfy(path, files):
    A4 = img2pdf.cm_to_pt(21), img2pdf.cm_to_pt(29.7)
    layout = img2pdf.get_layout_fun(A4)
    with open(path, 'wb') as pdf:
        pdf.write(img2pdf.convert(files, layout_fun = layout))


class Finestra(wx.Frame):
    def __init__(self, par = None, tit = "Convertitore di immagini in PDF", dim = (750, 200)):
        super(Finestra, self).__init__(par, title = tit, size = dim)
        self.Center()
        self.pannello = wx.Panel(self)
        self.pannello.SetBackgroundColour('white')
        self.carattere = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT)
        wx.StaticText(self.pannello, label = 'File di origine: ', pos = (10, 30)).SetFont(self.carattere)
        wx.StaticText(self.pannello, label = 'File di destinazione: ', pos = (10, 80)).SetFont(self.carattere)
        self.TC = wx.TextCtrl(self.pannello, pos = (250,80), size = (350, 26), style = wx.TE_READONLY)
        self.b1 = wx.Button(self.pannello, label = "Sfoglia", pos = (160, 30))
        self.b2 = wx.Button(self.pannello, label = "Sfoglia", pos = (625, 80))
        self.b1.Bind(wx.EVT_BUTTON, self.bot_1)
        self.b2.Bind(wx.EVT_BUTTON, self.bot_2)
        self.b3 = wx.Button(self.pannello, label = "Converti", pos = (350, 125))
        self.b3.Disable()
        self.b3.Bind(wx.EVT_BUTTON, self.converti)
        self.Show()
        self.dir_1 = wx.FileDialog(self, 'File da convertire', style = wx.FD_OPEN | wx.FD_MULTIPLE)
        self.dir_2 = wx.FileDialog(self, 'Cartella e nome del file di destinazione', wildcard = "PDF files (*.pdf)|*.pdf", style = wx.FD_SAVE)
        self.Bind(wx.EVT_CLOSE, self.quit)


    def bot_1(self, e):
        if self.dir_1.ShowModal() == wx.ID_OK:
            self.fo = self.dir_1.GetPaths()
        else:
            return None
        if not self.TC.IsEmpty():
            self.b3.Enable()

    def bot_2(self, e):
        if self.dir_2.ShowModal() == wx.ID_OK:
            self.cd = self.dir_2.GetPath()
            self.TC.SetLabel(self.cd)
        else:
            return None
        if self.dir_1.GetPaths():
            self.b3.Enable()    

    def converti(self, e):
        pdfy(self.cd, self.fo)
        wx.MessageDialog(self, message = 'Il file è stato creato!', caption = "Operazione terminata", style = wx.OK | wx.ICON_WARNING).ShowModal()
        self.TC.Clear()
        self.b3.Disable()

    def quit(self, e):
        sys.exit()



app = wx.App()
f=Finestra()
app.MainLoop()

