import ctypes
import sys
import re
from PyQt5.QtWidgets import *
from ilkui import *
from ikinciui import *
from Ucui import *
from HastaAramaui import *
from Aramaui import *
from Acılısui import *
import speech_recognition as sr
import time
import threading
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
import numpy as np
from PIL import Image
import os

# ----------------------------Arayüz---------------------
Uygulama = QApplication(sys.argv)

KayıtPen = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(KayıtPen)

SecmePen = QMainWindow()
ui2 = Ui_Dialog()
ui2.setupUi(SecmePen)

SıraPen = QMainWindow()
ui3 = Ui_Form()
ui3.setupUi(SıraPen)

WelcomeHomePage = QMainWindow()
ui4 = Ui_HomePage()
ui4.setupUi(WelcomeHomePage)

HastaArama = QMainWindow()
ui5 = Ui_HastaArama()
ui5.setupUi(HastaArama)

Kamera = QMainWindow()
ui6 = Ui_Cam()
ui6.setupUi(Kamera)

WelcomeHomePage.show()

# ---------------------------VeriTabanı---------------------
import sqlite3
import datetime

global curs
global conn

conn = sqlite3.connect('Hospital.db')  # db veri tabanı yoksa oluşturur
curs = conn.cursor()  # veri tabanı ile dialog kurmayı sağlıyor.

# --------------------------------------------------------------------------------------------------------
def _record():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    liste = []
    Zaman = datetime.datetime.now()
    Day = int(Zaman.strftime("%d"))
    Mount = int(Zaman.strftime("%m"))
    Year = int(Zaman.strftime("%Y"))
    for x in range(3):
        recognizer1 = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer1.adjust_for_ambient_noise(source, duration=1)
            print("Recording for 5 seconds")
            recorded_audio = recognizer1.listen(source, timeout=5, phrase_time_limit=5)
            print("Done recording")
        try:
            print("Recognizing the text")
            text1 = recognizer1.recognize_google(recorded_audio, language='tr')
            print("Decoded Text : {}".format(text1))
            liste.append(text1)

        except Exception as ex:
            print(ex)

    LisDay = int(liste[0])
    LisAy = int(liste[1])
    LisYıl = int(liste[2])

    if LisYıl > Year:
        print("Error Year Big")
        ctypes.windll.user32.MessageBoxW(0, "Year Big", "YEAR", 0)
    elif LisYıl == Year:
        ui.LineYear.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[2]))))
        if LisAy > Mount:
            print("Mistake Month Is Bigger Than This Month")
            ctypes.windll.user32.MessageBoxW(0, "The Month You Entered Is Greater Than The Current Month", "MONTH", 0)
        elif LisAy > 12:
            print("Error Month Greater Than 12")
            ctypes.windll.user32.MessageBoxW(0, "Month Greater Than 12", "MONTH", 0)
        else:
            ui.LineMounth.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[1]))))
            if LisDay > Day:
                print("Error Day Greater Than Today")
                ctypes.windll.user32.MessageBoxW(0, "The Day Is Greater Than Current Time", "DAY", 0)
            elif LisDay > 31:
                print("Error Day Greater Than 31")
                ctypes.windll.user32.MessageBoxW(0, "Day Greater Than 31", "DAY", 0)
            else:
                ui.LineDay.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[0]))))
    else:
        ui.LineYear.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[2]))))
        if LisAy > 12:
            print("Error Month Is Greater Than 12")
            ctypes.windll.user32.MessageBoxW(0, "Month Is Greater Than 12", "MONTH", 0)
        else:
            ui.LineMounth.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[1]))))
            if LisDay > 31:
                print("Error Day Greater Than 31")
                ctypes.windll.user32.MessageBoxW(0, "Day Greater Than 31", "DAY", 0)
            else:
                ui.LineDay.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[0]))))

