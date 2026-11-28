# Qoldiq (ishchi nom): MVP-layt

Telegram Mini App ko'rinishidagi veb-ilova: restoran va to'yxonalar saralangan oshxona chiqindisini e'lon qiladi, lichinka fermalari xaritada yaqin manbalarni ko'rib, olib ketishni belgilaydi va qabul qilganda sifatni baholaydi.

## Ishga tushirish (lokal)
```bash
python3 -m http.server 8765 --directory mvp
# brauzerda: http://localhost:8765
```
Bitta fayl: `index.html`. Xarita: Leaflet + OpenStreetMap. Telegram ichida ochilsa, `telegram-web-app.js` orqali ishlaydi; oddiy brauzerda ham ochiladi (ro'yxatdan o'tish kerak emas).

## Nima ishlaydi / nima taqlid
| Ishlaydi | Taqlid (MVP) |
|---|---|
| Restoran: chelak soni, tur, vaqt, rasm bilan e'lon; eng yaqin ferma masofasi | Ma'lumot brauzerda saqlanadi (`localStorage`), server yo'q |
| Xarita: restoranlar (to'q sariq = ochiq e'lon), fermalar (yashil) | Restoran va fermalar **namuna** (haqiqiy korxonalar emas) |
| Ferma: masofa bo'yicha e'lonlar, "Olib ketaman", "Qabul: toza / aralash" → reyting | Restoranga xabar yuborish, Telegram bot |
| Tejov hisobi: hajm × tarif (119 969,79 so'm/m³, Toshkent, 27.11.2026 taklifi) | 1 chelak ≈ 12 kg — **faraz**, intervyu va tarozi bilan almashtiriladi |

## Keyingi qadamlar
1. Telegram bot (@BotFather) va Mini App tugmasi.
2. Ochiq havola (GitHub Pages) — hakamlar ro'yxatdan o'tmasdan ochadi.
3. Intervyudan haqiqiy raqamlar (kg, to'lov), namuna nuqtalar o'rniga suhbatdosh roziligi bilan.
