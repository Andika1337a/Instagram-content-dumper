import instaloader

# Inisialisasi Instaloader
L = instaloader.Instaloader()

# Login ke Instagram (opsional, diperlukan untuk mengakses konten privat)
# Ganti 'username' dan 'password' dengan akun Instagram Anda
USERNAME = 'username'
PASSWORD = 'password'
L.login(USERNAME, PASSWORD)

# Ambil profil pengguna
target_profile = input("Masukkan username Instagram: ")
profile = instaloader.Profile.from_username(L.context, target_profile)

# Ambil dan download postingan terbaru
print(f"Mengambil postingan dari {profile.username}...")
for post in profile.get_posts():
    print(f"Downloading post: {post.url}")
    L.download_post(post, target=profile.username)
    # Anda bisa membatasi jumlah postingan yang diunduh dengan menambahkan break
    break  # Hanya mengunduh 1 postingan sebagai contoh

# Ambil dan download story (opsional)
print(f"Mengambil story dari {profile.username}...")
for story in L.get_stories([profile.userid]):
    for item in story.get_items():
        print(f"Downloading story: {item.url}")
        L.download_storyitem(item, target=f"{profile.username}_stories")
        # Anda bisa membatasi jumlah story yang diunduh dengan menambahkan break
        break  # Hanya mengunduh 1 story sebagai contoh

print("Proses selesai.")
