# hi guys
# Install dulu kivy,
# pip install  kivy (buat windows)
# pip3 install kivy (buat mac)
# (di terminal)


from typing import AsyncIterable, Sized
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
import threading
import nyimpen

# Define different Screen
class MainMenu(Screen):
    pass

class Peta(Screen):
    def pilih_padalarang(self):
        nyimpen.asal = 1
        asalupdated()
        return nyimpen.asal
    def pilih_baros(self):
        nyimpen.asal = 2
        asalupdated()
        return nyimpen.asal
    def pilih_pasteur(self):
        nyimpen.asal = 3
        asalupdated()
        return nyimpen.asal
    def pilih_pasirkoja(self):
        nyimpen.asal = 4
        asalupdated()
        return nyimpen.asal
    def pilih_kopo(self):
        nyimpen.asal = 5
        asalupdated()
        return nyimpen.asal
    def pilih_mohtoha(self):
        nyimpen.asal = 6
        asalupdated()
        return nyimpen.asal
    def pilih_buahbatu(self):
        nyimpen.asal = 7
        asalupdated()
        return nyimpen.asal


class HoverButton(Button):

    def __init__(self,**kwargs):
        super(HoverButton,self).__init__(**kwargs)
        self.size_hint = (1,None)
        self.height = 50
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        if self.collide_point(*pos):
            Clock.schedule_once(self.mouse_enter_css, 0)
        else:
            Clock.schedule_once(self.mouse_leave_css, 0)
    def mouse_leave_css(self, *args):
        self.background_normal ='photos/PINITB.png'if self.asal == 'ITB' else 'photos/pin_scaled.png'
        self.size_hint= 0.1,0.12
        self.text= ''
        Window.set_system_cursor('arrow')

    def mouse_enter_css(self, *args):
        self.size_hint=0.30,0.1
        self.background_normal='photos/label.png'
        self.text = self.asal
        self.font_name = 'fonts/emulogic.ttf'
        self.color = 0,0,0,1
        Window.set_system_cursor('hand')

class Identifikasi(Screen):
    count = 2.0
    instruksiID = StringProperty("Berapakah tinggi \n kendaraan Anda?")

    count_enabled = BooleanProperty(True)
    fasesatu = BooleanProperty(True)
    fasedua = BooleanProperty(False)
    fasetiga = BooleanProperty(False)
    tinggikendaraan = StringProperty("2.0")

    milihjenis_enabled = BooleanProperty(False)
    milihgandar_enabled = BooleanProperty(False)

    def golongansatu(self):
        nyimpen.golongan = 1
        return nyimpen.golongan
    def golongandua(self):
        nyimpen.golongan = 2
        return nyimpen.golongan
    def golongantiga(self):
        nyimpen.golongan = 3
        return nyimpen.golongan
    def golonganempat(self):
        nyimpen.golongan = 4
        return nyimpen.golongan
    def golonganlima(self):
        nyimpen.golongan = 5
        return nyimpen.golongan
    
    

    def on_tambahtinggi (self):
        if self.count_enabled == True:
            self.tinggikendaraan = str(round(self.count,2))
            self.count+=0.1
        if self.count <= 0:
            self.count_enabled = True
            self.count = 0.1
    
    def on_kurangitinggi (self):
        if self.count_enabled == True:
            self.tinggikendaraan = str(round(self.count,2))
            self.count-=0.1
        if self.count <=0:
            self.count_enabled = False
    
    def on_satuselesai(self):
        self.count_enabled = False
        self.fasesatu = False
        asalupdated()
        if self.count > 2.1:
            self.fasedua = True
            self.milihjenis_enabled = True
            self.instruksiID = "     Apakah jenis kendaraan \n     anda, Bis atau Truk?"
    
    def on_truk_duaselesai(self):
        self.fasedua = False
        self.fasetiga = True
        self.milihjenis_enabled = False
        self.milihgandar_enabled = True
        self.instruksiID = "      Berapa gandar?"

def asalupdated():
    print(nyimpen.asal)
    nyimpen.tujuan = nyimpen.asal
    print(nyimpen.tujuan)
    nyimpen.update = True

    dialogbelok = Jalan()
    dialogbelok.textmuncul()
    
    return nyimpen.tujuan, nyimpen.asal, nyimpen.update

