# Video: yakuniy qaror va ish tartibi

## Qaror (27-noyabr)
| | |
|---|---|
| Format | **16:9, 1920×1080, 30 fps**. Hakamlar noutbukda ko'radi |
| Davomiyligi | **3:00** (ruxsat 2:45–3:15) |
| Uslub | **Gibrid, "tun" skin** (jamoa 27-noyabrda tanladi: qora fonda yozuvlar diqqatni bir joyga yig'adi). Qora fon, oq qo'lyozma chiziqlar, bitta oltin urg'u. **Hook va yakun: siluet animatsiya** (8–10 s), **o'rta qism: daftar bloklari** (mexanizm, raqam, MVP). Namuna: tayyorgarlik repo'sida `daftar-kit/ferma-16x9-v1.mp4`, kod `daftar-kit/ferma/` |
| O'qilish tuzatishlari | Namunadagi kichik yozuvlar kattalashtiriladi: varaqdagi matn **≥ 44 px**, pastki izoh **≥ 34 px**, oq chiziq qalinroq; raqamlar oltin rangda eng katta element |
| Kadr | Spiker **chapda (40%)**, o'ngda varaq, unda bir vaqtda **bitta g'oya**. Siluet hookda ham spiker ovozi eshitiladi va hook tugashi bilan spiker katta panelda chiqadi (jamoa kadrda bo'lishi shart) |
| Zaxira | Siluet sahnasi ulgurmasa: o'sha "tun" skin'da faqat daftar bloklari (siluetsiz) |
| Spikerlar | **3 kishi, har biri o'z bloklarida** (qoida: ko'pchilik kadrda, bir necha kishi gapiradi) |
| Ovoz | Faqat jamoaning **haqiqiy ovozi**. SI-avatar va sintez ovoz yo'q. Musiqa va SFX o'zimiz sintez qilgan |
| MVP | 1:25–2:10 blokida **ekran yozuvi** varaqdagi telefon yoki noutbuk ramkasi ichida (fokus rejimi) |
| Subtitr | Faqat kalit iboralar, daqiqasiga 3–5 ta |
| Raqamlar | Har raqam yonida `MANBA: ...`. Manbasiz raqam ekranga chiqmaydi |

Nega shunday: qora fonda bitta g'oya yoziladi, diqqat chalg'imaydi; siluet hook esda qoladi; qo'lyozma uslub slayd o'qishga o'xshamaydi. Spiker kadrda turadi, ya'ni "Video va jamoa" mezoni (15 ball) bajariladi. Xavf: qora fonda mayda yozuv o'qilmaydi, shuning uchun o'lcham qoidalari qat'iy.

## Ish tartibi
1. **Ssenariy** (`ssenariy.md`): 6 blok, har blokda kim gapiradi, 2–4 ta tezis, varaqda nima chiqadi. Kanvas tayyor bo'lgach yoziladi, raqamlar kanvasdagi bilan bir xil.
2. **Tasvirga olish** (smartfon, quyidagi cheklist): har blok alohida, 2–3 dubl. Spiker kadrning **chap uchdan birida**, o'ng tomoni bo'sh devor.
3. **MVP ekran yozuvi**: 1080p, 30–40 s, asosiy ssenariy boshidan oxirigacha.
4. **Montaj**:
   - eng yaxshi dubllar tanlanadi, jimlik kesiladi (`montaj/engine.py`, tayyorgarlik papkasida);
   - so'z vaqtlari olinadi (transkripsiya). Bu faqat matnni aniqlash, ovoz o'zgartirilmaydi;
   - varaq animatsiyasi so'z vaqtlariga bog'lanadi (`daftar-kit`, tayyorgarlik papkasida);
   - render **cloud sessiyada** qilinadi (noutbuk kuchsiz, 3 daqiqa ~50+ daqiqa).
5. **Tekshiruv**: davomiylik 2:45–3:15, ovoz quloqchinsiz eshitiladi, har raqamning manbasi bor, havola inkognitoda ochiladi.
6. **Yuklash**: YouTube (havola orqali kirish), nomi `MVP-sprint_OzMU_jamoasi`. Render fayli repoga qo'yilmaydi.

## Tasvirga olish cheklisti
- [ ] Telefon **gorizontal**, shtativ yoki kitoblar ustida, ko'z darajasida
- [ ] 1080p, 30 fps; ekran tozalangan, "Bezovta qilmang" yoqilgan
- [ ] Yorug'lik yuzga oldindan (deraza oldida), orqada yorug' manba yo'q
- [ ] Spiker chap uchdan birida, o'ng tomoni tekis va bo'sh
- [ ] Mikrofon 30–50 sm, xona shovqinsiz; 5 soniya jimlik yozib olinadi (shovqinni tozalash uchun)
- [ ] Har blok alohida, boshida qarsak (ovoz va tasvirni moslash uchun)
- [ ] Kiyim bir xil (bloklar bitta kunda olingandek ko'rinsin)
- [ ] Tezis bilan gapiriladi, yodlab yoki ekrandan o'qib emas; kameraga qarab

## Vaqt rejasi (29-noyabr)
| Vaqt | Ish |
|---|---|
| 11:00–12:00 | Ssenariy yakuni, bir marta ovoz chiqarib o'qish, vaqtni o'lchash |
| 12:00–14:00 | Tasvirga olish (6 blok × 2–3 dubl) + MVP ekran yozuvi |
| 14:00–15:00 | Dubllarni tanlash, transkripsiya |
| 15:00–19:00 | Animatsiya va render (cloud): avval daftar bloklari, keyin siluet hook va yakun |
| 19:00–20:00 | Tekshiruv, tuzatish, YouTube'ga yuklash |
| 20:00 | Havola tayyor. Zaxira: animatsiyasiz oddiy montaj (spiker + MVP ekran yozuvi + raqam kartochkalari) |
