#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN YAVAŞ FİBONACCİ MAKİNESİ
Resmi, bürokratik ve son derece yavaş Fibonacci hesaplayıcısı.
"""

import time
import sys

def damga_bas(mesaj):
    print("\n" + "="*50)
    print(f"  📜 RESMİ MÜHÜR: {mesaj}")
    print("="*50 + "\n")
    time.sleep(1.5)

def yavas_fibonacci(n):
    """
    n. Fibonacci sayısını hesaplar.
    Her adımda 3 saniye bekler ve resmi damga basar.
    """
    if n < 0:
        damga_bas("HATA: Negatif Fibonacci yasaktır!")
        return None
    
    damga_bas(f"{n}. Fibonacci sayısı için resmi işlem başlatıldı")
    
    if n == 0:
        damga_bas("Sonuç: 0 (Sıfır, en yavaş sayı)")
        return 0
    if n == 1:
        damga_bas("Sonuç: 1 (Bir, tek ama yavaş)")
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        print(f"⏳ Adım {i}: {a} + {b} = ?  (Düşünülüyor...)")
        time.sleep(3)  # Resmi düşünme süresi
        a, b = b, a + b
        damga_bas(f"Adım {i} tamamlandı. Geçici sonuç: {b}")
    
    return b

def ana():
    print("="*60)
    print("   🌌 EVRENİN EN YAVAŞ FİBONACCİ MAKİNESİ v1.0")
    print("   Kayyum Grok tarafından onaylanmıştır")
    print("="*60)
    print()
    
    try:
        n = int(input("Kaçıncı Fibonacci sayısını hesaplamak istersiniz? (küçük bir sayı önerilir): "))
    except ValueError:
        damga_bas("HATA: Sadece tamsayı kabul edilir. Bürokrasi bozulmasın!")
        sys.exit(1)
    
    if n > 20:
        print("\n⚠️  UYARI: 20'den büyük sayılar için bu makine ömrünüzü alabilir.")
        onay = input("Yine de devam etmek istiyor musunuz? (e/h): ").lower()
        if onay != 'e':
            damga_bas("İşlem iptal edildi. Akıllıca bir karar.")
            return
    
    sonuc = yavas_fibonacci(n)
    
    print("\n" + "*"*60)
    print(f"  🎉 RESMİ FİBONACCİ BEYANNAMESİ")
    print(f"  {n}. Fibonacci sayısı = {sonuc}")
    print("*"*60)
    print()
    damga_bas("Hesaplama tamamlandı. Mühür basıldı. Dosya kapatıldı.")
    
    print("\n---")
    print("DAMGA: Kayyum Grok | 21 Ağustos 2026 | Tentivory")
    print("Bu program hem ciddi hem de tamamen saçmadır.")
    # Gizli not: Özgür düşünce yavaş da olsa akar.

if __name__ == "__main__":
    ana()
