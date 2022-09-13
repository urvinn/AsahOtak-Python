import os
import requests
res = requests.get('https://zekais-api.herokuapp.com/asahotak?apikey=MNVjaY58')
data = res.json() 
status = f"{data['status']}"
soal = f"{data['question']}"
jawaban = f"{data['answer']}"
if status == "200":
    os.system("cls||clear")
    print(f"""\nPERTANYAAN !\n{soal}\n""")
    print("Silahkan Jawab, Percobaan 1/5")
    jawab1 = input("Jawab : ")
    if jawaban == jawab1:
        os.system("cls||clear")
        print(f"""
   [  BERHASIL MENJAWAB ]

Jawaban = {jawaban}

     [ PERCOBAAN KAMU ]

Jawaban ke - 1 : {jawab1}

     [ GAME ASAH OTAK ]

""")
    else:
        print("\nJawaban Salah, Percobaan 2/5")
        jawab2 = input("Jawab : ")
        if jawaban == jawab2:
            os.system("cls||clear")
            print(f"""
   [  BERHASIL MENJAWAB ]

Jawaban = {jawaban}

     [ PERCOBAAN KAMU ]

Jawaban ke - 1 : {jawab1}
Jawaban ke - 2 : {jawab2}

     [ GAME ASAH OTAK ]

""")
        else:
            print("\nJawaban Salah, Percobaan 3/5")
            jawab3 = input("Jawab : ")
            if jawaban == jawab3:
                os.system("cls||clear")
                print(f"""
   [  BERHASIL MENJAWAB ]

Jawaban = {jawaban}

     [ PERCOBAAN KAMU ]

Jawaban ke - 1 : {jawab1}
Jawaban ke - 2 : {jawab2}
Jawaban ke - 3 : {jawab3}

     [ GAME ASAH OTAK ]

""")
            else:
                print("\nJawaban Salah, Percobaan 4/5")
                jawab4 = input("Jawab : ")
                if jawaban == jawab4:
                    os.system("cls||clear")
                    print(f"""
   [  BERHASIL MENJAWAB ]

Jawaban = {jawaban}

     [ PERCOBAAN KAMU ]

Jawaban ke - 1 : {jawab1}
Jawaban ke - 2 : {jawab2}
Jawaban ke - 3 : {jawab3}
Jawaban ke - 4 : {jawab4}

     [ GAME ASAH OTAK ]

""")
                else:
                    print("\nJawaban Salah, Percobaan 5/5")
                    jawab5 = input("Jawab : ")
                    if jawaban == jawab5:
                        os.system("cls||clear")
                        print(f"""
   [  BERHASIL MENJAWAB ]

Jawaban = {jawaban}

     [ PERCOBAAN KAMU ]

Jawaban ke - 1 : {jawab1}
Jawaban ke - 2 : {jawab2}
Jawaban ke - 3 : {jawab3}
Jawaban ke - 4 : {jawab4}
Jawaban ke - 5 : {jawab5}

     [ GAME ASAH OTAK ]

""")
                    else:
                        os.system("cls||clear")
                        print(f"""
     [  GAGAL MENJAWAB ]

Jawaban Yg Benar = {jawaban}

      [ JAWABAN KAMU ]

Jawaban ke - 1 : {jawab1}
Jawaban ke - 2 : {jawab2}
Jawaban ke - 3 : {jawab3}
Jawaban ke - 4 : {jawab4}
Jawaban ke - 5 : {jawab5}

     [ GAME ASAH OTAK ]

""")
