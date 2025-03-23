from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Güvenlik amacıyla bir secret key ekleyin

# SQL Server bağlantısı
server = 'DESKTOP-EMQQEDE'
database = 'E_Ticaret'

# Veritabanı bağlantısını oluşturma
def get_siparisler(kullanici_id):
    try:
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("SELECT siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi FROM Siparisler WHERE kullanici_id = ?", (kullanici_id,))
        siparisler = cursor.fetchall()
        conn.close()
        return siparisler
    except pyodbc.Error as e:
        print(f"SQL Server bağlantısı başarısız oldu: {e}")
        return []

# Giriş Yapma
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kullanici_adi = request.form['kullanici_adi']
        sifre = request.form['sifre']

        try:
            conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
            cursor = conn.cursor()
            cursor.execute("SELECT kullanici_id, kullanici_adi, sifre FROM Kullanici WHERE kullanici_adi = ? AND sifre = ?", (kullanici_adi, sifre))
            user = cursor.fetchone()
            conn.close()

            if user:
                session['kullanici_id'] = user[0]  # Kullanıcı ID'sini session'a kaydediyoruz
                session['kullanici_adi'] = user[1]  # Kullanıcı adı session'a kaydediyoruz
                return redirect(url_for('dashboard'))
            else:
                return 'Giriş başarısız. Kullanıcı adı veya şifre hatalı.'
        except pyodbc.Error as e:
            return f"Veritabanı hatası: {e}"

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'kullanici_id' not in session:
        return redirect(url_for('login'))  # Kullanıcı girişi yapılmamışsa login sayfasına yönlendir

    kullanici_id = session['kullanici_id']
    kullanici_adi = session['kullanici_adi']
    siparisler = get_siparisler(kullanici_id)
    
    return render_template('dashboard.html', kullanici_adi=kullanici_adi, siparisler=siparisler)

# Ana Sayfa
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
