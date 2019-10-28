#####__Graphcs__################################
from graphics_teclas_simultaneas import *
win = GraphWin("Pomodoro", 250,200)
win.setCoords(0, 1000, 1000, 0)
win.setBackground("#333333")
win.ligar_Buffer()

#####__PyGame__#################################
import pygame 
pygame.init()
pygame.mixer.init()

#####__DateTime__#################################
import datetime

#####__START__####################################
ti = "00:00:00"
crono = Text(Point(500,500),str(ti))
crono.setStyle("bold")
crono.setSize(25)
crono.setTextColor("black")
crono.setOutline("white")
crono.draw(win)

##__WYM_==_What_You_Make__########################
wym = Text(Point(500,200),"404")
wym.setStyle("bold")
wym.setSize(25)
wym.setTextColor("#A700FF")
wym.draw(win)

while(True):
   ######__Productivity__#########################
   wym.setText("Productivity")
   win.getMouse()
   minutes = 0
   timestart = datetime.datetime.now()

   while(minutes < 2):
      x = win.checkKey_Buffer()
      win.update()

      if 'Escape' in x and 'Control_L' in x:
         time.sleep(0.3)
         x = win.checkKey_Buffer()
         win.update()
         break

      timenow = datetime.datetime.now()
      delta_time = timenow - timestart

      print( (delta_time).seconds )
      if (delta_time).seconds - minutes*60 >= 60:
         minutes += 1
         tistart = datetime.datetime.now()

      crono.setText(str(minutes) + ":"+str((delta_time).seconds - minutes*60)+":"+str(int((delta_time).microseconds/100000)))

   #####__Rest__###################################
   wym.setText("Rest")
   win.getMouse()
   minutes = 0
   timestart = datetime.datetime.now()
   while(minutes < 2):
      x = win.checkKey_Buffer()
      win.update()

      if 'Escape' in x and 'Control_L' in x:
         time.sleep(0.3)
         x = win.checkKey_Buffer()
         win.update()
         break

      timenow = datetime.datetime.now()
      delta_time = timenow - timestart

      print( (delta_time).seconds )
      if (delta_time).seconds - minutes*60 >= 60:
         minutes += 1
         tistart = datetime.datetime.now()

      crono.setText(str(minutes) + ":"+str((delta_time).seconds - minutes*60)+":"+str(int((delta_time).microseconds/100000)))

#####__END__####################################

win.close()