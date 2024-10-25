from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman profil tim
@app.route('/')
def profile_team():
    # Data anggota tim untuk halaman profil
    team_members = [
        {
            "name": "Akbar Eka Putra Avrilian",
            "id": "22.83.0932",
            "description": "Integer rutrum ligula eu dignissim laoreet...",
            "skills": {
                "Coding": 70,
                "Jaringan": 40,
                "Basis Data": 60,
                "IoT": 80
            },
            "image": "saya.jpg"
        },
        {
            "name": "Rifky Dwi Prasetyo",
            "id": "22.83.0900",
            "description": "Integer rutrum ligula eu dignissim laoreet...",
            "skills": {
                "Coding": 80,
                "Jaringan": 70,
                "Basis Data": 50,
                "IoT": 90
            },
            "image": "rifky.jpg"
        },
        {
            "name": "Andreas Saputra Sianipar",
            "id": "22.83.0911",
            "description": "Integer rutrum ligula eu dignissim laoreet...",
            "skills": {
                "Coding": 90,
                "Jaringan": 90,
                "Basis Data": 90,
                "IoT": 90
            },
            "image": "andre.jpg"
        }
    ]
    return render_template('index.html', team_members=team_members)

if __name__ == "__main__":
    app.run(debug=True)