# --------------------------------------------------------------------------------------------------------
def _TcRecord(a):
    deneme = threading.Thread(target=showTime)
    deneme.start()
    liste = []
    for x in range(1):
        recognizer1 = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer1.adjust_for_ambient_noise(source, duration=1)
            print("Recording for 10 seconds")
            recorded_audio = recognizer1.listen(source, timeout=10, phrase_time_limit=10)
            print("Done recording")
        try:
            print("Recognizing the text")
            text1 = recognizer1.recognize_google(recorded_audio, language='tr')
            print("Decoded Text : {}".format(text1))
            liste.append(text1)

        except Exception as ex:
            print(ex)
    if a == "1":
        ui5.LineTcGiris.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[0]))))
        text = ui5.LineTcGiris.text()
    elif a == "2":
        ui.LineTc.setText("{}".format(int(re.sub('[\s+|\W+]', '', liste[0]))))
        text = ui.LineTc.text()
    elif a == "3":
        ui.LineAd.setText("{}".format(liste[0].title()))
        text = ui.LineAd.text()
    elif a == "4":
        ui.LineSoyad.setText("{}".format(liste[0]).upper())
        text = ui.LineSoyad.text()

    print("text: " + text)
    print(a)
# -------------------------------- Welcome ---------------------------------------------------------
def _WelcomeRecord():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    for x in range(1):
        recognizer1 = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer1.adjust_for_ambient_noise(source, duration=1)
            print("Recording for 10 seconds")
            recorded_audio = recognizer1.listen(source, timeout=10, phrase_time_limit=10)
            print("Done recording")
        try:
            print("Recognizing the text")
            textWel = recognizer1.recognize_google(recorded_audio, language='tr')
            print("Decoded Text : {}".format(textWel))
        except Exception as ex:
            _WelcomeRecord()

        textOpen = str(textWel)
        print(textOpen)
    while True:
        if textWel == "open":
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif textWel == "Open":
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif textWel == "OPEN":
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' open ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' Open ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' OPEN ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif 'open ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif 'Open ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif 'OPEN ' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' open' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' Open' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        elif ' OPEN' in textOpen:
            WelcomeHomePage.hide()
            Kamera.show()
            acılıs()
            break
        else:
            _WelcomeRecord()

# --------------------------------------------------------------------------------------------------------
def arayuz(a):
    t2 = threading.Thread(target=_TcRecord(a))
    t2.daemon = True
    t2.start()
    t2.join()

def arayuz2():
    t1 = threading.Thread(target=_record)
    t1.daemon = True
    t1.start()
    t1.join()
# --------------------------------------------------------------------------------------------------------
def _kamera():
    ui.cap = cv2.VideoCapture(0)
    a = int(0)
    sor = "SELECT COUNT(Patient_id_tc) FROM Patient "
    curs.execute(sor, )
    data = curs.fetchall()
    c = str(data)
    b = c.strip("'[( ,)]")
    print(b)
    i = int(b)
    i = i + 1
    print(i)
    n = str(i)
    while True:
        face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
        ret, img = ui.cap.read()
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
        ui.label.setPixmap(QPixmap.fromImage(qImg))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        yuzler = face_detector.detectMultiScale(gray, 1.3, 5)
        a = a + 1
        for (x, y, w, h) in yuzler:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite('VeriDepo/%s.%s.jpg' % (n, a,), gray[y:y + h, x:x + w])
        if cv2.waitKey(1) & a == 50:
            break

    ui.cap.release()
    cv2.destroyAllWindows()
# ------------------------------------------------------------------------------------------------
def Tanımlama():
    path = 'VeriDepo'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

    # imajların alınması ve etiketlenmesi için fonksiyon
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        ornekler = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # gri
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[0])
            print("id= ", id)
            yuzler = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in yuzler:
                ornekler.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return ornekler, ids

    print("\n [INFO] yuzler eğitiliyor. Birkaç saniye bekleyin ...")
    yuzler, ids = getImagesAndLabels(path)
    recognizer.train(yuzler, np.array(ids))
    print(recognizer.train(yuzler, np.array(ids)))
    # Modeli egitim/egitim.yml dosyasına kaydet
    recognizer.write('egitim/egitim.yml')  # Dikkat! recognizer.save() Raspberry Pi üzerinde çalışmıyor
    # Eğitilen yüz sayısını göster ve kodu sonlandır
    print(f"\n [INFO] {len(np.unique(ids))} yüz eğitildi. Betik sonlandırılıyor.")

