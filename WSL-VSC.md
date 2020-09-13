# Instalasi WSL serta Konfigurasi pada VSC
## Windows Only

### A. Instalasi WSL

1. Buka Microsoft Store lalu cari Ubuntu, pilih, lalu install, tunggu hihngga selesai
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/1.png" width="500" />
2. Buka Turn Windows features on or off, lalu centang pada pilihan Windows Subsytem for Linux
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/1b.png" width="300" />
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/2.png" width="300" />
3. Jalankan Terminal ubuntu yang sudah diinstall, berikan nama, dan password yang kalian inginkan
4. Lalu update terminal tersebut dengan cara `sudo apt update`


### B. Konfigurasi WSL pada VSC (Visual Studio Code)

1. Buka VSC lalu install Remote-WSL (extension VSC), instal dengan mencari extension langsung dari VSC
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/3.png" width="300" />
2. Buka Terminal baru dengan memilih pada menubar, Terminal->New Terminal, pada VSC
3. Klik dropdown pada pojok kanan terminal, Select Default Shell
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/4.png" width="500" />
4. Lalu pilih WSL Bash
<img src="https://github.com/dummytarget/Pawang-Ular/blob/master/img/5.png" width="500" />
5. Terminal WSL sudah bisa digunakan, open projek untuk melihat di direktori mana project tersebut berada
