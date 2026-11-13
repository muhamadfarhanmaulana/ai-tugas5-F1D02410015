import json

def load_kb(filepath="kb_melon.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    kb = load_kb()
    print(f"=== {kb['judul']} ===")
    print("Jawab y/t.")
    
    fakta_list = []
    for r in kb["aturan"]:
        for syarat in r["jika"]:
            is_sub = any(syarat == sub["maka"] for sub in kb["aturan"])
            if not is_sub and syarat not in fakta_list:
                fakta_list.append(syarat)
                
    user_memori = {}
    fakta_awal = []
    
    for idx, fakta in enumerate(fakta_list, 1):
        jawaban = input(f"{idx}. {fakta}? (y/t) > ").strip().lower()
        if jawaban == 'y':
            user_memori[fakta] = True
            fakta_awal.append(fakta)
        else:
            user_memori[fakta] = False

    print("\nFakta awal:", ", ".join(fakta_awal) if fakta_awal else "tidak ada")
    print()

    # Mesin Inferensi / Evaluasi Aturan
    memori_kerja = list(fakta_awal)
    siklus = 1
    aturan_terpakai = []
    
    while True:
        aturan_baru_ditemukan = False
        for r in kb["aturan"]:
            if r["maka"] in memori_kerja:
                continue
                
            mode = r["mode"]
            syarat_terpenuhi = True
            
            for syarat in r["jika"]:
                if syarat not in memori_kerja:
                    syarat_terpenuhi = False
                    break
            
            if mode == "dan" and syarat_terpenuhi:
                memori_kerja.append(r["maka"])
                aturan_terpakai.append(r)
                print(f"Siklus {siklus}: {r['id']} -> {r['maka']}")
                siklus += 1
                aturan_baru_ditemukan = True
                break
            elif mode == "atau" and any(s in memori_kerja for s in r["jika"]):
                memori_kerja.append(r["maka"])
                aturan_terpakai.append(r)
                print(f"Siklus {siklus}: {r['id']} -> {r['maka']}")
                siklus += 1
                aturan_baru_ditemukan = True
                break
                
        if not aturan_baru_ditemukan:
            print(f"Siklus {siklus}: tidak ada aturan baru, berhenti")
            break

    if aturan_terpakai:
        kesimpulan_akhir = aturan_terpakai[-1]["maka"]
        print(f"\nKesimpulan: {kesimpulan_akhir}")
        print("Alasan:")
        
        def cetak_alasan(target, indent=2):
            for r in aturan_terpakai:
                if r["maka"] == target:
                    syarat_str = ", ".join(r["jika"])
                    print(f"{' ' * indent}{target}  <- {r['id']} ({syarat_str})")
                    for s in r["jika"]:
                        cetak_alasan(s, indent + 4)
                        
        cetak_alasan(kesimpulan_akhir)
    else:
        print("\nKesimpulan: tidak ada (kasus negatif)")

    print("\n--------------------------------------------------------------------------------")
    print("Catatan Batasan Keberlakuan:")
    print("Basis pengetahuan sistem pakar ini disusun berdasarkan literatur jurnal ilmiah")
    print("pertanian dari Bambang Yuwono dkk., Zulkifli Arief, serta Dodi Prasetio.")
    print("Sistem ini ditujukan untuk membantu identifikasi gejala umum, hama, dan kendala")
    print("fisiologis pada tanaman melon (Cucumis melo L.) dalam ranah edukasi dan pendukung")
    print("analisis akademik. Hasil diagnosis yang dihasilkan oleh program ini bersifat")
    print("sebagai saran pendukung keputusan awal dan bukan merupakan keputusan mutlak")
    print("pengganti diagnosis langsung dari ahli agronomi atau pakar pertanian profesional.")
    print("--------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()