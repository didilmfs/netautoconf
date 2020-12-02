#from pymongo import MongoClient
import os
CORE = ['10.33.109.249','10.33.109.250']
DIST= ['10.33.109.251','10.33.109.252']
ACCESS= ['10.33.109.253','10.33.109.254']

#connection = MongoClient('mongodb://localhost:27017/')
#db = connection.database
# Membaca Data MongoDB.

# Memasukan value ip address ke variable IPADDR
IPADDR= '10.33.109.250'
# Memasukan value merk/vendor ke variable VENDOR
VENDOR= 'huawei'
# Filter nilai variable VENDOR pakai IF ELSE
if (VENDOR == 'cisco'):
        if (IPADDR in CORE):
                # Memasukan nilai variable IPADDR ke ansible inventory core cisco
                with open("CiscoInventoryCore", "r") as in_file:
                        buf = in_file.readlines()

                if(IPADDR in buf):
                        print("Device dengan ip address " + IPADDR + " sudah terkonfigurasi sebelumnya")
                else:
                        buf.insert(1, (IPADDR + '\n'))
                        with open("CiscoInventoryCore", "w") as out_file:
                                out_file.writelines(buf)
                        # Menjalankan command ansible-playbook untuk push config
                        os.system('ansible-playbook -i CiscoInventoryCore CiscoPushConfCore.yml')
                        # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                        config = os.system('ansible-playbook -i CiscoInventoryCore CiscoGetConfCore.yml')
                        #print(config)
                        # Mengirimkan nilai variable ke mongodb
                        #collection = db.kelompokg
                        #updateResult = collection.insert_many(config)

        elif(IPADDR in DIST):
                # Memasukan nilai variable IPADDR ke ansible inventory dist cisco
                with open("CiscoInventoryDist", "r") as in_file:
                        buf = in_file.readlines()
                if(IPADDR in buf):
                        print("Device dengan ip address " + IPADDR + " sudah terkonfigurasi sebelumnya")
                else:
                        buf.insert(1, (IPADDR + '\n'))
                        with open("CiscoInventoryDist", "w") as out_file:
                            out_file.writelines(buf)
                        # Menjalankan command ansible-playbook untuk push config
                        os.system('ansible-playbook -i CiscoInventoryDist CiscoPushConfDist.yml')
                        # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                        config = os.system('ansible-playbook -i CiscoInventoryDist CiscoGetConfDist.yml')
                        # Mengirimkan nilai variable ke mongodb
                        #collection = db.kelompokg
                        #updateResult = collection.insert_many(config)

        elif(IPADDR in ACCESS):
                # Memasukan nilai variable IPADDR ke ansible inventory acc cisco
                with open("CiscoInventoryAccess", "r") as in_file:
                      buf = in_file.readlines()
                if(IPADDR in buf):
                        print("Device dengan ip address " + IPADDR + " sudah terkonfigurasi sebelumnya")
                
                else:
                        buf.insert(1, (IPADDR + '\n'))
                        with open("CiscoInventoryAccess", "w") as out_file:
                              out_file.writelines(buf)
                        # Menjalankan command ansible-playbook untuk push config
                        os.system('ansible-playbook -i CiscoInventoryAccess CiscoPushConfAccess.yml')
                        # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                        config = os.system('ansible-playbook -i CiscoInventoryAccess CiscoGetConfAccess.yml')
                        # Mengirimkan nilai variable ke mongodb
                        #collection = db.kelompokg
                        #updateResult = collection.insert_many(config)
        else:
                print("ip address tidak ada dalam range")

elif (VENDOR == 'huawei'):
        if (IPADDR in CORE):
                # Memasukan nilai variable IPADDR ke ansible inventory core huawei
                with open("HuaweiInventoryCore", "r") as in_file:
                        buf = in_file.readlines()

                if((IPADDR+'\n') in buf):
                        continue
                else:
                        buf.insert(1, (IPADDR + '\n'))
                        
                with open("HuaweiInventoryCore", "w") as out_file:
                        out_file.writelines(buf)

                # Menjalankan command ansible-playbook untuk push config
                os.system('ansible-playbook -i HuaweiInventoryCore HuaweiPushConfCore.yml')
                # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                config = os.system('ansible-playbook -i HuaweiInventoryCore HuaweiGetConfCore.yml')
                with open("getconf.txt", "r") as getconf_file:
                        getconf = getconf_file.read()

                print(getconf)
                # Mengirimkan nilai variable ke mongodb
                #collection = db.kelompokg
                #updateResult = collection.insert_many(config)

        elif(IPADDR in DIST):
                # Memasukan nilai variable IPADDR ke ansible inventory dist huawei
                with open("HuaweiInventoryDist", "r") as in_file:
                        buf = in_file.readlines()
                
                if((IPADDR+'\n') in buf):
                        print("Device dengan ip address " + IPADDR + " sudah terkonfigurasi sebelumnya");
                else: 
                        buf.insert(1, (IPADDR + '\n'))
                        with open("HuaweiInventoryDist", "w") as out_file:
                              out_file.writelines(buf)
                        # Menjalankan command ansible-playbook untuk push config
                        os.system('ansible-playbook -i HuaweiInventoryDist HuaweiPushConfDist.yml')
                        # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                        config = os.system('ansible-playbook -i HuaweiInventoryDist HuaweiGetConfDist.yml')
                        with open("getconf.txt", "r") as getconf_file:
                                getconf = getconf_file.read()

                        print(getconf)
                        # Mengirimkan nilai variable ke mongodb
                        #collection = db.kelompokg
                        #updateResult = collection.insert_many(config)

        elif(IPADDR in ACCESS):
                # Memasukan nilai variable IPADDR ke ansible inventory acc huawei
                with open("HuaweiInventoryAccess", "r") as in_file:
                        buf = in_file.readlines()
                if((IPADDR+'\n') in buf):
                        print("Device dengan ip address " + IPADDR + " sudah terkonfigurasi sebelumnya");
                else:
                        buf.insert(1, (IPADDR + '\n'))
                        with open("HuaweiInventoryAccess", "w") as out_file:
                              out_file.writelines(buf)
                        # Menjalankan command ansible-playbook untuk push config
                        os.system('ansible-playbook -i HuaweiInventoryAccess HuaweiPushConfAccess.yml')
                        # Mendapatkan informasi konfigurasi device & Memasukan output ansible ke variable
                        config = os.system('ansible-playbook -i HuaweiInventoryAccess HuaweiGetConfAccess.yml')
                        with open("getconf.txt", "r") as getconf_file:
                                getconf = getconf_file.read()

                        print(getconf)
                        # Mengirimkan nilai variable ke mongodb
                        #collection = db.kelompokg
                        #updateResult = collection.insert_many(config)
        else:
                print("ip address tidak ada dalam range")
else:
        print("Vendor belum didukung")
