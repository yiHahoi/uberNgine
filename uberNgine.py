

import sys
import pygame
import random

#------#
# Vect #
#------#

class VECT:
    """
    2d vector
    """
    def __init__(self):
        self.x = 0
        self.y = 0


#------#
# Quad #
#------#

class QUAD:
    """
    4d vector
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0


#-------#
# Mouse #
#-------#

class MOUSE:
    """
    Estructura con el estado del mouse.
    """
    def __init__(self):
 	self.x = 0 # Posicion en el eje x del mouse dentro de la ventana.
 	self.y = 0 # Posicion en el eje y del mouse dentro de la ventana.
 	self.rButton = False # Estado del boton derecho del mouse.
 	self.lButton = False # Estado del boton izquierdo del mouse.


#---------#
# Teclado #
#---------#

class KEYBOARD:

    """
    Estructura con el estado del teclado.
    """

    def __init__(self):
 	self.up = False # Estado de la tecla arriba.
 	self.down = False # Estado de la tecla abajo.
	self.left = False # Estado de la tecla izquierda.
 	self.right = False # Estado de la tecla derecha.
 	self.q = False # Estado de la tecla q.
 	self.w = False # Estado de la tecla w.
 	self.e = False # Estado de la tecla e.
 	self.r = False # Estado de la tecla r.
 	self.a = False # Estado de la tecla a.
 	self.s = False # Estado de la tecla s.
 	self.d = False # Estado de la tecla d.
	self.f = False # Estado de la tecla f.
 	self.z = False # Estado de la tecla z.
 	self.x = False # Estado de la tecla x.
 	self.c = False # Estado de la tecla c.
	self.v = False # Estado de la tecla v.
	self.p = False # Estado de la tecla p.
 	self.space = False # Estado de la tecla espacio.
 	self.ctrl = False # Estado de la tecla control izquierdo.
 	self.alt = False # Estado de la tecla alt izquierdo.
 	self.shift = False # Estado de la tecla shift izquierdo.
 	self.tab = False # Estado de la tecla tab.
 	self.esc = False # Estado de la tecla Esc.



#--------#
# Camara #
#--------#

class CAMERA:

    def __init__(self):

        self.pos = VECT() # Vector de posicion de camara.
        self.vel = VECT() # Vector de velocidad de camara.
        self.accel = VECT() # Vector de aceleracion de camara.
        self.pan = VECT() # Vector de paneo de camara.
        self.width = 320 # Ancho de camara a mostrar en pantalla.
        self.height = 240 # Alto de camara a mostrar en pantalla.

        self.pos.x = 0
        self.pos.y = 0
        self.vel.x = 0.0
        self.vel.y = 0.0
        self.accel.x = 0.0
        self.accel.y = 0.0
        self.pan.x = 0
        self.pan.y = 0


#---------#
# Ventana #
#---------#

class WINDOW:
    """
    Estructura que almacena las propiedades de la ventana de juego.
    """

    def __init__(self):
	self.NAME = "uBeR'N'GiNe" # Titulo de la ventana.
	self.ICON = "uber.ico"# Icono del Motor.
        self.WIDTH = 640 # Ancho de la ventana.
        self.HEIGHT = 480 # Altura de la ventana.
	self.BPP = 24 # Bits por pixel a utilizar en la ventana.
        self.FPS = 60 # Tasa de refresco limite del programa.
        self.BACKGROUNDCOLOR = (255,255,255)
        self.maxDepth = 5
        self.mSeg = 1000/self.FPS # Periodo por Frame.
	self.lastClock = 0 # Ultimo tiempo almacenado por funcion fps().
	#self.Quit # Variable que controla el cierre de la ventana.
	self.PAUSE = False # Variable que identifica si el juego se encuentra en pausa (detiene variables de tiempo).
        self.minPauseTime = 200 # Tiempo minimo para que cambie el valor de la variable PAUSA al apretar la tecla p.
        self.totalPauseTime = 0 # Variable que aloja el tiempo total que se ha encontrado el estado de juego en pausa.
        self.stateSubTicks = 1 # Variable temporal para alojar un periodo de tiempo.

        self.DISPLAY = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_icon(pygame.image.load(self.ICON))
        pygame.display.set_caption(self.NAME)


#--------------------------------#
# Estructura principal del juego #
#--------------------------------#

class STATE:

    """
    Estructura principal del juego que contiene el estado actual.
    """

    def __init__(self):
        self.WIN = WINDOW() # Ventana del juego.
        self.MOUSE = MOUSE() # Variables de mouse.
        self.KEY = KEYBOARD() # Variables de teclado.
        self.CAM = CAMERA() # Camara del juego.
        self.TICKS = 0 # Tiempo del estado de juego en ms (no del programa, se detiene al pausar).
        self.DELTA = 10 # Delta de tiempo para frame (para calcular posicion).
        self.TIMESCALE = 1.0 # Factor de velocidad
        self.OBJ = [] # Vector que contiene todos los objetos del juego.
        #self.DATA = [] # Variables de juego que queremos mantener separadas del motor.


    def loadObj(self,fileName):

        obj = OBJECT()

        file = open(fileName, 'r')

        for line in file:


            words = line.split()

            if words[0] == 'object':
                obj.name = str(words[1])
            elif words[0] == 'pos':
                obj.pos.x = int(words[1])
                obj.pos.y = int(words[2])
            elif words[0] == 'vel':
                obj.vel.x = float(words[1])
                obj.vel.y = float(words[2])
            elif words[0] == 'accel':
                obj.accel.x = float(words[1])
                obj.accel.y = float(words[2])
            elif words[0] == 'depth':
                obj.depth = int(words[1])
            elif words[0] == 'mass':
                obj.mass = float(words[1])
            elif words[0] == 'ghost':
                if words[1] == 'True':
                    obj.ghost = True
                else:
                    obj.ghost = False
            elif words[0] == 'camRelative':
                if words[1] == 'True':
                    obj.camRelative = True
                else:
                    obj.camRelative = False
            elif words[0] == 'scale':
                obj.scale = float(words[1])
            elif words[0] == 'transparency':
                obj.transparency = float(words[1])
            elif words[0] == 'mirror':
                if words[1] == 'True':
                    obj.xMirror = True
                else:
                    obj.xMirror = False
                if words[2] == 'True':
                    obj.yMirror = True
                else:
                    obj.yMirror = False
            #Animaciones
            elif words[0] == 'animation':
                anim = ANIMATION()
                obj.anim.append(anim)
                obj.anim[-1].name = str(words[1])
            elif words[0] == 'imgFile':
                obj.anim[-1].frame = pygame.image.load(str(words[1])).convert_alpha()
            elif words[0] == 'frameDim':
                obj.anim[-1].frameWidth = int(words[1])
                obj.anim[-1].frameHeight = int(words[2])
            elif words[0] == 'fps':
                obj.anim[-1].fps = int(words[1])
            elif words[0] == 'loop':
                if words[1] == 'True':
                    obj.anim[-1].loop = True
                else:
                    obj.anim[-1].loop = False
            elif words[0] == 'subFrameTotal':
                obj.anim[-1].subFrameTotal = int(words[1])
                for ctr in range(int(words[1])):
                    subFrame = QUAD()
                    obj.anim[-1].subFrame.append(subFrame)
            elif words[0] == 'subFrameDim':
                obj.anim[-1].subFrameWidth = int(words[1])
                obj.anim[-1].subFrameHeight = int(words[2])

        file.close()

        #Se crean los subframes al final
        for anim in obj.anim:
            xPos = 0
            yPos = 0
            for frame in anim.subFrame:
                if xPos >= anim.frameWidth/anim.subFrameWidth:
                    xPos = 0
                    yPos += 1
                frame.x = xPos*anim.subFrameWidth
                frame.y = yPos*anim.subFrameHeight
                frame.w = anim.subFrameWidth
                frame.h = anim.subFrameHeight
                xPos += 1

        self.OBJ.append(obj)



#-------------#
# Animaciones #
#-------------#

class ANIMATION:

    """
    Estructura que almacena todos los datos de una animacion.
    """
   
    def __init__(self):

        self.name = 'anim'
        self.frame = 0 # Imagen que contiene las distintas frames de una animacion.
        self.frameWidth = 0
        self.frameHeight = 0
        self.subFrame = [] # Sub-imagenes de la animacion.
        self.subFrameTotal = 0
        self.subFrameCurrent = 0 # Imagen en la que se encuentra la animacion.
        self.subFrameWidth = 0 # Ancho de sub-imagen en pixeles.
        self.subFrameHeight = 0 # Alto de sub-imagen en pixeles.
	self.loop = True # La animacion se repite si loop=1.
	self.lastClock = 0 # Reloj actual de animacion.
	self.fps = 5 # Sub-imagenes por segundo de la animacion (velocidad).
        self.collision = [] # Lista con listas de Rects para calcular colisiones (una lista por subframe).



#---------#
# Objetos #
#---------#


class OBJECT:

    """
    Estructura que almacena los datos de cada objeto o personaje en el juego.
    """

    def __init__(self):

        self.name = 'obj'
        self.pos = VECT() # Vector de posicion del objeto.
        self.vel = VECT() # Vector de velocidad del objeto.
        self.accel = VECT() # Vector de aceleracion del objeto.
        self.depth = 0 # Profundidad en la que se encuentra el objeto.
        self.mass = 0.0 # Masa del objeto.
        self.scale = 1.0 # Ampliado de imagen.
        self.ghost = False # Objetos con ghost=True no colisionan.
        self.anim = [] # Lista de Animaciones del objeto.
        self.animCurrent = 0 # Animacion actual del objeto.
        self.camRelative = True # Posicion del objeto en relacion a la camara.
        self.transparency = 1.0 # Transparencia del objeto, 0.0=transparente, 1.0=visible.
        self.xMirror = False # Inversion horizontal.
        self.yMirror = False # Inversion vertical.








def updateInput(state):

    temp = pygame.mouse.get_pos()
    state.MOUSE.x = temp[0]
    state.MOUSE.y = temp[1]

    for event in pygame.event.get():
        #Se revisa si se cerro el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Se actualiza el estado del mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 0:
                state.MOUSE.rButton = True
            elif event.button == 1:
                state.MOUSE.lButton = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 0:
                state.MOUSE.rButton = False
            elif event.button == 1:
                state.MOUSE.lButton = False

        #Se actualiza el estado del teclado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state.KEY.up = True
            elif event.key == pygame.K_DOWN:
                state.KEY.down = True
            elif event.key == pygame.K_LEFT:
                state.KEY.left = True
            elif event.key == pygame.K_RIGHT:
                state.KEY.right = True
            elif event.key == pygame.K_q:
                state.KEY.q = True
            elif event.key == pygame.K_w:
                state.KEY.w = True
            elif event.key == pygame.K_e:
                state.KEY.e = True
            elif event.key == pygame.K_r:
                state.KEY.r = True
            elif event.key == pygame.K_a:
                state.KEY.a = True
            elif event.key == pygame.K_s:
                state.KEY.s = True
            elif event.key == pygame.K_d:
                state.KEY.d = True
            elif event.key == pygame.K_f:
                state.KEY.f = True
            elif event.key == pygame.K_z:
                state.KEY.z = True
            elif event.key == pygame.K_x:
                state.KEY.x = True
            elif event.key == pygame.K_c:
                state.KEY.c = True
            elif event.key == pygame.K_v:
                state.KEY.v = True
            #Boton de Pausa
            elif event.key == pygame.K_p:
                if state.KEY.p:
                    state.KEY.p = False
                    state.WIN.PAUSE = False
                else:
                    state.KEY.p = True
                    state.WIN.PAUSE = True
            elif event.key == pygame.K_SPACE:
                state.KEY.space = True
            elif event.key == pygame.K_LCTRL:
                state.KEY.ctrl = True
            elif event.key == pygame.K_LALT:
                state.KEY.alt = True
            elif event.key == pygame.K_LSHIFT:
                state.KEY.shift = True
            elif event.key == pygame.K_TAB:
                state.KEY.tab = True
            elif event.key == pygame.K_ESCAPE:
                state.KEY.esc = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                state.KEY.up = False
            elif event.key == pygame.K_DOWN:
                state.KEY.down = False
            elif event.key == pygame.K_LEFT:
                state.KEY.left = False
            elif event.key == pygame.K_RIGHT:
                state.KEY.right = False
            elif event.key == pygame.K_q:
                state.KEY.q = False
            elif event.key == pygame.K_w:
                state.KEY.w = False
            elif event.key == pygame.K_e:
                state.KEY.e = False
            elif event.key == pygame.K_r:
                state.KEY.r = False
            elif event.key == pygame.K_a:
                state.KEY.a = False
            elif event.key == pygame.K_s:
                state.KEY.s = False
            elif event.key == pygame.K_d:
                state.KEY.d = False
            elif event.key == pygame.K_f:
                state.KEY.f = False
            elif event.key == pygame.K_z:
                state.KEY.z = False
            elif event.key == pygame.K_x:
                state.KEY.x = False
            elif event.key == pygame.K_c:
                state.KEY.c = False
            elif event.key == pygame.K_v:
                state.KEY.v = False
            #elif event.key == pygame.K_p:
                #state.KEY.p = False
            elif event.key == pygame.K_SPACE:
                state.KEY.space = False
            elif event.key == pygame.K_LCTRL:
                state.KEY.ctrl = False
            elif event.key == pygame.K_LALT:
                state.KEY.alt = False
            elif event.key == pygame.K_LSHIFT:
                state.KEY.shift = False
            elif event.key == pygame.K_TAB:
                state.KEY.tab = False
            elif event.key == pygame.K_ESCAPE:
                state.KEY.esc = False



#Funcion para calcular la logica del estado de juego.
def logic(state):
    GetTicks(state);
    if(state.WIN.PAUSE == False):
        loop(state)



#Funcion para renderizar en pantalla el estado de juego
def render(state):

    #Actualizamos la animacion de cada obj.
    for ctrl1 in range(0, len(state.OBJ)):
        if len(state.OBJ[ctrl1].anim[state.OBJ[ctrl1].animCurrent].subFrame) > 1:
            animUpdate(state.OBJ[ctrl1].anim[state.OBJ[ctrl1].animCurrent], state)

    #Fondo blanco.
    state.WIN.DISPLAY.fill(state.WIN.BACKGROUNDCOLOR)
    #Dibujamos en orden de profundidad.
    for ctrl2 in range(0,state.WIN.maxDepth):
        for ctrl1 in range(0,len(state.OBJ)):
            if ctrl2 == state.OBJ[ctrl1].depth:
                drawObj(state.OBJ[ctrl1], state.CAM)

    #Actualizamos la pantalla.
    pygame.display.update()
    #Calculamos FPS y limitamos si corresponde.
    fps(state)



#Funcion para calcular los ticks de juego considerando las pausas.
def GetTicks(state):

    if state.WIN.PAUSE:
        state.WIN.totalPauseTime =  pygame.time.get_ticks() - state.TICKS
    else:
        temp = state.TICKS
        state.TICKS = pygame.time.get_ticks() - state.WIN.totalPauseTime
        state.TICKS = int(state.TICKS * state.TIMESCALE)
        state.DELTA = state.TICKS - temp
    return state.TICKS;



#Funcion para controlar los FPS
def fps(state):
    clocks = 0
    newTime = pygame.time.get_ticks()

    clocks = newTime - state.WIN.lastClock
    if clocks < state.WIN.mSeg:
        pygame.time.wait(state.WIN.mSeg - clocks)
    state.WIN.lastClock = pygame.time.get_ticks()


#Funcion para actualizar animaciones
def animUpdate(anim, state):
    if anim.loop == False and anim.subFrameCurrent == len(anim.subFrame)-1:
        return
    else:
        mSec = 1000/anim.fps # total de ms que dura cada frame de la animacion
        mSecTotal = mSec*len(anim.subFrame) # total de ms que dura la animacion
        clocks = state.TICKS - anim.lastClock # ticks transcurridos desde ultimo animUpdate()
        #clocks = max(0,clocks) # esta linea es para evitar ticks negativos causados por cambios de timescale.
        if clocks >= mSecTotal:
            while clocks >= mSecTotal:
                clocks -= mSecTotal
            anim.lastClock = state.TICKS - clocks
        anim.subFrameCurrent = clocks/mSec
        #print 'mSec: ',mSec,' mSecTotal: ',mSecTotal,' clocks: ',clocks,' anim.lastClock: ',anim.lastClock,' anim.subFrameCurrent: ',anim.subFrameCurrent


#Funcion para controlar la camara (version 1)
def camPan1(state):
    """
    t = 0.1;
    camMaxForceX = 10
    error = 0.00001
    #state->CAM.accel.x = 0;
    if state.OBJ[0].vel.x > state.CAM.vel.x:
        state.CAM.accel.x = camMaxForceX
    if state.OBJ[0].vel.x < state.CAM.vel.x:
        state.CAM.accel.x = -camMaxForceX
    state.CAM.vel.x +=  t*state.CAM.accel.x
    delta = state.OBJ[0].vel.x - state.CAM.vel.x
    if delta <= error or delta >= -error:
        state.CAM.accel.x = 0
        state.CAM.vel.x = state.OBJ[0].vel.x

    state.CAM.pos.x += t*state.CAM.vel.x
    printf("%f  %f\n", state->OBJ[0].accel.x,state->CAM.accel.x);*/
    """
    state.CAM.pos.x = state.OBJ[0].pos.x - 320
    state.CAM.pos.y = state.OBJ[0].pos.y - 240


#Funcion para controlar la camara (version 2)
def camPan2(state):
    if state.MOUSE.lButton: # Control de camara.
        state.CAM.pos.x +=  state.CAM.pan.x - state.MOUSE.x
        state.CAM.pos.y +=  state.CAM.pan.y - state.MOUSE.y
        state.CAM.pan.x = state.MOUSE.x
        state.CAM.pan.y = state.MOUSE.y

    if state.MOUSE.lButton == False:
        state.CAM.pan.x = state.MOUSE.x
        state.CAM.pan.y = state.MOUSE.y


def drawObj(obj, cam):
    animCurr = obj.animCurrent
    frame = obj.anim[animCurr].frame
    frameSize = frame.get_rect()
    frame2 = pygame.transform.scale(frame,(int(frameSize.width*obj.scale),int(frameSize.height*obj.scale)))
    subFrameCurr = obj.anim[animCurr].subFrameCurrent
    temp = obj.anim[animCurr].subFrame[subFrameCurr]
    rect = QUAD()
    rect.x = int(temp.x * obj.scale)
    rect.y = int(temp.y * obj.scale)
    rect.w = int(temp.w * obj.scale)
    rect.h = int(temp.h * obj.scale)

    out = pygame.Surface((rect.w,rect.h)).convert_alpha()
    out.fill((0,0,0,0))
    out.blit(frame2,(0,0),(rect.x,rect.y,rect.w,rect.h),pygame.BLEND_RGBA_ADD)
    out2 = pygame.transform.flip(out , obj.xMirror, obj.yMirror)

    rect2 = pygame.display.get_surface().get_rect()
    HEIGHT = rect2.h
    
    #Camara
    if obj.camRelative:
        state.WIN.DISPLAY.blit(out2,(obj.pos.x-cam.pos.x , (-obj.pos.y+HEIGHT-rect.h)-cam.pos.y))
    else:
        state.WIN.DISPLAY.blit(out2,(obj.pos.x , -obj.pos.y+HEIGHT-rect.h ))






#------------------#
# Codigo del juego #
#------------------#

"""
IDEA DE JUEGO:

