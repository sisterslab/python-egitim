import random

#Katılımcı listesi içerisinden random bir değer ile o indexteki arkadaşı ekrana getir
participant = ["Ceren", "Selin", "Elif Naz", "İlkay", "Nurdan", "Ayça", "Ayşe Beril", "Begüm", "Bilge", "Nurcan", "Burcu", "Elvan", "idil", "Sevda", "Nurefşan", "Işınsu", "Ayşe Aktağ", "Elif Çelik", "Aylin", "Buket", "Ceydanur", "Fadime", "Sema", "İlayda", "Yağmur"]

value = random.randint(0, len(participant) - 1)

print("Bir sonraki talihlimiz: ", participant[value])