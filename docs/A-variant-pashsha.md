# A variant: restoran oshxona chiqindisi → qora askar pashshasi lichinkasi → parranda va baliq ozuqasi

**Holat:** gipoteza (28-noyabr). Intervyular tasdiqlamaguncha hech narsa "dalil" emas.
**Yo'nalish (tavsiya):** 5. Oziq-ovqat va qishloq xo'jaligi. Qiymat ozuqa oqsilida yaratiladi (import soya shroti o'rnini bosish). Muqobil: 4. Ekologiya.

## G'oya bir jumlada
Toshkent restoranlari oshxona chiqindisini qimmat tarif bilan poligonga yuboradi. Biz uni olib ketib, qora askar pashshasi (*Hermetia illucens*) lichinkasiga beramiz. Lichinkadan parranda va baliq uchun oqsilli ozuqa, qoldig'idan o'g'it olinadi.

## Hozirgacha topilgan dalillar (manbasi bilan)
| Fakt | Manba |
|---|---|
| Toshkent shahri yuridik shaxslar uchun chiqindi olib ketish tarifini oshirish taklif qilingan: 89 977,57 → **119 969,79 so'm/m³** (QQSsiz), 27.11.2026, 15 kunlik muhokamada | https://www.gazeta.uz/oz/2026/11/27/tariffs/ · https://www.spot.uz/oz/2026/11/27/waste-tariff |
| Toshkent viloyati: yuridik shaxslar 86 890 so'm/m³ (QQSsiz), 1.04.2026 dan | https://www.spot.uz/oz/2026/03/25/waste-tariff |
| O'zbekiston 2026-yil yanvar–sentyabrda Rossiyadan 245 ming t soya shroti olgan; O'zbekiston uchun o'rtacha eksport narxi **509 $/t** (Rossiya eksport statistikasi) | https://uz.kursiv.media/2026-04-29/uzbekistan-zakupil-70-tys-tonn-soevogo-shrota/ · https://www.oilworld.ru/analytics/reviews/305338 |
| Toshkent viloyati sharoitida qora askar pashshasini ko'paytirish texnologiyasi bo'yicha ilmiy ish; parranda ozuqasi sifatida sinovlar | https://zenodo.org/records/15384115 · https://zenodo.org/records/15644760 |
| Lichinka sikli 10–14 kun; mayda xo'jalik uchun biznes-model (O'zbekiston, 2025) | https://expertiza.uz/upload/iblock/35d/1t9fh7ufb6gk5db5twb7qt16ls49xeun.pdf |
| Toshkentda tuxum sotuvchi insektariy bor (bozor shakllanmoqda) | https://agro-uzbekistan.com/ru/trade/i-3077/ |

**Topilmadi / tekshirish kerak:**
- [ ] Bitta restoran kuniga necha kg oshxona chiqindisi chiqaradi (intervyudan olinadi, o'ylab topilmaydi)
- [ ] Restoran hozir chiqindiga oyiga qancha to'laydi (intervyu)
- [ ] O'zbekistonda lichinkani ozuqaga ishlatish bo'yicha veterinariya va sanitariya talablari
- [ ] Lichinka uni yoki tirik lichinka narxi (Toshkentdagi sotuvchilar)
- [ ] O'zbekistonda tijoriy BSF korxonalari (qisqa qidiruvda topilmadi)

## Mikro-auditoriya (taxmin)
**To'lovchi va manba:** Toshkent shahridagi o'rta va katta restoran yoki oshxona (kuniga 100+ porsiya), oshxona menejeri yoki egasi.
**Xaridor:** Toshkent viloyatidagi parranda yoki baliq fermasi (ozuqa xarajati katta).

## Kimlar bilan intervyu (5–7 ta)
| # | Kim | Nima bilish kerak |
|---|---|---|
| 1–3 | Restoran yoki oshxona menejeri / egasi | kuniga qancha chiqindi, kim olib ketadi, oyiga qancha to'laydi, saralash mumkinmi, tarif oshishi haqida biladimi |
| 4–5 | Parranda yoki baliq fermeri | ozuqaga oyiga qancha ketadi, oqsil manbai nima (soya shroti?), hasharot ozuqasini sinab ko'radimi, qancha to'lashga tayyor |
| 6 | Lichinka yetishtiruvchi yoki entomolog (agro-uzbekistan e'loni, ilmiy ish mualliflari) | substrat, hosildorlik, sanitariya talablari |
| 7 | Chiqindi tashuvchi operator (ixtiyoriy) | restoranlardan chiqindi qanday yig'iladi |

## Savollar (qo'llanmadagi 8 savolga qo'shimcha)
- Restoran: kecha oshxonada qancha chiqindi chiqdi? Kim olib ketdi? Oxirgi oyda chiqindi uchun qancha to'ladingiz?
- Restoran: sabzavot po'sti, non, ovqat qoldig'i alohida yig'iladimi? Buning uchun nima kerak bo'lardi?
- Fermer: oxirgi oyda ozuqaga qancha pul ketdi? Oqsilni nimadan olasiz, qayerdan, qanchadan?
- Fermer: hasharot yoki lichinka ozuqasi haqida eshitganmisiz? Sinab ko'rganmisiz? Nega?

## MVP rejasi (ishlaydigan prototip: Telegram bot + hisob-kitob)
1. **Restoran uchun bot:** kunlik chiqindini kiritadi (kg, rasm) → bot olib ketish vaqtini belgilaydi; SI rasmdan aralashmani aniqlaydi (plastik, suyak, folga bor-yo'qligi, chunki lichinkaga faqat toza organika kerak).
2. **Hisob paneli:** restoranning oylik tejovi (tarif × hajm) va qayta ishlangan kg; fermer uchun ozuqa narxi taqqoslovi.
Taqlid qilinadigan qism: olib ketish logistikasi va lichinka fermasi (fizik qism) qo'lda/taxminiy.

## Biznes-model gipotezalari
- Restoran: hozirgi tarifdan arzon to'lov evaziga oshxona chiqindisi olib ketiladi (yoki tekin, agar saralab bersa).
- Fermer: lichinka uni yoki tirik lichinka uchun to'laydi (soya shroti o'rnini qisman bosadi).
- Qo'shimcha: lichinka qoldig'i (frass) o'g'it sifatida sotiladi.

## Asosiy xavf (gipoteza)
Lichinka oqsilini ozuqa sifatida sotishga ruxsat (veterinariya) va fermerning ishonchi. Yevropa Ittifoqida hasharotni restoran qoldig'ida boqib, chorva ozuqasiga ishlatish taqiqlangan (aniq qoida tekshiriladi). Shuning uchun boshlang'ich substrat: faqat **ovqat tayyorlashdan oldingi** oshxona chiqindisi (sabzavot, meva po'sti, non), likopchadan qolgan ovqat emas.
Tekshirish (1 hafta, $500): 10 ta fermerga lichinka namunasi taklif, kamida 3 tasi buyurtma bersa, gipoteza tasdiqlanadi.

## Qayta hisob (rubrika, 28-noyabr; baho, o'lchov emas)
| | Auditoriya 30% | Biznes 25% | MVP 20% | Dalil 15% | Noyoblik 10% | /100 |
|---|---|---|---|---|---|---|
| **A: pashsha** | 3.5 | 4 | 3 | 4 | 5 | **75** |
| B: ijara | 5 | 4 | 5 | 4 | 2 | **86** |
