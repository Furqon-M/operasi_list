data_angka = [1,5,1,4,3,2,4,3,2,3,2,3,7,8,9,0]

print(f"data angka = \n{data_angka}")

# count data (menghitung data ini muncul berapa kali dalam si data angka)

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah data 4 = {jumlah_data_4}")

print(f"Jumlah data 3 = {jumlah_data_3}")

# ambil posisi data

data = ["kelana","angan","raka","dira"]

print(f"data = \n{data}")

index_angan = data.index("angan")

print(f"index angan = {index_angan}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = \n{data}")
data.sort()
print(f"data = \n{data}")

# balik listnya

data_angka.reverse()
data.reverse()
print(f"data angka = \n{data_angka} \n{data}")