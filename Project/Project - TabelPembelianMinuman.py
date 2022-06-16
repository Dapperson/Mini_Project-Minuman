jawab='y' or 'Y'
while(True):
    print("Pilih Jenis Minuman: \n1. TEH\n2. KOPI")
    jm=input("Pilih Kode (1/2): ")
    if jm=='1':
        kode=['1','2','3','4','5','6','7']
        print("Pilih Minuman: ")
        print("------------------------------------")
        print("| KODE |      NAMA       |  HARGA  |")
        print("------------------------------------")
        print("| 1    | TEH BOTOL SOSRO | Rp.3000 |")
        print("| 2    | ICHI OCHA       | Rp.3200 |")
        print("| 3    | TEH KOTAK       | Rp.3500 |")
        print("| 4    | FRESHTEA        | Rp.6200 |")
        print("| 5    | NU GREEN TEA    | Rp.5800 |")
        print("| 6    | TEH JAVANA      | Rp.2800 |")
        print("| 7    | TEH PUCUK       | Rp.3200 |")
        print("------------------------------------")
        pilih=input("\nPilih Kode: ")
        pajak=150
        pilih in kode
        if '1' in pilih:
            nama='TEH BOTOL SOSRO    '
            harga=3000
        elif '2' in pilih:
            nama='ICHI OCHA          '
            harga=3200
        elif '3' in pilih:
            nama='TEH KOTAK          '
            harga=3500
        elif '4' in pilih:
            nama='FRESHTEA           '
            harga=6200
        elif '5' in pilih:
            nama='NU GREEN TEA       '
            harga=5800
        elif '6' in pilih:
            nama='TEH JAVANA         '
            harga=2800
        elif '7' in pilih:
            nama='TEH PUCUK          '
            harga=3200
        else:
            print("Kode yang anda masukan salah")
    elif jm=='2':
        print("Pilih Minuman: ")
        print("---------------------------------------")
        print("| KODE |      NAMA          |  HARGA  |")
        print("---------------------------------------")
        print("| 1    | NESCAFE BLACK      | Rp.8000 |")
        print("| 2    | LUWAK WHITE KOFFIE | Rp.5800 |")
        print("| 3    | ABC EXO            | Rp.5600 |")
        print("| 4    | KOPIKO 78 C        | Rp.5200 |")
        print("| 5    | GOOD DAY CAPPUCCINO| Rp.6800 |")
        print("| 6    | GOLDA COFFE        | Rp.3200 |")
        print("---------------------------------------")
        pilih=input("Pilih kode: ")
        pajak=200
        if pilih=='1':
            nama='NESCAFE BLACK      '
            harga=8000
        elif pilih=='2':
            nama='LUWAK WHITE KOFFIE '
            harga=5800
        elif pilih=='3':
            nama='ABC EXO            '
            harga=5600
        elif pilih=='4':
            nama='KOPIKO 78 C        '
            harga=5200
        elif pilih=='5':
            nama='GOOD DAY CAPPUCCINO'
            harga=6800
        elif pilih=='6':
            nama='GOLDA COFFEE       '
            harga=3200
        else:
            print("Kode yang anda masukan salah")
    else:
        print("Kode yang anda masukan salah")
        jawab = input("\nIngin membeli lagi ? (Y/T): ")
        if jawab == 't' and 'T':
            print("\nTerimakasih telah berbelanja")
        break
    jumlah=int(input("Jumlah yang ingin dibeli: "))
    th=(jumlah*harga)+pajak
    print("=============================================================================")
    print("|Nama                   |  Jumlah  |  Pajak  |    Harga     |     Total     |")
    print("=============================================================================")
    print("|%s"%(nama),"\t|    %i    "%(jumlah),"| Rp.%i "%(pajak),"|\tRp.%i"%(harga),"\t|\tRp. %i\t|"%(th),)
    jawab = input("\nIngin membeli lagi ? (Y/T): ")
    if jawab=='t'and'T':
        print("\nTerimakasih telah berbelanja ^^")
        break