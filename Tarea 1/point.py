# Universidad del Valle de Guatemala
# Gabriela Paola Contreras Guerra
# Gráficos por computador --> SR1:Points

import struct as st

def char (c):
    return st.pack('=c', c.encode('ascii'))

def word(w):
    return st.pack ('=h', w)

def dword(d):
    return st.pack('=i',d)

def color( r,g,b):
    return bytes([int(b*255),
                  int(g*255),
                  int(r*255)]
                )
                    
class Renderer(object):
    
    def __init__(self, width, height):
        self.glinit(width, height)
        
    def glinit(self, width, height):
        self.glCreateWindow(width,height)
        self.clearColor =color(0,0,0) 
        self.currColor = color(1,0,0)
        self.glClear()
        self.glViewPort(0,0,self.width, self.height) 

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    def glViewPort(self, ejex, ejey, width, height):
        self.vpx = ejex
        self.vpy = ejey 
        self.vpwidth = width
        self.vpheight = height
     
    def glClearViewPort(self, clr= None):
        for x in range(self.vpx, self.vpx + self.vpwidth):
            for y in range( self.vpy, self.vpy + self.vpheight):
                self.Point(x,y,clr)

    def glClear(self):
        self.pixels = [[ self.clearColor 
                        for y in range(self.height)]  
                        for x in range (self.width)]  
    
    def glClearColor(self, r,g,b):
        self.clearColor = color(r,g,b)
    
    def glColor(self, r,g,b):
        self.currColor = color(r,g,b)
    
    def Point(self, x, y, clr =None):
        if (0 <= x < self.width) and (0<= y < self.height):
            self.pixels[x][y] = clr or self.currColor
    
    def glPoint(self, ndc_x, ndc_y, clr =None):
        xw = int ((ndc_x+1) * (self.vpwidth/2) + self.vpx)
        yw = int ((ndc_y+1) * (self.vpheight/2) + self.vpy)
    
        self.Point(xw,yw,clr)

    def glFinish(self, filename):
        with open(filename,"wb") as file:
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            
            file.write(dword( 14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))

            file.write(word(24))
            file.write(dword(0)) 
            file.write(dword(self.width * self.height * 3)) 
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            for y in range (self.height):
                for x in range (self.width):
                    file.write(self.pixels[x][y])