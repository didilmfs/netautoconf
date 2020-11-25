from pymongo import MongoClient
import os
CORE = [‘192.168.1.1’,’192.168.1.2’]
DIST= [‘192.168.1.11’,’192.168.1.12’]
ACCESS= [‘192.168.1.21’,’192.168.1.22’]

connection = MongoClient('mongodb://localhost:27017/')
db = connection.database
# Membaca Data MongoDB.

# Memasukan value ip address ke variable IPADDR

# Memasukan value merk/vendor ke variable VENDOR

# Filter nilai variable VENDOR pakai IF ELSE 
if (VENDOR == ‘cisco’):
	if (IPADDR in CORE):
		# Memasukan nilai variable IPADDR ke ansible inventory core cisco
		with open("CiscoInventoryCore", "r") as in_file:
    			buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("CiscoInventoryCore", "w") as out_file:
    			out_file.writelines(buf)

    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i CiscoInventoryCore CiscoPushConfCore.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i CiscoInventoryCore CiscoGetConfCore.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)

  else if(IPADDR in DIST):
    # Memasukan nilai variable IPADDR ke ansible inventory dist cisco
    with open("CiscoInventoryDist", "r") as in_file:
              buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("CiscoInventoryDist", "w") as out_file:
            out_file.writelines(buf)
    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i CiscoInventoryDist CiscoPushConfDist.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i CiscoInventoryDist CiscoGetConfDist.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)

  else if(IPADDR in ACCESS):
    # Memasukan nilai variable IPADDR ke ansible inventory acc cisco
    with open("CiscoInventoryAccess", "r") as in_file:
              buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("CiscoInventoryAccess", "w") as out_file:
              out_file.writelines(buf)
    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i CiscoInventoryAccess CiscoPushConfAccess.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i CiscoInventoryAccess CiscoGetConfAccess.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)
  else:
    print(“ip address tidak ada dalam range”)

else if (VENDOR == ‘huawei’):
	if (IPADDR in CORE):
		# Memasukan nilai variable IPADDR ke ansible inventory core huawei
		with open("HuaweiInventoryCore", "r") as in_file:
    			buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("HuaweiInventoryCore", "w") as out_file:
              out_file.writelines(buf)

    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i HuaweiInventoryCore HuaweiPushConfCore.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i HuaweiInventoryCore HuaweiGetConfCore.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)

  else if(IPADDR in DIST):
    # Memasukan nilai variable IPADDR ke ansible inventory dist huawei
    with open("HuaweiInventoryDist", "r") as in_file:
              buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("HuaweiInventoryDist", "w") as out_file:
              out_file.writelines(buf)
    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i HuaweiInventoryDist HuaweiPushConfDist.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i HuaweiInventoryDist HuaweiGetConfDist.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)

  else if(IPADDR in ACCESS):
    # Memasukan nilai variable IPADDR ke ansible inventory acc huawei
    with open("HuaweiInventoryAccess", "r") as in_file:
              buf = in_file.readlines()

    buf.insert(1, (IPADDR + '\n'))

    with open("HuaweiInventoryAccess", "w") as out_file:
              out_file.writelines(buf)
    # Menjalankan command ansible-playbook untuk push config
    os.system(‘ansible-playbook -i HuaweiInventoryAccess HuaweiPushConfAccess.yml’)
    # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
    config = os.system(‘ansible-playbook -i HuaweiInventoryAccess HuaweiGetConfAccess.yml’)
    # Mengirimkan nilai variable ke mongodb
    collection = db.kelompokg
    updateResult = collection.insert_many(config)
  else:
	  print(“ip address tidak ada dalam range”)
else:
	print(“Vendor belum didukung”)
