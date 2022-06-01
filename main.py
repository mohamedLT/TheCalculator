from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label



class MainApp(App):
    def number_btn(self,inst):
        txt = inst.text
        if txt in ["+","-","*","/","%","="] and self.res=="" and self.res_label.text!="SYNTAX ERROR" and self.res!=self.res_label.text:
            self.res = self.res_label.text+txt
            self.res_label.text=self.res
            return
        if txt=="AC":
            self.res=""
            self.res_label.text=self.res
            return
        if txt!="=":
            self.res+=txt
            self.res_label.text=self.res
            return
        else :
            try:
                exec("self.res_label.text=str({r})".format(r=self.res))
            except :
                self.res_label.text = "SYNTAX ERROR"
            finally:
                self.res=""
            return


    def build(self):
        self.res = ""
        main_lay = BoxLayout(orientation='vertical')
        self.res_label = Label(text=self.res,size_hint_y=.3)
        buttons_layout = GridLayout(cols=4,rows=5,size_hint_y=.7)
        for i in ["(",")","%","AC",7,8,9,"/",4,5,6,"*",1,2,3,"-",0,".","=","+"]:
            b= Button(text=str(i))
            b.bind(on_press=self.number_btn)
            buttons_layout.add_widget(b)
        main_lay.add_widget(self.res_label)
        main_lay.add_widget(buttons_layout)
        return main_lay
        
    


MainApp().run()