from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from datetime import datetime
from kivy.uix.textinput import TextInput


def RGBConverter(r, g, b):
    return [percentage(r, 255), percentage(g, 255), percentage(b, 255), 1]


def percentage(part, whole):
    return round(float(part) / float(whole), 2)


bemerktColor = RGBConverter(255, 245, 157)
angeschautColor = RGBConverter(255, 238, 88)  # FFEE58 255, 238, 88
aktivBeschaeftigtColor = RGBConverter(253, 216, 53)  # FDD835 253, 216, 53
haendischAngefasstColor = RGBConverter(100, 255, 219)  # 64FFDA 100, 255, 219
fussGedruecktColorErfolgColor = RGBConverter(178, 255, 89)  # B2FF59 178, 255, 89
fussGedruecktColorMisserfolgColor = RGBConverter(255, 82, 82)  # FF5252 255, 82, 82
hilfeGesuchtColor = [1, 1, 1, 1]  # 000000
blackColor = [0, 0, 0, 1]

spielVerstandenColor = RGBConverter(121, 135, 203)  # 7986CB 121, 135, 203
spielNichtVerstandenColor = RGBConverter(149, 117, 205)  # 9575CD 149, 117, 205
spielGestartetColor = RGBConverter(156, 39, 176)  # 9C27B0 156, 39, 176
spielBeendetColor = RGBConverter(104, 58, 183)  # 673AB7 104, 58, 183


