# TUGAS 2

## Bagan Request Client ke Web

![Bagan Django](https://user-images.githubusercontent.com/113079090/221418715-3aa8565f-b71f-454a-80ef-5ae1b23e9145.png)

1. Client akan melakukan request terhadap URL.
2. URL akan memilih View.
3. View akan melakukan QuerySet terhadap Model.
4. Model akan melakukan transaksi data dengan Database.
5. Model akan merespon data sesuai dengan data yang ada pada Database.
6. View akan memilih template HTML yang berada pada directory Template.
7. Template akan menampilkan halaman HTML di Web.

## Penggunaan Virtual Environment

Virtual Environment akan memastikan bahwa versi dari sebuah library pada suatu project tidak akan berubah apabila kita melakukan update pada library yang sama di project lainnya. Jika Virtual Environment tidak digunakan, library perlu didowngrade untuk mengerjakan project lainnya (dan perlu diupgrade saat mengerjakan project yang lain)

## Instruksi Penggunaan

1. Membuat App Study Tracker dengan python manage.py startapp study_tracker.
2. Menambahkan app study_tracker pada INSTALLED_APPS di settings, register App di apps dan URL settings.
![image](https://user-images.githubusercontent.com/113079090/221419850-70722ca8-9213-406b-94cf-5d3e9c2f1b94.png)
![image](https://user-images.githubusercontent.com/113079090/221419878-008187ab-cb79-49aa-ba60-5aa66922d9d6.png)
![image](https://user-images.githubusercontent.com/113079090/221419700-37ca0180-99dc-47de-911e-c9e91ad8557c.png)
![image](https://user-images.githubusercontent.com/113079090/221419724-e5666fc5-5508-4dc8-a286-8d897d1aacc7.png)

3. Membuat class Assignment pada models.py di study_tracker. Register models pada admin.py.
![image](https://user-images.githubusercontent.com/113079090/221419756-a1a99fe2-ace0-4269-808c-6c6acb6e6a2c.png)
![image](https://user-images.githubusercontent.com/113079090/221419896-f46dfa39-2bbf-4b00-a1a2-bc8fd13ed299.png)

4. Mengambil data pada object Assignment melalui views.py
![image](https://user-images.githubusercontent.com/113079090/221420001-ede8cec1-628e-4af5-9479-261abf05017d.png)

Source:
Kelas Terbuka. (2018). Tutorial Django 1.11 Bahasa Indonesia. Retrieved from https://youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld

# TUGAS 3

## Menginput menggunakan form

Kita dapat menginput data selain menggunakan form, yaitu dengan berbagai pilihan lain, seperti charfield dll. Tetapi menginput menggunakan form akan lebih memudahkan pengambilan data untuk dimasukan ke dalam database

## HTML VS JSON VS XML

HTML berbeda dengan JSON dan XML. HTML berfokus untuk menampilkan data dan teks sedangkan JSON dan XML berfokus pada pertukaran data. HTML bersifat statis sedangkan XML bersifat dinamis.
JSON dan XML sendiri memiliki perbedaan yang menonjol pada kodenya. JSON dianggap lebih praktis untuk digunakan saat melakukan pemrograman sedangkan XML dianggap lebih mudah dimengerti karena tag yang diberikan lebih jelas.

## Data Delivery

Data delivery adalah proses transfer data antara server dengan database. Data delivery diperlukan dalam suatu platform agar server dapat menyimpan dan menampilkan data yang dibutuhkan oleh client.

## Penjelasan pembuatan program

1. Membuat forms.py

Buat forms.py pada directory study_tracker dengan fields name, subject, date, progress, dan deskripsi.
![image](https://user-images.githubusercontent.com/113079090/222966278-4cf74354-2e7d-48c9-9ef4-af8a5594118e.png)

2. Membuat fungsi pada views untuk menambahkan data tugas pada form.

Membuat fungsi bernama create_assignment sebagai fungsi untuk menambahkan tugas.
![image](https://user-images.githubusercontent.com/113079090/222966356-f113123b-9d7e-46fa-9d22-6189e05f6289.png)

3. Membuat file HTML baru yang menampilkan form untuk menambahkan data tugas baru.

Membuat file HTML dengan nama create_assignment.html untuk menampilkan form untuk penambahan tugas
![image](https://user-images.githubusercontent.com/113079090/222966447-37b873af-b55f-44b6-879c-48278f9f17cb.png)

4. Modifikasi file HTML yang menampilkan tabel tugas dengan menambahkan button untuk menuju ke halaman form.

Membuat button Tugas Baru dalam file create.html
![image](https://user-images.githubusercontent.com/113079090/222966540-7e20b1da-ea88-4a75-9577-3e1689e3b5cd.png)

5. Menyajikan data dalam bentuk JSON dan XML

Membuat fungsi dalam views untuk menampilkan data dalam bentuk XML dan JSON
![image](https://user-images.githubusercontent.com/113079090/222966620-0f44acb2-5080-439c-bc4a-c4329b16c8a4.png)

source:
tutorial pbp
https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb
https://byjus.com/free-ias-prep/difference-between-xml-and-html/
https://docs.oracle.com/en/cloud/saas/data-cloud/data-cloud-help-center/IntegratingBlueKaiPlatform/data_delivery.html

# TUGAS 4

## Kegunaan CSRF Token
CSRF Token berfungsi sebagai security yang menjaga terambilnya data. Token yang digenerate pada setiap kali merefresh akan mengubah input dengan melakukan hashing. Apabila tidak menggunakan CSRF Token, kita tidak dapat menggunakan method Post dan akan tertulis fobidden pada server.

## Membuat Form secara manual
Pembuatan form secara manual dapat dilakukan dengan menggunakan method form yang terdapat dalam HTML.
contoh penggunaan:
<form method='post'>
    {% csrf_token %}
    <label for="message">Message: </label>
    <input type="text" name="mess" id="message">
    <button type="Submit">Kirim</button>
</form>
                         
## Alur proses pengisian form
1. Browser menggenerate HTTP Request menuju url
2. Server menerima HTTP Request dan menggenerate HTML page FORM
3. Menampilkan HTML pada browser
4. Server menggenerate HTTP Request, methtod, dan argumen menuju UTL Destination berdasarkan on HTML Page FORM
5. User melakukan pengisian form
6. Server Menerima HTTP Request
7. Server enggenerate HTML Page
8. Menampilkan HTML Page pada browser

Saat user melakukan pengisian form, views akan menerima data dan menyampaikannya ke models. Kemudian models akan mengolah data dan menyimpannya pada database. Models bertugas melakukan transaksi data terhadap database. Kemudian models akan menyampaikan data yang diperlukan ke views, lalu views melakukan merge terhadap template.

## Pengimplementasian
1. Membuat form registrasi
Membuat fungsi register pada views.py
![image](https://user-images.githubusercontent.com/113079090/224529058-0ba3a85a-5062-467b-a6a3-7ef4c8941d3d.png)
Membuat html register pada templates
![image](https://user-images.githubusercontent.com/113079090/224529024-afefee9f-5976-4ded-a3f7-412047299131.png)

2. Membuat form login
Membuat fungsi login pada views.py
![image](https://user-images.githubusercontent.com/113079090/224529096-68311d00-0111-4e05-8c8a-9dbe6203a52e.png)
Membuat html login pada templates
![image](https://user-images.githubusercontent.com/113079090/224529160-c1bef310-2b7f-46c2-823f-dd2cacc9bd58.png)

3. Membuat fungsi logout
Membuat fungsi logout pada views
![image](https://user-images.githubusercontent.com/113079090/224529204-ddf2c275-3658-4fcd-9d57-29c1ed233bce.png)

5. Melakukan restriksi akses hanya pada pengguna yang sudah login
![image](https://user-images.githubusercontent.com/113079090/224529248-7336e80a-bf22-4dd6-abb9-a8877b1d13c2.png)

Source:
Kelas Terbuka. (2018). Tutorial Django 1.11 Bahasa Indonesia. Retrieved from https://youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld
2023 PBP Fasilkom UI. (2023). Tutorial 3. Retrieved from https://pbp-fasilkom-ui.github.io/genap-2023/tutorial/tutorial-3/
