# Maglumatlar
baha_tl = 365.99  # Harydyň bahasy (TL bilen)
manat_kursy = 1.18  # TL-den manada geçiş kursy
agram_kg = 0.7  # Harydyň agramy (KG)
kargo_kg_baha = 25  # Kargo bahasy (manat/KG)

# Hasaplama we geçiriş
baha_manat = baha_tl * manat_kursy  # TL-den manada geçýär
kargo_bahasy = agram_kg * kargo_kg_baha  # Kargo bahasy
jemi_borc = baha_manat + kargo_bahasy  # Jemi çykdajy

# Netijeleri görkezýäris
print("Bahasy (Manat): {:.2f}".format(baha_manat))
print("Kargo Bahasy: {:.2f}".format(kargo_bahasy))
print("-" * 16)
print("Jemi Borç: {:.2f} manat".format(jemi_borc))
