# Hujjatlar: kanvas, MVP pasporti, intervyu jurnali

Tashkilotchining 1, 2, 3-shablonlari tuzilmasida (bo'limlar, tartib, maydonlar bir xil), O'zMU uslubida A4 PDF. Shrift 11 pt.

```bash
cd hujjatlar
python3 build.py            # hammasi -> ../chiqish/
python3 build.py kanvas     # faqat bittasi: kanvas | pasport | jurnal
python3 build.py shablon    # bo'sh shablonlar (kulrang ko'rsatmalar)
```
Google Chrome kerak (headless PDF), shriftlar uchun internet.

## Qayerga nima yoziladi
| Fayl | Nima | Repoda |
|---|---|---|
| `kanvas.py` | kanvas matni | ha |
| `pasport.py` | MVP pasporti | ha |
| `../maxfiy/jamoa.py` | jamoa nomi, tarkib, sardor telefoni | **yo'q** |
| `../maxfiy/jurnal.py` | intervyular, kontaktlar | **yo'q** |

Birinchi marta: `mkdir -p ../maxfiy && cp namuna_jamoa.py ../maxfiy/jamoa.py && cp namuna_jurnal.py ../maxfiy/jurnal.py`.

## Tekshiruv
- Bo'sh maydon kulrang ko'rsatma bilan chiqadi: topshirishdan oldin bitta ham kulrang qolmasin.
- Kanvas 2 betdan oshsa, `build.py` ogohlantiradi (+20% gacha ruxsat).
- Fayl nomlari shablon talabiga mos: `Kanvas_[Jamoa]_OzMU.pdf`, `MVP_[Jamoa].pdf`, `Jurnal_[Jamoa].pdf`.
- `chiqish/` repoga tushmaydi (jurnalda kontaktlar bor).
