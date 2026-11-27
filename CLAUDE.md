# CLAUDE.md: O'zMU jamoasi · Zakovat Hackaton 2026 · saralash ishi

Bu **topshiriladigan** ish repozitoriysi (shaklning "Repozitoriy yoki ishchi papka" maydoni). Foydalanuvchi bilan o'zbek tilida (lotin) gaplash.

## Chegara: bu repo va tayyorgarlik papkasi
| | Bu repo `ozmu-zakovat-2026` | Tayyorgarlik `~/zakovat xakaton prep` |
|---|---|---|
| Nima | saralash ishining o'zi: reja, vazifa tadqiqoti, kanvas/pasport matni, MVP kodi | nizom, qoidalar, shablonlar (md), umumiy tahlillar, video/motion-kit qoliplari |
| Kim ko'radi | **ochiq**, hakamlar ish tarixini ko'radi | ichki |
| Qoida | saralash bo'yicha har yangi fayl shu yerda | saralash ishini u yerda qilma; qoidalarni o'qish uchun ishlatiladi |

- Qoidalar va shablonlar matni: `~/zakovat xakaton prep/reglaments/` (`saralash_qoidalari.md`, `shablonlar/`, `forma_tuzilmasi.md`). Bu yerga ko'chirilmaydi.
- Video montaj kerak bo'lsa, `motion-kit` dan nusxa olinadi, natija (render) repoga qo'yilmaydi (`*.mp4` gitignore'da).

## Maxfiylik (repo ochiq)
- `maxfiy/` (jamoa tarkibi, telefonlar, intervyular) va `chiqish/` (PDF'lar) repoga tushmaydi.
- Intervyu matnini, ismini, raqamini hech qachon o'ylab topma. Raqamlar faqat manbadan (havola bilan) yoki intervyudan.
- Token, parol, `.env` commit qilinmaydi.

## Ish tartibi
- Reja: `docs/REJA.md`. Hujjatlar: `hujjatlar/` (`python3 build.py`).
- Har kungi ishni commit qil (ish tarixi baholanadi). **30-noyabr 00:00 dan keyin hech narsa commit qilinmaydi.**
