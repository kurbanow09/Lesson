import string

def harp_bilen_baslayan_sozler(faýl_ad, harp):
    try:
        with open(faýl_ad, 'r', encoding='utf-8') as fayl:
            mazmun = fayl.read().lower() 
            sozler = mazmun.split()  

        temiz_sozler = [soz.strip(string.punctuation) for soz in sozler]

        netije = [soz for soz in temiz_sozler if soz and soz[0] == harp.lower()]

        print(f"\nBir sany harp girizildi: {harp}")
        if netije:
            for soz in set(netije): 
                print(soz)
        else:
            print("Şol harp bilen başlanýan söz tapylmady.")

    except FileNotFoundError:
        print("Faýl tapylmady.")

harp = input("Bir sany harp giriziň: ").strip().lower()

if len(harp) != 1 or not harp.isalpha():
    print("Diňe bir harp giriziň!")
else:
    faýl_ad = "Book.txt" 

    harp_bilen_baslayan_sozler(faýl_ad, harp)