class PressurePlate(App):
        # Blank Für spontan neue kategorien hinzufügen (input field)
        # sprechen wir wirklich unsere zielgruppe an? oder nicht? 
    def build(self):
        Button.color = [0, 0, 0, 1]

        self.gapFiller = Button(background_normal="", background_color=blackColor, size_hint_x=None, width=300,
                                size_hint_y=None, height=300)
        self.gapFiller_right = Button(background_normal="", background_color=blackColor, size_hint_x=None, width=300,
                                      size_hint_y=None, height=300)
        self.hilfe_gesucht_button_right = Button(text="hilfe gesucht", on_press=self.plate02hilfeGesuchtAction,
                                                 background_normal="", size_hint_x=None, width=300, size_hint_y=None,
                                                 height=300)
        self.hilfe_gesucht_button = Button(text="hilfe gesucht", on_press=self.plate01hilfeGesuchtAction,
                                           background_normal="", size_hint_x=None, width=300, size_hint_y=None,
                                           height=300)
        self.reverseButton = Button(text="Rückgängig", on_press=self.plate01reverseAction, background_normal="",
                                    size_hint_x=None, width=300, size_hint_y=None, height=300, center=(0.5,0.5))

        ## LINKE SEITE
        self.bemerkt_button = Button(on_press=self.plate01BemerktAction, background_normal="img/bemerkt.png",
                                     size_hint_x=None, width=300, size_hint_y=None, height=300)
        self.angeschaut_button = Button(on_press=self.plate01angeschautAction, background_normal="img/angeschaut.png",
                                        size_hint_x=None, width=300, size_hint_y=None, height=300)
        self.aktiv_beschaeftigt_button = Button(on_press=self.plate01aktivBeschaeftigtAction,
                                                background_normal="img/aktivBeschaeftigt.png", size_hint_x=None,
                                                width=300, size_hint_y=None, height=300)
        self.haendisch_angefasst_button = Button(on_press=self.plate01haendischAngefasstAction,
                                                 background_normal="img/haendischAngefasst.png", size_hint_x=None,
                                                 width=300, size_hint_y=None, height=300)
        self.fuss_gedrueckt_erfolg_button = Button(on_press=self.plate01fussErfolgAction,
                                                   background_normal="img/fussGedruecktErfolg.png", size_hint_x=None,
                                                   width=300, size_hint_y=None, height=300)
        self.fuss_gedrueckt_misserfolg_button = Button(on_press=self.plate01fussMisserfolgAction,
                                                       background_normal="img/fussGedruecktMisserfolg.png",
                                                       size_hint_x=None, width=300, size_hint_y=None, height=300)

        self.spiel_verstanden_button = Button(on_press=self.plate01spielVerstandenAction,
                                              background_normal="img/spielVerstanden.png", size_hint_x=None, width=300,
                                              size_hint_y=None, height=300)
        self.spiel_nicht_verstanden_button = Button(on_press=self.plate01spielNichtVerstandenAction,
                                                    background_normal="img/spielNichtVerstanden.png", size_hint_x=None,
                                                    width=300, size_hint_y=None, height=300)
        self.spiel_gestartet_button = Button(on_press=self.plate01spielGestartetAction,
                                             background_normal="img/spielGestartet.png", size_hint_x=None, width=300,
                                             size_hint_y=None, height=300)
        self.spiel_beendet_button = Button(on_press=self.plate01spielBeendetAction,
                                           background_normal="img/spielBeendet.png", size_hint_x=None, width=300,
                                           size_hint_y=None, height=300)
        self.wildcard_text_button = TextInput(text='', width=300, height=300, on_double_tap=self.plate01SaveWildcardText, size_hint=(None, None))



        ## RECHTE SEITE
        self.bemerkt_button_right = Button(on_press=self.plate02BemerktAction, background_normal="img/bemerkt.png",
                                           size_hint_x=None, width=300, size_hint_y=None, height=300)
        self.angeschaut_button_right = Button(on_press=self.plate02angeschautAction,
                                              background_normal="img/angeschaut.png", size_hint_x=None, width=300,
                                              size_hint_y=None, height=300)
        self.aktiv_beschaeftigt_button_right = Button(on_press=self.plate02aktivBeschaeftigtAction,
                                                      background_normal="img/aktivBeschaeftigt.png", size_hint_x=None,
                                                      width=300, size_hint_y=None, height=300)
        self.haendisch_angefasst_button_right = Button(on_press=self.plate02haendischAngefasstAction,
                                                       background_normal="img/haendischAngefasst.png", size_hint_x=None,
                                                       width=300, size_hint_y=None, height=300)
        self.fuss_gedrueckt_erfolg_button_right = Button(on_press=self.plate02fussErfolgAction,
                                                         background_normal="img/fussGedruecktErfolg.png",
                                                         size_hint_x=None, width=300, size_hint_y=None, height=300)
        self.fuss_gedrueckt_misserfolg_button_right = Button(on_press=self.plate02fussMisserfolgAction,
                                                             background_normal="img/fussGedruecktMisserfolg.png",
                                                             size_hint_x=None, width=300, size_hint_y=None, height=300)

        self.spiel_verstanden_button_right = Button(on_press=self.plate02spielVerstandenAction,
                                                    background_normal="img/spielVerstanden.png", size_hint_x=None,
                                                    width=300, size_hint_y=None, height=300)
        self.spiel_nicht_verstanden_button_right = Button(on_press=self.plate02spielNichtVerstandenAction,
                                                          background_normal="img/spielNichtVerstanden.png",
                                                          size_hint_x=None, width=300, size_hint_y=None, height=300)
        self.spiel_gestartet_button_right = Button(on_press=self.plate02spielGestartetAction,
                                                   background_normal="img/spielGestartet.png", size_hint_x=None,
                                                   width=300, size_hint_y=None, height=300)
        self.spiel_beendet_button_right = Button(on_press=self.plate02spielBeendetAction,
                                                 background_normal="img/spielBeendet.png", size_hint_x=None, width=300,
                                                 size_hint_y=None, height=300)
        self.wildcard_text_button_right = TextInput(text='', width=300, height=300, on_double_tap=self.plate02SaveWildcardText, size_hint=(None, None))

        ## LAYOUT : LEFT SIDE
        self.leftRow1 = BoxLayout()
        self.leftRow1.add_widget(self.bemerkt_button)
        self.leftRow1.add_widget(self.angeschaut_button)
        self.leftRow1.add_widget(self.aktiv_beschaeftigt_button)

        self.leftRow2 = BoxLayout()
        self.leftRow2.add_widget(self.haendisch_angefasst_button)
        self.leftRow2.add_widget(self.fuss_gedrueckt_erfolg_button)
        self.leftRow2.add_widget(self.fuss_gedrueckt_misserfolg_button)

        self.leftRow3 = BoxLayout()
        self.leftRow3.add_widget(self.hilfe_gesucht_button)
        self.leftRow3.add_widget(self.spiel_verstanden_button)
        self.leftRow3.add_widget(self.spiel_nicht_verstanden_button)

        self.leftRow4 = BoxLayout()
        self.leftRow4.add_widget(self.wildcard_text_button)
        self.leftRow4.add_widget(self.spiel_gestartet_button)
        self.leftRow4.add_widget(self.spiel_beendet_button)

        self.leftSide = BoxLayout(orientation="vertical")
        self.leftSide.add_widget(self.leftRow1)
        self.leftSide.add_widget(self.leftRow2)
        self.leftSide.add_widget(self.leftRow3)
        self.leftSide.add_widget(self.leftRow4)

        ## LAYOUT : RIGHT SIDE
        self.rightRow1 = BoxLayout()
        self.rightRow1.add_widget(self.bemerkt_button_right)
        self.rightRow1.add_widget(self.angeschaut_button_right)
        self.rightRow1.add_widget(self.aktiv_beschaeftigt_button_right)

        self.rightRow2 = BoxLayout()
        self.rightRow2.add_widget(self.haendisch_angefasst_button_right)
        self.rightRow2.add_widget(self.fuss_gedrueckt_erfolg_button_right)
        self.rightRow2.add_widget(self.fuss_gedrueckt_misserfolg_button_right)

        self.rightRow3 = BoxLayout()
        self.rightRow3.add_widget(self.hilfe_gesucht_button_right)
        self.rightRow3.add_widget(self.spiel_verstanden_button_right)
        self.rightRow3.add_widget(self.spiel_nicht_verstanden_button_right)

        self.rightRow4 = BoxLayout()
        self.rightRow4.add_widget(self.wildcard_text_button_right)
        self.rightRow4.add_widget(self.spiel_gestartet_button_right)
        self.rightRow4.add_widget(self.spiel_beendet_button_right)

        self.rightSide = BoxLayout(orientation="vertical")
        self.rightSide.add_widget(self.rightRow1)
        self.rightSide.add_widget(self.rightRow2)
        self.rightSide.add_widget(self.rightRow3)
        self.rightSide.add_widget(self.rightRow4)

        ## LAYOUT TOGETHER
        self.layout = GridLayout(cols=3, padding=[30])
        self.layout.add_widget(self.leftSide)
        self.layout.add_widget(self.reverseButton)
        self.layout.add_widget(self.rightSide)

        return self.layout

    def plate01BemerktAction(self, instance):
        self.saveAction("bemerkt", "01")

    def plate01reverseAction(self, instance):
        self.saveAction("letzte aktion RÜCKGÄNGIG machen", "-")

    def plate01angeschautAction(self, instance):
        self.saveAction("angeschaut", "01")

    def plate01aktivBeschaeftigtAction(self, instance):
        self.saveAction("aktiv beschäftigt", "01")

    def plate01haendischAngefasstAction(self, instance):
        self.saveAction("händisch angefasst", "01")

    def plate01fussErfolgAction(self, instance):
        self.saveAction("fuss gedrückt - ERFOLG", "01")

    def plate01fussMisserfolgAction(self, instance):
        self.saveAction("fuss gedrückt - MISSERFOLG", "01")

    def plate01hilfeGesuchtAction(self, instance):
        self.saveAction("hilfe gesucht", "01")

    def plate01spielVerstandenAction(self, instance):
        self.saveAction("spiel verstanden", "01")

    def plate01spielNichtVerstandenAction(self, instance):
        self.saveAction("spiel nicht verstanden", "01")

    def plate01spielGestartetAction(self, instance):
        self.saveAction("spiel gestartet", "01")

    def plate01spielBeendetAction(self, instance):
        self.saveAction("spiel beendet", "01")

    def plate01SaveWildcardText(self, instance):
        self.saveAction(self.wildcard_text_button.text, "01")
        self.wildcard_text_button.text = ""

    def plate02BemerktAction(self, instance):
        self.saveAction("bemerkt", "02")

    def plate02reverseAction(self, instance):
        self.saveAction("letzte aktion RÜCKGÄNGIG machen", "02")

    def plate02angeschautAction(self, instance):
        self.saveAction("angeschaut", "02")

    def plate02aktivBeschaeftigtAction(self, instance):
        self.saveAction("aktiv beschäftigt", "02")

    def plate02haendischAngefasstAction(self, instance):
        self.saveAction("händisch angefasst", "02")

    def plate02fussErfolgAction(self, instance):
        self.saveAction("fuss gedrückt - ERFOLG", "02")

    def plate02fussMisserfolgAction(self, instance):
        self.saveAction("fuss gedrückt - MISSERFOLG", "02")

    def plate02hilfeGesuchtAction(self, instance):
        self.saveAction("hilfe gesucht", "02")

    def plate02spielVerstandenAction(self, instance):
        self.saveAction("spiel verstanden", "02")

    def plate02spielNichtVerstandenAction(self, instance):
        self.saveAction("spiel nicht verstanden", "02")

    def plate02spielGestartetAction(self, instance):
        self.saveAction("spiel gestartet", "02")

    def plate02spielBeendetAction(self, instance):
        self.saveAction("spiel beendet", "02")

    def plate02SaveWildcardText(self, instance):
         self.saveAction(self.wildcard_text_button_right.text, "02")
         self.wildcard_text_button_right.text = ""

    def saveAction(self, actionname, whichPlate):
        dateTimeObj = datetime.now()
        filename = "nutzerstudie_pressureplate_" + dateTimeObj.strftime("%d_%m_%Y") + ".txt"
        File_object = open(filename, "a")

        output = dateTimeObj.strftime("%d.%m.%Y,%H:%M:%S," + actionname + "," + whichPlate + "\n")
        File_object.write(output)
        print(output)

        File_object.close()


PressurePlate().run()
