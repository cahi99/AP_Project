from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.imagelist import SmartTileWithLabel
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.uix.menu import  RightContent

KV='''
<RightContentCls>
    MDIconButton:
        icon:'plus'
        pos_hint: {"center_x": .5, "center_y": .5}
    
    MDLabel:
        text: "0"
        theme_text_color: "Secondary"
        hading: 'center'
    MDIconButton:
        icon:'minus'
        pos_hint: {"center_x": .5, "center_y": .5}


<MyCard@MDCard>
    cards:cards
    n_producto:n_producto
    id:cards
    orientation: "vertical"
    padding: "10dp"
    spading: "10dp"
    size_hint: .5, None
    size: "260dp", "180dp"
    pos_hint: {"center_x": .5, "center_y": .5}
    SmartTileWithLabel:
        source: "Imagenes/Productos/plato_6.jpg"
        width:self.height
    MDGridLayout:
        cols:2
        adaptive_height: True
        MDLabel:
            id:n_producto
            text: root.nombres
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": .5, "center_y": .5}
            hading: 'center'
        RightContentCls:
            hading: 'center'
    
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Productos"
                        left_action_items:[['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items:[['cart',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5
                
                    ScrollView:
                        MDGridLayout:
                            id:box
                            cols: 3
                            adaptive_height: True
                            padding: dp(8), dp(8)
                            spacing: dp(8), dp(8)
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation:'vertical'
                spacing: '6dp'
                padding: '6dp'
                Image:
                    source: 'Imagenes/2.jpg'
                MDLabel:
                    text: 'Mi Tienda'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Distribuidores'
                            IconLeftWidget:
                                icon: 'store'
                        OneLineIconListItem:
                            text: 'Mis Pedidos'
                            IconLeftWidget:
                                icon: 'cart'
'''
class MyCard(MDCard):
    pass
class RightContentCls(RightContent):
    pass

class ProductosApp(MDApp):
    cards = ObjectProperty(None)
    nombres= StringProperty('0')
    n_producto = ObjectProperty(None)
    def build(self):
        screen = Builder.load_string(KV)
        for i in range(8):
            screen.ids.box.add_widget(
                MyCard()
            )
        for i in screen.ids:
            print(self.n_producto.text)
        return screen


ProductosApp().run()