# B variant: talabalar ijarasi (vazifa berilmasa)

**Qachon ishlatiladi:** admin vazifalar ro'yxatini bermasa yoki ro'yxatda mos vazifa bo'lmasa. Qoidalar 3-band: jamoa yo'nalish doirasida o'z g'oyasini ishlab chiqadi.
**Yo'nalish:** 2. Raqamli davlat, huquq va adolat.
**Holat:** gipoteza. Intervyular tasdiqlamaguncha hech narsa "dalil" emas.

## Gipoteza
Toshkentga kelgan talaba arzon ijara e'loniga ishonib, uyni ko'rmasdan "bron" uchun kartaga pul o'tkazadi va aldanadi. Shartnomasiz yashagani uchun ijara kompensatsiyasini ham ololmaydi.

## Hozirgacha topilgan dalillar (manbasi bilan)
| Fakt | Manba |
|---|---|
| 2026-yil yanvar–mart: ijarada yashovchi talabalar 108 741, talabalar bilan 77 800+ ijara shartnomasi | https://talimxabarlari.uz/71571/ |
| Toshkent IIBB talabalar va ota-onalarni soxta ijara e'lonlaridan ogohlantirgan (08.08.2026) | https://talimxabarlari.uz/76736/ |
| Sxema: uy egasi "ko'p odam so'rayapti" deb, uyni ko'rsatmasdan kartaga pul so'raydi | https://anhor.uz/uzl/news/firibgarlar/ |
| Kompensatsiya: Toshkentda oyiga 440 ming so'mgacha (1 BHM), ariza har oy 7-sanagacha, kontrakt.edu.uz yoki my.gov.uz | https://infoedu.uz/talabalar-ijara-kompensatsiyasi-440-ming-som |
| Vazirlik 2022-yilda talabalar uchun ijara platformasi yaratgan | https://www.spot.uz/oz/2022/09/09/platform/ |

**Tekshirish kerak (hali tasdiqlanmagan):**
- [ ] Ijara firibgarligi holatlari soni (IIV, prokuratura). Hozircha topilmadi
- [ ] Vazirlikning 2022-yilgi platformasi ishlayaptimi?
- [ ] Talaba bilan ro'yxatdan o'tgan shartnoma tuzgan uy egasiga soliq imtiyozi: aniq qoida va lex.uz havolasi
- [ ] Kompensatsiya uchun shartnoma qanday ro'yxatdan o'tadi (soliq saytida uy egasi kiritadimi?)

## Mikro-auditoriya (taxmin, intervyuda aniqlanadi)
Viloyatdan kelgan 1–2-kurs talabasi, 18–20 yosh, yotoqxonada joy ololmagan, Toshkentda birinchi marta ijara qidiradi; oilasi oyiga ~1–1,5 mln so'm ijara to'laydi (raqam intervyudan olinadi).

## Kimlar bilan intervyu (5–7 ta)
| # | Kim | Nima bilish kerak |
|---|---|---|
| 1–3 | Ijarada yashovchi talabalar (1–2-kurs, viloyatdan) | qanday topgan, oldindan pul so'rashganmi, aldanganmi, shartnoma bormi, kompensatsiya olayaptimi |
| 4 | Aldangan talaba yoki uning ota-onasi | qanday bo'lgan, qancha pul, qayerga murojaat qilgan |
| 5 | Talabalarga uy beradigan uy egasi | nega shartnomasiz, ro'yxatdan o'tkazish qiyinmi, ishonchli ijarachi uchun nima qiladi |
| 6 | O'zMU talabalar turar joyi yoki yoshlar bilan ishlash bo'limi xodimi | nechta talaba yotoqxonasiz, shikoyatlar, kompensatsiya arizalari |
| 7 | Rieltor (ixtiyoriy) | talaba mijozlar, komissiya, firibgarlar sxemasi |

## Savollar (qo'llanmadagi 8 savolga qo'shimcha)
- Toshkentdagi hozirgi uyingizni qanday topdingiz? Qancha vaqt qidirdingiz?
- Uyni ko'rishdan oldin kimdir pul so'raganmi? Qancha? Nima qildingiz?
- O'zingiz yoki tanishlaringiz ijarada aldanganmi? Qanday?
- Uy egasi bilan shartnoma bormi? Bo'lmasa, nega?
- Ijara kompensatsiyasi haqida bilasizmi? Ariza berganmisiz? Nima to'sqinlik qildi?
- Uy egasi uchun: talabaga uy berganda eng katta qo'rquvingiz nima? Shartnomani ro'yxatdan o'tkazganmisiz?

## MVP rejasi (ishlaydigan prototip: Telegram bot)
1. **E'lon tekshiruvi:** talaba e'lon matni yoki havolasini yuboradi → SI xavf belgilarini sanaydi (uyni ko'rsatmasdan oldindan to'lov, narx tumandagi o'rtachadan juda past, shoshiltirish) → "xavfli / shubhali / normal" va sababi.
2. **Shartnoma:** talaba va uy egasi ma'lumotlarini kiritadi → namunaviy ijara shartnomasi (PDF).
3. **Kompensatsiya yo'riqnomasi:** qadam-baqadam, rasmiy havolalar bilan.
Taqlid qilinadigan qism: narxlar bazasi (qo'lda 20–30 ta e'lon), uy egasini tekshirish.
SI vositalari pasportda yoziladi.

## Biznes-model gipotezalari (intervyuda tekshiriladi)
- Talaba uchun bepul.
- Uy egasi "tekshirilgan e'lon" uchun to'laydi: unga ishonchli ijarachi va (tasdiqlansa) soliq imtiyozi.
- OTM bilan hamkorlik: yotoqxonasiz talabalarga xavfsiz ijara xizmati.

## Asosiy xavf (gipoteza)
Uy egalari shartnomani ro'yxatdan o'tkazishni va "tekshirilgan e'lon" uchun to'lashni xohlamaydi.
Tekshirish (1 hafta, $500): 20 ta uy egasiga taklif, kamida 5 tasi e'lonini tekshiruvga qo'ysa, gipoteza tasdiqlanadi.

## Raqobatchilar (tekshirish kerak)
OLX (umumiy, tekshiruvsiz), vazirlik platformasi (2022, holati noma'lum), Oson Ijara (faqat quruvchidan). Talabaga xos "tekshirilgan e'lon + shartnoma + kompensatsiya" xizmati topilmadi (27-noyabr, qisqa qidiruv).
