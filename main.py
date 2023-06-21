import interface
from PyQt6.QtWidgets import *


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.musteriNo = ""
        self.musteriNoBilgi = ""
        self.isimSoyisim = ""
        self.yas = 18
        self.il = ""
        self.ilce = ""
        self.mahalle = ""
        self.medeniDurum = "Bekar"

        self.urunFiyati = 0
        self.urunAdet = 1
        
        self.sms = False
        self.telefon = False
        self.eposta = False

        self.teslimTarihi = ""
        self.tumBilgi = ""

        self.musteriler = [
            {
                "musteriNo": "1",
                "isim": "Berk Akkaya"
            },
            {
                "musteriNo": "2",
                "isim": "İrem Akkın"
            },
            {
                "musteriNo": "3",
                "isim": "Dilara Ozan Demirel"
            }
        ]

        self.ui.pushButton_kaydet.clicked.connect(self.siparisDetayiOlustur)

        self.ui.calendarWidget_teslimTarihi.clicked.connect(self.teslimTarihiDegistir)

        self.ui.comboBox_il.addItems(["İl giriniz", "İzmir", "Aydın", "Manisa"])
        self.ui.comboBox_il.currentIndexChanged.connect(self.ilDegistir)

        self.ui.comboBox_ilce.currentIndexChanged.connect(self.ilceDegistir)

        self.ui.checkBox_eposta.clicked.connect(self.checkBoxDegistir)
        self.ui.checkBox_telefon.clicked.connect(self.checkBoxDegistir)
        self.ui.checkBox_sms.clicked.connect(self.checkBoxDegistir)

        self.ui.dial_yas.valueChanged.connect(self.changeAge)

        self.ui.radioButton_bekar.clicked.connect(self.medeniDurumDegistir)
        self.ui.radioButton_evli.clicked.connect(self.medeniDurumDegistir)
        self.ui.radioButton_bekar.click()

        self.ui.horizontalSlider_urunAdet.valueChanged.connect(self.urunAdetDegistir)
        self.ui.lineEdit_urunFiyati.textEdited.connect(self.urunFiyatDegistir)

        self.ui.lineEdit_musteriNo.textEdited.connect(self.musteriNoBosKontrol)
        self.ui.lineEdit_musteriNo.returnPressed.connect(self.musteriNoDegistir)

        self.tumBilgileriKapat()
    

    def musteriNoBosKontrol(self):
        text = self.ui.lineEdit_musteriNo.text()
        
        if text == "":
            self.ui.lineEdit_musteriNoBilgi.setText("")
            self.ui.lineEdit_isimSoyisim.setText("")

            self.ui.statusbar.showMessage("Kayıt bulunamadı.")
            self.tumBilgileriKapat()
    
    def musteriNoDegistir(self):
        self.musteriNo = self.ui.lineEdit_musteriNo.text()
        eslesen = -1

        for i in range(len(self.musteriler)):
            if self.musteriler[i]["musteriNo"] == self.musteriNo:
                eslesen = i
                break
        
        if eslesen == -1:
            self.musteriNoBilgi = ""
            self.ui.lineEdit_musteriNoBilgi.setText("")

            self.isimSoyisim = ""
            self.ui.lineEdit_isimSoyisim.setText("")

            self.tumBilgileriKapat()

            self.ui.statusbar.showMessage("Kayıt bulunamadı.")

            return
        
        musteri = self.musteriler[eslesen]

        self.musteriNoBilgi = musteri["musteriNo"]
        self.ui.lineEdit_musteriNoBilgi.setText(musteri["musteriNo"])

        self.isimSoyisim = musteri["isim"]
        self.ui.lineEdit_isimSoyisim.setText(musteri["isim"])

        self.tumBilgileriAc()
        self.ui.statusbar.showMessage("Kayıt bulundu.")
        

    def ilDegistir(self):
        self.ui.comboBox_ilce.clear()
        self.il = self.ui.comboBox_il.currentText()

        self.ui.comboBox_ilce.setDisabled(True)
        self.ui.comboBox_mahalle.setDisabled(True)
        #self.ui.comboBox_mahalle.setDisabled(True)

        if self.il == "İl giriniz":
            self.il = ""

        if self.il == "İzmir":  #İzmir
            self.ui.comboBox_ilce.setDisabled(False)
            self.ui.comboBox_ilce.addItems(["İlçe giriniz", "Bornova", "Bayraklı", "Karşıyaka", "Buca"])
            self.ilce = ""
          
        elif self.il == "Aydın":  #Aydın
            self.ui.comboBox_ilce.setDisabled(False)
            self.ui.comboBox_ilce.addItems(["İlçe giriniz", "Kuşadası", "Söke", "Nazilli"])
            self.ilce = ""
            
        elif self.il == "Manisa":  #Manisa
            self.ui.comboBox_ilce.setDisabled(False)
            self.ui.comboBox_ilce.addItems(["İlçe giriniz", "Yunusemre", "Salihli", "Demirci"])
            self.ilce = ""
    

    def ilceDegistir(self):
        self.ilce = self.ui.comboBox_ilce.currentText()

        if self.ilce == "İlçe giriniz":
            self.ilce = ""
            self.ui.comboBox_mahalle.setEnabled(False)
        else:
            self.ui.comboBox_mahalle.setEnabled(True)

    

    def medeniDurumDegistir(self):
        for radio_button in self.ui.groupBox_2.findChildren(QRadioButton):
            if radio_button.isChecked():
                selected_option = radio_button.text()
                self.medeniDurum=selected_option      
                break

    def checkBoxDegistir(self):
        if self.ui.checkBox_sms.isChecked():
            self.sms = True
        else:
            self.sms = False
        
        if self.ui.checkBox_eposta.isChecked():
            self.eposta = True
        else:
            self.eposta = False
        
        if self.ui.checkBox_telefon.isChecked():
            self.telefon = True
        else:
            self.telefon = False
    

    def changeAge(self):
        self.yas = self.ui.dial_yas.value()
        self.ui.lcdNumber_yas.display(self.yas)


    def teslimTarihiDegistir(self):
        self.teslimTarihi = self.ui.calendarWidget_teslimTarihi.selectedDate().toString("dd.MM.yyyy")
        self.ui.lineEdit_teslimTarihi.setText(self.teslimTarihi)
    

    def tumBilgileriKapat(self):
        self.ui.groupBox_2.setDisabled(True)
        self.ui.groupBox_3.setDisabled(True)


    def tumBilgileriAc(self):
        self.ui.groupBox_2.setDisabled(False)
        self.ui.groupBox_3.setDisabled(False)

        self.ui.comboBox_ilce.setEnabled(False)
        self.ui.comboBox_mahalle.setEnabled(False)

    
    def urunAdetDegistir(self):
        self.urunAdet = self.ui.horizontalSlider_urunAdet.value()
        self.ui.lcdNumber_urunAdet.display(self.urunAdet)
    

    def urunFiyatDegistir(self):
        try:
            self.urunFiyati = int(self.ui.lineEdit_urunFiyati.text())
        except:
            self.urunFiyati = 0

    
    def siparisDetayiOlustur(self):
        if (self.il == "") or (self.ilce == "") or (self.urunFiyati == 0):
            return

        text = ""

        text += f"{self.musteriNo} no'lu {self.isimSoyisim} isimli kullanıcı {self.yas} yaşında ve {self.il} ili {self.ilce} ilçesinde oturmakta olup {self.medeniDurum}'dir. "

        text += f"Satın aldığı {self.urunAdet} adet ürün için {self.urunFiyati * self.urunAdet} TL ödemiştir. Ürün gönderim tarihi {self.teslimTarihi}'dir. "
        text += "İletişim seçenekleri: "

        if (not self.sms) and (not self.telefon) and (not self.eposta):
            text += "yok"
        else:
            if self.sms: text += "sms "
            if self.telefon: text += "telefon "
            if self.eposta: text += "eposta "
        
        self.ui.textEdit_tumBilgi.setText(text)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainUi()

    MainWindow.show()
    sys.exit(app.exec())
