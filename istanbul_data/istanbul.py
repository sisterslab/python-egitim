import regex

'''
+Dosya okuma
+Tüm harfler küçük olacak
+Noktalama işaretleri kaldırılacak
Bir satırdaki text sadece sayıdan oluşuyorsa o satır yeni dosyaya eklenmeyecek
+Son olarak satır bazlı unique olacak. Mesela ilk satırda; Bugün neden gelmedin? yazıyor 5. satırda da aynı cümle birebir yazıyorsa bu eklenmeyecek
+ş ğ ü ö ç ı harfleri s g u o c i ile replace edilecek
'''

def remove_punc(text):
    remove = regex.compile(r'[\p{C}|\p{M}|\p{P}|\p{S}|\p{Z}]+', regex.UNICODE)
    return remove.sub(u" ", text).strip()

def text_preprocessing(line):
    pre_text = line.lower()
    pre_text = pre_text.replace("ş", "s").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ç", "c").replace("ı", "i")

    pre_text = remove_punc(pre_text)
    return pre_text

file = open(r".\istanbul_data\istanbul_data.txt", "r", encoding="utf-8")
lines = file.readlines()

unique_text = set()

for line in lines:
    text = text_preprocessing(line)
    if not text.isdigit():
        unique_text.add(text)

with open(r".\istanbul_data\islenmis_istanbul_data.txt", "w", encoding="utf-8") as f:
    for i in unique_text:
        f.write(i + "\n")