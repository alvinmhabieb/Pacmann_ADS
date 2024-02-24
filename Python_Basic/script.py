#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Transaction:
    def __init__(self):
        """
        fungsi inisiasi dictionary
        """
        self.data_item = dict()
        self.daftar_belanja = dict()

    def add_item(self, item, jumlah, harga):
        """
        fungsi menambahkan item belanja dan menghitung total belanja
        item   : nama item yang akan ditambahkan (str)
        jumlah : jumlah item yang akan ditambahkan (int)
        harga  : harga item yang akan ditambahkan (int)
        """
        self.data_item.update({item: [jumlah, harga]})
        return f'Item yang dibeli adalah: {self.data_item}'

    def update_item_name(self, item, item_baru):
        """
        fungsi untuk memperbaharui item
        item        : item yang ingin diganti (str)
        item_baru   : item pengganti (str)
        """
        temp = self.data_item[item]
        self.data_item.pop(item)
        self.data_item.update({item_baru: temp})
        return f'Item yang dibeli adalah {self.data_item}'
    
    def update_item_qty(self, item, jumlah_baru):
        """
        fungsi untuk memperbaharui jumlah item dan total belanja 
        item        : item yang ingin diubah jumlahnya (str)
        jumlah_baru : jumlah baru dari item (int)
        """
        self.data_item[item][0] = jumlah_baru
        return f'Item yang dibeli adalah: {self.data_item}'

    def update_item_price(self, item, harga_baru):
        """
        fungsi untuk memperbaharui harga item dan total belanja
        item        : item yang ingin diubah harganya (str)
        harga_baru  : harga baru dari item (int)
        """
        self.data_item[item][1] = harga_baru
        return f'Item yang dibeli adalah: {self.data_item}'
    
    def index_item(self, item):
        """
        fungsi mengembalikan nilai index dari baris yang mengandung value 'item'
        item    : item yang mau dicari (str)
        return
        i       : index dari baris yang mengandung item
        """
        for i in range(len(self.data_item)):
            if item == self.data_item[i][0]:
                return i
    
    def delete_item(self, item):
        """
        fungsi untuk menghapus item
        item   : item yang ingin dihapus (str)
        """
        self.data_item.pop(item)
        return f'Item yang dibeli adalah: {self.data_item}'
    
    def reset_transaction(self):
        """
        fungsi untuk menghapus seluruh rekaman transaksi
        output: keterangan tidak ada item yang dibeli
        """
        self.data_item.clear()
        return f'Semua item berhasil didelete!'

    def check_order(self):
        """
        fungsi untuk melihat pesanan dan mengecek pesanan apa ada yang bernilai nol
        output : print data item yang dipesan
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 0:
                data = pd.DataFrame(self.data_item).T
                data.columns = ['jumlah', 'harga']
                print(data.to_markdown())
                print('Pemesanan sudah benar')
            else:
                print('Terdapat kesalahan input data')
        except:
            print('Harap untuk mengulang kembali transaksi')
    
    def total_price(self):
        """
        fungsi mengecek total belanja dan menghitung diskon
        output: keterangan persentase diskon dan total belanja
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 200_000:
                total_belanja = total_belanja - (0.05*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 5%, total belanja anda: {total_belanja}'
            elif total_belanja > 300_000:
                total_belanja = total_belanja - (0.08*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 8%, total belanja anda: {total_belanja}'
            elif total_belanja > 500_000:
                total_belanja = total_belanja - (0.1*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 10%, total belanja anda: {total_belanja}'
            elif total_belanja <= 200_000:
                return f'Item yang dibeli adalah: {self.data_item}. Anda tidak mendapat diskon, total belanja anda: {total_belanja}'
        except:
            print('Harap periksa kembali daftar belanja Anda')

