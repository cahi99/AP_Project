MDTextField:
    hint_text :"Enter Username"
    helper_text: 'Olvidaste tu usuario?'
    helper_text_mode: 'on_focus'
    icon_right : 'android'
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5, 'center_y':0.5}
    size_hint_x:None
    width:300



    def build(self):
        screen= Screen()
        self.theme_cls.primary_palette="Green"
        button = MDRectangleFlatButton(text='show',pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
        self.username = Builder.load_file('logg.kv')
        screen.add_widget(self.username)
        screen.add_widget(button)
        #screen.add_widget(button)
        return screen

    def show_data(self,obj):
        if self.username.text is "":
            check_string = "Please enter a username"
        else:
                check_string= self.username.text
        close_button = MDFlatButton(text='Close',on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog=MDDialog(text=check_string,size_hint=(0.5,1),buttons=[close_button,more_button])
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()