#bienvenidos al Buffet
#de principio tenemos menu
print("Bienvenidos al Buffet Comemos Felices.com")
ac=input("Desea ver nuestros acompañamientos, 1 para si, 2 para no:")
if(ac=="1"):
    print("1.1:arroz")
    print("1.2:papa")
    print("1.3:yuca")
    a1=input("elige tu acompañamiento:")
if(ac=="2"):
    a1=("0")
ab=input("Elige el principio, 1 para si,2 para no:")
if(ab=="1"):
    print("2.1:pasta")
    print("2.2:arverja")
    print("2.3:ensalda fría")
    a2=input("elige tu principio:")
if(ab=="2"):
    a2=("0")
ap=input("Elige la proteína, 1 para si,2 para no:")
if(ap=="1"):
    print("3.1:Pollo al curry")
    print("3.2:Carne de res")
    print("3.3:Alistas BBQ")
    a3=input("elige tu proteína:")
if(ap=="2"):
    a3=("0")
if(a1=="1.1" and a2=="2.1" and a3=="3.1"):
    print("Aqui esta su almuerzo: Arroz, pasta y pollo al curry.")
if(a1=="1.1" and a2=="2.1" and a3=="3.1"):
    print("Arroz  Pasta  Pollo al curry.")

if(a1=="1.1" and a2=="2.1" and a3=="3.2"):
    print("Arroz  Pasta  Carne de res.")

if(a1=="1.1" and a2=="2.1" and a3=="3.3"):
    print("Arroz  Pasta  Alitas BBQ.")

if(a1=="1.1" and a2=="2.2" and a3=="3.1"):
    print("Arroz  Arveja  Pollo al curry.")

if(a1=="1.1" and a2=="2.2" and a3=="3.2"):
    print("Arroz  Arveja  Carne de res.")

if(a1=="1.1" and a2=="2.2" and a3=="3.3"):
    print("Arroz  Arveja  Alitas BBQ.")

if(a1=="1.1" and a2=="2.3" and a3=="3.1"):
    print("Arroz  Ensalada fría  Pollo al curry.")

if(a1=="1.1" and a2=="2.3" and a3=="3.2"):
    print("Arroz  Ensalada fría  Carne de res.")

if(a1=="1.1" and a2=="2.3" and a3=="3.3"):
    print("Arroz  Ensalada fría  Alitas BBQ.")

if(a1=="1.2" and a2=="2.1" and a3=="3.1"):
    print("Papa  Pasta  Pollo al curry.")

if(a1=="1.2" and a2=="2.1" and a3=="3.2"):
    print("Papa  Pasta  Carne de res.")

if(a1=="1.2" and a2=="2.1" and a3=="3.3"):
    print("Papa  Pasta  Alitas BBQ.")

if(a1=="1.2" and a2=="2.2" and a3=="3.1"):
    print("Papa  Arveja  Pollo al curry.")

if(a1=="1.2" and a2=="2.2" and a3=="3.2"):
    print("Papa  Arveja  Carne de res.")

if(a1=="1.2" and a2=="2.2" and a3=="3.3"):
    print("Papa  Arveja  Alitas BBQ.")

if(a1=="1.2" and a2=="2.3" and a3=="3.1"):
    print("Papa  Ensalada fría  Pollo al curry.")

if(a1=="1.2" and a2=="2.3" and a3=="3.2"):
    print("Papa  Ensalada fría  Carne de res.")

if(a1=="1.2" and a2=="2.3" and a3=="3.3"):
    print("Papa  Ensalada fría  Alitas BBQ.")

if(a1=="1.3" and a2=="2.1" and a3=="3.1"):
    print("Yuca  Pasta  Pollo al curry.")

if(a1=="1.3" and a2=="2.1" and a3=="3.2"):
    print("Yuca  Pasta  Carne de res.")

if(a1=="1.3" and a2=="2.1" and a3=="3.3"):
    print("Yuca  Pasta  Alitas BBQ.")

if(a1=="1.3" and a2=="2.2" and a3=="3.1"):
    print("Yuca  Arveja  Pollo al curry.")

if(a1=="1.3" and a2=="2.2" and a3=="3.2"):
    print("Yuca  Arveja  Carne de res.")

if(a1=="1.3" and a2=="2.2" and a3=="3.3"):
    print("Yuca  Arveja  Alitas BBQ.")

if(a1=="1.3" and a2=="2.3" and a3=="3.1"):
    print("Yuca  Ensalada fría  Pollo al curry.")

if(a1=="1.3" and a2=="2.3" and a3=="3.2"):
    print("Yuca  Ensalada fría  Carne de res.")

if(a1=="1.3" and a2=="2.3" and a3=="3.3"):
    print("Yuca  Ensalada fría  Alitas BBQ.")

print("Gracias por preferirnos, vuelva pronto")