Juego tipo plataformas donde se controla a un personaje mediante el teclado.
Tambien se puede usar el mouse para agarrar y mover al personaje o los distintos objetos del mapa.
"""

def setUp(state):

    miles = pygame.mixer.Sound("data/sound/output.wav")
    miles.play()
    #asyn = pygame.mixer.Sound("data/sound/Asynchronicity_0.ogg")
    #asyn.play()

    state.loadObj("data/chars/yiha/yiHa.txt")
    state.loadObj("data/maps/Fondo01/fondo.txt")

    



def loop(state):

    """
    if state.KEY.right:
        state.OBJ[0].animCurrent = 1
        state.OBJ[0].xMirror = False
        state.OBJ[0].pos.x += 8*state.TIMESCALE
    elif state.KEY.left:
        state.OBJ[0].animCurrent = 1
        state.OBJ[0].xMirror = True
        state.OBJ[0].pos.x -= 8*state.TIMESCALE
    elif state.KEY.space:
        state.OBJ[0].animCurrent = 2
    else:
        state.OBJ[0].animCurrent = 0
    """

    #  Por alguna razon falla el timescale variable xd
    #if state.KEY.up:
    #    state.TIMESCALE += 0.01
    #    state.TIMESCALE = min(5.0,state.TIMESCALE)
    #elif state.KEY.down:
    #    state.TIMESCALE -= 0.01
    #    state.TIMESCALE = max(0.01,state.TIMESCALE)



    if state.KEY.right:
        state.OBJ[0].animCurrent = 1
        state.OBJ[0].xMirror = False
        Fx = 0.1
        
    elif state.KEY.left:
        state.OBJ[0].animCurrent = 1
        state.OBJ[0].xMirror = True
        Fx = -0.1
        
    elif state.KEY.space:
        state.OBJ[0].animCurrent = 2
        #state.OBJ[0].pos.y += 20
        Fx = 0.0

    else:
        state.OBJ[0].animCurrent = 0
        Fx = 0.0
	state.OBJ[0].vel.x *= 0.92


    #Xf = Xo + Vxo*t + 0.5*Ax*t*t
    #Yf = Yo + Vyo*t + 0.5*Ay*t*t
    deltaT = state.DELTA
    state.OBJ[0].vel.x = state.OBJ[0].vel.x + state.OBJ[0].accel.x*deltaT
    state.OBJ[0].accel.x = Fx/state.OBJ[0].mass
    state.OBJ[0].pos.x += state.OBJ[0].vel.x*deltaT + 0.5*state.OBJ[0].accel.x*deltaT*deltaT
    state.OBJ[0].pos.y += state.OBJ[0].vel.y*deltaT + 0.5*state.OBJ[0].accel.y*deltaT*deltaT
    if state.OBJ[0].vel.x > 0.3:
    	state.OBJ[0].vel.x = 0.3
    if state.OBJ[0].vel.x < -0.3:
    	state.OBJ[0].vel.x = -0.3


#------#
# MAIN #
#------#

#Se inicializa pygame
pygame.init()
#Se crea variable de estado
state = STATE()
#Se cargan los datos de juego
setUp(state)
#Se inicializa el loop de juego
while True:
    #Game Loop
    camPan2(state)
    updateInput(state)
    logic(state)
    render(state)








