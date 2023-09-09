#pendeklarasian variable product menjadi array agar bisa di ini banyak value
product =[]




#fungsi untuk menampilkan data product
def show_datas():
    if len(product) <=0:
        print("belum ada product yang dimasukan")
    else:
        for indeks in range(len(product)):
            print("[%d] %s" % (indeks, product[indeks]))

#fungsi untuk menambahkan data
def insert_data():
    product_baru = input("judul product: ")
    product.append(product_baru)


#fungsi edit data product
def edit_data():
    show_datas()
    indeks = int(input("inputkan ID product: "))
    if(indeks>len(product)):
        print("ID salah")
    else:
        nama_product = input("nama baru: ")
        product[indeks] = nama_product

#fungsi menghapus data
def delete_data():
    show_datas()
    indeks = int(input("inputkan ID product"))
    if(indeks>len(product)):
        print("ID salah")
    else:
        product.remove(product[indeks])


#fungsi menampilkan menu

def show_menu():
    print ("\n")
    print ("<-----------MENU---------->")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if menu == "1":
        show_datas()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print("Pilihan anda salah atau tidak ada")


if __name__ == "__main__":

    while(True):
        show_menu()
