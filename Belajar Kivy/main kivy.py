
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("Hello!!!")
    text_input_str = StringProperty("Heeey")
    slidervaluetxt = StringProperty("hey")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.my_text = str(self.count)
            self.count +=1
    
    def on_toggle_button_state(self, widget):
        print(f"toggle {widget.state}")
        if widget.state  ==  "normal":
            widget.text =  "OFF"
            self.count_enabled = False
    
        else:
            widget.text = "ON"
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print(f"Switch {widget.active}.")

    def onslidervalue(self,widget):
        print(int(widget.value))
        self.slidervaluetxt = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
   


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation=("lr-bt")
        self.padding= ("20dp", "20dp", "20dp", "20dp")
        for i in range(0,100):
            size = "100dp"
            b = Button(text=str(i+1), size_hint=(None, None), size=(size,size))
            self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass
class thelabApp(App):
    pass

class  CanvasEcample(Widget):
    pass

class CanvasExample2(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400,200,88))
            self.rect = Line(rectangle=(200,200,200,200))
            self.rectt = Rectangle(pos=(200,200), width=2)

    def on_button_aclick(self):
        print("foo")
        self.rectt.pos = (103,100)

    pass

thelabApp().run()