# ---------------------------Kayıt Ekleme---------------------
def Kayit():
    _tc = ui.LineTc.text()
    _name = ui.LineAd.text()
    _surname = ui.LineSoyad.text()
    _dateDay = ui.LineDay.text()
    _dateMonth = ui.LineMounth.text()
    _dateYear = ui.LineYear.text()
    _date = (_dateDay + "." + _dateMonth + "." + _dateYear)
    curs.execute("INSERT INTO Patient VALUES (?, ?, ?, ?)", (_tc, _name, _surname, _date,))
    conn.commit()
    deneme = threading.Thread(target=Tanımlama)
    deneme.start()
    SecmePen.show()
    KayıtPen.close()


# ---------------------------Combobox Seçme---------------------
def Secim():
    deneme = threading.Thread(target=showTime3)
    deneme.start()
    _tc = ui5.LineTcGiris.text()
    Zaman = datetime.datetime.now()
    _Date1 = Zaman.strftime("%d.%m.%Y")
    secim = ui2.comboBox.currentText()
    print("text :", secim)
    if secim == "Dentist":
        _BolumID = "1"
        _DoctorId = "3"
        _tc = ui5.LineTcGiris.text()
        Zaman = datetime.datetime.now()
        _Date = Zaman.strftime("%d.%m.%Y")
        _Time = Zaman.strftime("%H:%M:%S")
        curs.execute(
            "INSERT INTO Appointment(Policlinic_id,Patient_id_tc,Doctor_id,Time,Date) VALUES (?, ?, ?,? ,?)",
            (_BolumID, _tc, _DoctorId, _Time, _Date))
    elif secim == "General Surgeon":
        _BolumID = "2"
        _DoctorId = "5"
        _tc = ui5.LineTcGiris.text()
        Zaman = datetime.datetime.now()
        _Date = Zaman.strftime("%d.%m.%Y")
        _Time = Zaman.strftime("%H:%M:%S")
        curs.execute("INSERT INTO Appointment(Policlinic_id,Patient_id_tc,Doctor_id,Time,Date) VALUES (?, ?, ?,? ,?)",
                     (_BolumID, _tc, _DoctorId, _Time, _Date))
    elif secim == "Dermotology":
        _BolumID = "3"
        _DoctorId = "1"
        _tc = ui5.LineTcGiris.text()
        Zaman = datetime.datetime.now()
        _Date = Zaman.strftime("%d.%m.%Y")
        _Time = Zaman.strftime("%H:%M:%S")
        curs.execute("INSERT INTO Appointment(Policlinic_id,Patient_id_tc,Doctor_id,Time,Date) VALUES (?, ?, ?,? ,?)",
                     (_BolumID, _tc, _DoctorId, _Time, _Date))
    elif secim == "Psychiatry":
        _BolumID = "4"
        _DoctorId = "2"
        _tc = ui5.LineTcGiris.text()
        Zaman = datetime.datetime.now()
        _Date = Zaman.strftime("%d.%m.%Y")
        _Time = Zaman.strftime("%H:%M:%S")
        curs.execute("INSERT INTO Appointment(Policlinic_id,Patient_id_tc,Doctor_id,Time,Date) VALUES (?, ?, ?,? ,?)",
                     (_BolumID, _tc, _DoctorId, _Time, _Date))
    elif secim == "Infectious Diseases":
        _BolumID = "5"
        _DoctorId = "4"
        _tc = ui5.LineTcGiris.text()
        Zaman = datetime.datetime.now()
        _Date = Zaman.strftime("%d.%m.%Y")
        _Time = Zaman.strftime("%H:%M:%S")
        curs.execute("INSERT INTO Appointment(Policlinic_id,Patient_id_tc,Doctor_id,Time,Date) VALUES (?, ?, ?,? ,?)",
                     (_BolumID, _tc, _DoctorId, _Time, _Date))
    else:
        print("HATA")

    print("_BolumID :", _BolumID)
    print("_DoctorId :", _DoctorId)
    print("_tc :", _tc)
    print("_Date :", _Date)
    print("_Time :", _Time)
    conn.commit()
    SıraPen.show()
    SecmePen.close()

    secim = ui2.comboBox.currentText()
    print("text :", secim)
    Tc = ui5.LineTcGiris.text()
    print("text :", Tc)
    sor = "SELECT COUNT(Appointment.Policlinic_id) FROM Patient INNER JOIN Appointment ON Patient.Patient_id_tc = Appointment.Patient_id_tc INNER JOIN Doctor ON Appointment.Doctor_id = doctor.Doctor_id INNER JOIN Policlinic ON Appointment.Policlinic_id = policlinic.Policlinic_id WHERE policlinic.Policlinic_id = ? AND Appointment.Date = ? ; "
    curs.execute(sor, (_BolumID, _Date1,))
    data = curs.fetchall()
    a = str(data)
    ui3.lineEdit.setText("{}".format(a.strip('[(,)]')))

    ui3.tableWidget.clear()
    ui3.tableWidget.setHorizontalHeaderLabels(
        ('Tc', 'Name', 'Surname', "Policlinic Name", "Doctor Name", "Doctor Surname", "Date", "Time"))
    ui3.tableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)  # Tablonun taşmasını önler (sıkıştırır.)
    sor2 = "SELECT Patient.Patient_id_tc,Patient.Name,Patient.Surname,Policlinic.Policlinic_name,doctor.Doctor_name,Doctor.Doctor_surname,Appointment.Date,Appointment.Time FROM Patient INNER JOIN Appointment ON Patient.Patient_id_tc = Appointment.Patient_id_tc INNER JOIN Doctor ON Appointment.Doctor_id = doctor.Doctor_id INNER JOIN Policlinic ON Appointment.Policlinic_id = policlinic.Policlinic_id WHERE Appointment.Patient_id_tc = ? ; "
    curs.execute(sor2, (Tc,))
    for satirIndex, satirVeri in enumerate(curs):  # 2 parametreyi enumerate tutar
        for sutunIndex, sutunVeri in enumerate(satirVeri):
            ui3.tableWidget.setItem(satirIndex, sutunIndex, QTableWidgetItem(str(sutunVeri)))

    ui3.tableWidget_2.clear()
    ui3.tableWidget_2.setHorizontalHeaderLabels(('Name', 'Surname'))
    ui3.tableWidget_2.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)  # Tablonun taşmasını önler (sıkıştırır.)
    sor3 = "SELECT Patient.Name,Patient.Surname FROM Patient INNER JOIN Appointment ON Patient.Patient_id_tc = Appointment.Patient_id_tc INNER JOIN Doctor ON Appointment.Doctor_id = doctor.Doctor_id INNER JOIN Policlinic ON Appointment.Policlinic_id = policlinic.Policlinic_id WHERE policlinic.Policlinic_id = ? AND Appointment.Date = ? ; "
    curs.execute(sor3, (_BolumID, _Date1,))
    for satirIndex, satirVeri in enumerate(curs):  # 2 parametreyi enumerate tutar
        for sutunIndex, sutunVeri in enumerate(satirVeri):
            ui3.tableWidget_2.setItem(satirIndex, sutunIndex, QTableWidgetItem(str(sutunVeri)))