class MasukTol(Screen):
    kiri_atm = 0.54
    tengahx_atm = 0.66
    kanan_atm = 0.78

    atas_atm = 0.45
    tengahy_atm = 0.29
    bawah_atm = 0.13
    instruksimasuk = StringProperty(f"Selamat datang di \nGerbang Masuk Tol. \nSilahkan scan kartu Anda!")
    textsaldo = StringProperty()

    bisanext = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(MasukTol,self).__init__(*args, **kwargs)
        self.ubahintsaldo = [str(int) for int in nyimpen.saldoawal]
        self.textsaldo = ''.join(self.ubahintsaldo)
        self.n = 0

    def updatelabelsaldo(self):
        threading.Thread(target=self.updatesaldo).start()

    def masukkansaldo(self):
        self.instruksimasuk = "Silakan masukan \n saldo Anda!"
        self.bisanext = True
        
    def updatesaldo(self):
        self.ubahintsaldo = [str(int) for int in nyimpen.saldoawal]
        self.textsaldo = ''.join(self.ubahintsaldo)
        print(self.ubahintsaldo)
        print(self.textsaldo)
        nyimpen.saldo = int(self.textsaldo)
        print(nyimpen.saldo)
        return self.textsaldo, self.ubahintsaldo
    
    def pencetsatu(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=1
            self.n +=1
            return nyimpen.saldoawal, self.n, self.textsaldo
    def pencetdua(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=2
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencettiga(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=3
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetempat(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=4
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetlima(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=5
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetenam(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=6
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencettujuh(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=7
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetdelapan(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=8
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetsembilan(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=9
            self.n +=1
            return nyimpen.saldoawal, self.n
    def pencetnol(self):
        if self.n < 6:
            nyimpen.saldoawal[self.n]=0
            self.n +=1
            return nyimpen.saldoawal, self.n


class ScanKartu(Button):
    def __init__(self,**kwargs):
        super(ScanKartu,self).__init__(**kwargs)
        self.size_hint = (1,None)
        self.height = 50
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        if self.collide_point(*pos):
            Clock.schedule_once(self.mouse_enter_css, 0)
        else:
            Clock.schedule_once(self.mouse_leave_css, 0)
    def mouse_leave_css(self, *args):
        self.background_normal ='photos/tapkartu.png'
        self.size_hint= 0.3,0.35
        Window.set_system_cursor('arrow')

    def mouse_enter_css(self, *args):
        self.size_hint=0.3,0.35
        self.background_normal='photos/kartu_hover.png'
        self.background_down='photos/kartu_clicked.png'
        self.anim_loop = 5
        self.font_name = 'fonts/emulogic.ttf'
        self.color = 0,0,0,1
        Window.set_system_cursor('hand')

class Jalan(Screen):
    nanyainbelok = False
    gerbang = ["Padalarang", "Baros", "Pasteur", "Pasir Koja", "Kopo", "Moh Toha", "Buah batu", "Cileunyi"]

    buttonnonyala = BooleanProperty(True)
    buttonyesnyala = BooleanProperty(True)
    buttonbayarnyala = BooleanProperty(False)

    posisibutton = NumericProperty(1)
    instruksibelok = StringProperty( f"Terdapat persimpangan \nke arah kanan dan kiri. \n\n Mau ke mana?")
    buttonyes_text = StringProperty(f"Kanan")
    buttonno_text = StringProperty(f"Kiri")

    def textmuncul(self):
        print("textmuncul")
        self.instruksibelok = f"Terdapat persimpangan ke arah \n {nyimpen.gerbang[nyimpen.asal-2]} dan {nyimpen.gerbang[nyimpen.asal]}. \n\n Mau ke mana?"
        self.buttonyes_text = f"{nyimpen.gerbang[nyimpen.asal-2]}"
        self.buttonno_text = f"{nyimpen.gerbang[nyimpen.asal]}"
        print("textmuncullagi")
        return self.instruksibelok, self.buttonyes_text, self.buttonno_text

    def on_buttonyes(self):
        self.instruksibelok = f"Dalam 500 m, mendekati \n gerbang tol {self.gerbang[nyimpen.tujuan-2]} \n\n Apa mau belok?"
        self.buttonbayarnyala = True
        self.buttonnonyala = False
        self.buttonyes_text = "Tidak"
        if nyimpen.tujuan > 2:
            nyimpen.tujuan -=1
        print(nyimpen.tujuan)
        return nyimpen.tujuan

    def on_buttonno(self):
        self.instruksibelok = f"Dalam 500 m, mendekati \n gerbang tol {self.gerbang[nyimpen.tujuan]} \n\n Apa mau belok?"
        self.buttonno_text = "Tidak"
        self.buttonbayarnyala = True
        self.buttonyesnyala = False
        print(nyimpen.tujuan)
        if nyimpen.tujuan <7:
            nyimpen.tujuan +=1
        elif nyimpen.tujuan ==7:
            pass
        return nyimpen.tujuan

    def posisibuttonbayar_atas(self):
        self.posisibutton = 0.16
        return self.posisibutton

    def posisibuttonbayar_bawah(self):
        self.posisibutton = 0.03
        return self.posisibutton
    def ayobayar(self):
        pembayaran()

def pembayaran():
    print(nyimpen.golongan)
    if (abs(nyimpen.tujuan-nyimpen.asal) ==1):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 2000
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 3000
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 4000
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 5000
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 6500
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==2):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 3500
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 5500
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 6500
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 8000
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 10000
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==3):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 4500
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 6500
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 8500
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 11000
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 13000
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==4):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 4500
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 6500
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 9000
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 11000
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 13500
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==5):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 4500
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 7000
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 9000
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 11500
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 13500
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==6):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 5500
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 10000
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 11500
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 14000
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 17000
    elif (abs(nyimpen.tujuan-nyimpen.asal) ==7):
        if nyimpen.golongan ==1:
            nyimpen.tarif = 9000
        elif nyimpen.golongan ==2:
            nyimpen.tarif = 15000
        elif nyimpen.golongan ==3:
            nyimpen.tarif = 17500
        elif nyimpen.golongan ==4:
            nyimpen.tarif = 21500
        elif nyimpen.golongan ==5:
            nyimpen.tarif = 26000
    print(nyimpen.tarif)
    return nyimpen.tarif


class Bayar(Screen):
    kiri_atm = 0.54
    tengahx_atm = 0.66
    kanan_atm = 0.78

    atas_atm = 0.45
    tengahy_atm = 0.29
    bawah_atm = 0.13
    instruksikeluar = StringProperty(f"Selamat datang di \nGerbang Keluar Tol. \nSilahkan scan kartu Anda!")
    saldotambahan = StringProperty()
    sudahtambahsaldo = BooleanProperty(False)
    texttarif = StringProperty()
    

    def __init__(self, *args, **kwargs):
        super(Bayar,self).__init__(*args, **kwargs)
        self.ubahintsaldotambah = [str(int) for int in nyimpen.saldotambah]
        self.saldotambahan = ''.join(self.ubahintsaldotambah)
        self.m = 0
        self.strukkeluar = False
        self.texttarif = str(000000)
        

    def munculkantarif(self):
        self.texttarif = str(nyimpen.tarif)
        self.instruksikeluar = f"Berikut merupakan tarif perjalanan \n dari gerbang {nyimpen.gerbang[nyimpen.asal-1]} \nke gerbang  {nyimpen.gerbang[nyimpen.tujuan-1]} "
        print(self.texttarif)
        if nyimpen.saldo >= nyimpen.tarif:
            self.keluar()
        elif nyimpen.saldo<nyimpen.tarif:
            self.gabisakeluar()
        return self.texttarif

    
    def udahinputsaldo(self):
        nyimpen.saldo+=int(self.saldotambahan)
        if nyimpen.saldo >= nyimpen.tarif:
            self.keluar()
        elif nyimpen.saldo<nyimpen.tarif:
            self.instruksikeluar = "maaf masih tidak cukup :("

    def gabisakeluar(self):
        self.instruksikeluar = "Saldo tidak cukup! \n Tambah saldo Anda!"
        self.sudahtambahsaldo = True
    def keluar(self):
        self.instruksikeluar = "Saldo cukup. \n Print struk Anda!"
        self.strukkeluar = True

    def updatelabelsaldo(self):
        threading.Thread(target=self.updatesaldo).start()

    def updatelabeltarif(self):
        threading.Thread(target=self.munculkantarif).start()
        
    def updatesaldo(self):
        self.ubahintsaldotambah = [str(int) for int in nyimpen.saldotambah]
        self.saldotambahan = ''.join(self.ubahintsaldotambah)
        print(self.ubahintsaldotambah)
        print(self.saldotambahan)
        return self.saldotambahan, self.ubahintsaldotambah
    

    def pencetsatu(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=1
            self.m +=1
            return nyimpen.saldotambah, self.m, self.saldotambahan
    def pencetdua(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=2
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencettiga(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=3
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetempat(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=4
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetlima(self):
        if self.m< 6:
            nyimpen.saldotambah[self.m]=5
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetenam(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=6
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencettujuh(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=7
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetdelapan(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=8
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetsembilan(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=9
            self.m +=1
            return nyimpen.saldotambah, self.m
    def pencetnol(self):
        if self.m < 6:
            nyimpen.saldotambah[self.m]=0
            self.m +=1
            return nyimpen.saldotambah, self.m

class Struk(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# Designate kv files
kv = Builder.load_file('jalan tol kivy.kv')

class AwesomeApp(App):
    asal = 0
    tujuan = 0

    gerbang = ["Padalarang", "Baros", "Pasteur", "Pasir Koja", "Kopo", "Moh Toha", "Buah batu", "Cileunyi"]
    def build(self):
        return kv

AwesomeApp().run()