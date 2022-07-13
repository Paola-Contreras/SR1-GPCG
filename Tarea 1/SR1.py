# Universidad del Valle de Guatemala
# Gabriela Paola Contreras Guerra
# Gráficos por computador --> SR1:Points

from point import Renderer, color 

#Screen size data 
w = 300
h = 300

#Viewport data 
w2 = int( w / 2 )
h2 = int ( h / 2 )
ejex = int( w / 4 )
ejey = int( h / 4 )

#Size of my screen 
rend = Renderer(w,h)

#Viewport size
rend.glViewPort(ejex,ejey,w2,h2)

#Background color 
rend.glClearColor(1,1,1)
rend.glClear()
rend.glClearViewPort(color(0,0,0))

#Dot color 
rend.glColor(0,1,0)

#Dot coordinates 
rend.glPoint(0,0)


#Generate BMP
rend.glFinish("output1.bmp")