# ---------------------------Hasta Sorgulama---------------------
def HastaSorgula():
    tc = ui5.LineTcGiris.text()
    ui.LineTc.setText("{}".format(ui5.LineTcGiris.text()))
    sor = "SELECT COUNT(Patient_id_tc) FROM Patient WHERE Patient_id_tc = ?"
    curs.execute(sor, (tc,))
    data = curs.fetchall()
    a = str(data)
    b = a.strip('[(,)]')
    print(b)
    if b == '0':
        print("kayıt Ol")
        HastaArama.close()
        KayıtPen.show()
    else:
        SecmePen.show()
        HastaArama.close()

# ---------------------------Sure Gösterimi---------------------
def showTime():
    minute = 0
    while True:
        if minute == 10:
            break
        else:
            pass
        minute = minute + 1
        time.sleep(1)
        QtCore.QCoreApplication.processEvents()
        ui.progressBar.setValue(minute)


def showTime2():
    minute = 0
    while True:
        if minute == 10:
            break
        else:
            pass
        minute = minute + 1
        time.sleep(1)
        QtCore.QCoreApplication.processEvents()
        ui5.progressBar.setValue(minute)

def showTime3():
    minute = 0
    while True:
        if minute == 10:
            break
        else:
            pass
        minute = minute + 1
        time.sleep(1)
        QtCore.QCoreApplication.processEvents()
        ui3.progressBar.setValue(minute)
        print(ui3.progressBar.text())
        if ui3.progressBar.text() == "100%":
            SıraPen.hide()
            WelcomeHomePage.show()
            break
    again()
