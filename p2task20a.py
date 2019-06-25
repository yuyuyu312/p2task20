"""kg = google-kyrgyzstan
ru = google-russia
kz = google-kazakhstan
uz = google-uzbekistan
us = google-us
"""
country_list = ['google-kyrgyzstan', 'google-russia', 'google-kazakhstan', 'google-uzbekistan', 'google-us']
a = input("Поприветсвуйте")
if a == "привет":
    print(country_list)
    b = int(input("choice your country"))
    if 0 < b < 6:
        b -= 1
        print('you choose' + ' ' + country_list[b])
    else: print("not defined")
#    str = input("Книга жалоб")
    jaloba = open("book_of_complaints.txt", 'a')
    jaloba.write(input())
    jaloba.close()
