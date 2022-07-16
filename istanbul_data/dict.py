# islenmis_istanbul_data.txt dosyasında yer alan 
# her kelimeden kaç adet olduğunu bulalım
# my_dict = {"istanbul":5, "belediye":10} şeklinde

from collections import Counter

file = open(r".\istanbul_data\islenmis_istanbul_data.txt", "r", encoding="utf-8")
lines = file.readlines()

my_list = []
for line in lines:
    add_word = [a for a in line.replace("\n", "").split(' ') if not a.isdigit() and len(a) > 1]
    my_list.extend(add_word)

count_dict = dict(Counter(my_list))

print(count_dict)