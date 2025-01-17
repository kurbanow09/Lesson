ishgarler={"Mekan" : {"hunari" : "programist",
"bilimi" : "orta",
 "yashy" : 22},

"Oraz" : {"hunari" : "hasapchy",
"bilimli" : "yokary",
"yashy" : 30},
}

ady = input("Ady: ")
if ady in ishgarler:
    isleg=input("Doly maglumat:(howa/yok)")
    if isleg=="howa":
        print(ishgarler[ady])
    else:
        mag=input("hunari/bilimli/yashhy")
        print(ishgarler[ady][mag])
else:
    print(f"(ady) atly ishgar yok")