# ---------------------------------------------------------------------------------------
def SesKayıtbaslama():
    deneme = threading.Thread(target=showTime2)
    deneme.start()
    a = "1"
    arayuz(a)
# --------------------------Sinyal - Slot (tıklanınca yapılacaklar)---------------------
def tc():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    a = "2"
    arayuz(a)

# ---------------------------------------------------------------------------------------
def name():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    a = "3"
    arayuz(a)

# ---------------------------------------------------------------------------------------
def surname():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    a = "4"
    arayuz(a)
# ---------------------------------------------------------------------------------------
def day():
    deneme = threading.Thread(target=showTime)
    deneme.start()
    arayuz2()
# ---------------------------------------------------------------------------------------
def acılıs():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('egitim/egitim.yml')
    face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
    ui6.cap = cv2.VideoCapture(0)
    timer = 0
    timer2 = 0
    id = 0
    while (True):
        ret, img = ui6.cap.read()
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        yuzler = face_detector.detectMultiScale(img, 1.1, 5, minSize=(100,100))
        for (x, y, w, h) in yuzler:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, uyum = recognizer.predict(gri[y:y + h, x:x + w])
            if (uyum < 80):
                sor = "SELECT Patient_id_tc FROM Patient WHERE rowid = ?"
                curs.execute(sor, (id,))
                data = curs.fetchall()
                c = str(data)
                b = c.strip("'[( ,)]")
                print(b)
                id = b
                n = b
                sor = "SELECT Name FROM Patient WHERE Patient_id_tc = ?"
                curs.execute(sor, (id,))
                data = curs.fetchall()
                dataname = str(data)
                name = dataname.strip("'[( ,)]")
                print(name)
                uyum = f"Uyum=  {round(uyum, 0)}%"
                print("uyum " + uyum + "\nid " + id)
                timer = timer + 1
                timer2 = 0
            else:
                id = "Unknown"
                name= "Register"
                n =""
                uyum = f"Uyum=  {round(uyum, 0)}%"
                print("uyum " + uyum + "\nid " + id)
                timer = 0
                timer2 = timer2 + 1
        cv2.putText(img, str(id), (x + 6, y - 6), cv2.FONT_HERSHEY_DUPLEX, .8, (0, 0, 255))
        cv2.putText(img, str(name), (x,y+h+20), cv2.FONT_HERSHEY_DUPLEX, .8, (0, 0, 255))
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
        ui6.label.setPixmap(QPixmap.fromImage(qImg))
        ui5.LineTcGiris.setText(n)
        a = len(yuzler)
        if cv2.waitKey(1) & timer == 100:
            Kamera.hide()
            HastaArama.show()
            break
        elif cv2.waitKey(1) & timer2 == 100:
            Kamera.hide()
            HastaArama.show()
            break

# ---------------------------------------------------------------------------------------
if Kamera.isActiveWindow() == True:
    acılıs()
# --------------------------------------------------------------------------------------------------------
def again():
    print("Hello Open again")
    ui4.pushButton.click()

def welcomeAcılma():
    _WelcomeRecord()
    ui.LineAd.setText("")
    ui.LineDay.setText("")
    ui.LineYear.setText("")
    ui.LineSoyad.setText("")
    ui.LineMounth.setText("")
    ui.label.clear()

if WelcomeHomePage.isActiveWindow() == True:
    print("Hello Open")
    ui4.pushButton.animateClick(100)

ui.BKayit.clicked.connect(Kayit)
ui.BKayit_2.clicked.connect(_kamera)
ui.pushButton.clicked.connect(day)
ui.pushButton_2.clicked.connect(tc)
ui.pushButton_3.clicked.connect(surname)
ui.pushButton_4.clicked.connect(name)
ui2.BtnKayit2.clicked.connect(Secim)
ui4.pushButton.clicked.connect(welcomeAcılma)
ui5.pushButton.clicked.connect(HastaSorgula)
ui5.pushButton_2.clicked.connect(SesKayıtbaslama)

sys.exit(Uygulama.exec_())
