# Jamoa kanvasi (Shablon 1). Bo'sh "" qolgan maydon PDF'da kulrang ko'rsatma bo'lib chiqadi.
# Hajm: ~2 bet A4 (ko'pi bilan +20%). `python3 build.py kanvas` bet sonini ko'rsatadi.
# Raqam va manbalar faqat haqiqiy: manba havolasi ishlashi kerak. Intervyu insaytlari jurnaldan olinadi.
DATA = {
    "loyiha": "",        # loyiha nomi (sarlavhada katta chiqadi)
    "yonalish": "",      # "2-yo'nalish. Raqamli davlat, huquq va adolat"
    "vazifa": "",        # vazifa raqami va nomi

    # 2. Muammo
    "muammo": "",        # 3 gap: qanday muammo, kim uchun, qayerda
    "raqam": "",         # bitta mahalliy raqam
    "manba": "",         # ishlaydigan havola

    # 3. Mikro-auditoriya
    "kim": "",
    "geografiya": "",
    "daromadi": "",
    "hozir": "",
    "soni": "",          # taxminiy son + qanday hisoblangani

    # 4. Intervyu insaytlari (kamida 3)
    "insaytlar": [
        # {"kim": "D.R., 20 yosh, Toshkent", "dedi": "\"...\"", "tushundik": "..."},
    ],

    # 5. Yechim
    "yechim": "",        # 4–6 gap
    "mvp_havola": "",

    # 6. Biznes-model
    "kim_tolaydi": "",
    "nima_uchun": "",
    "qancha": "",
    "bepul": "",

    # 7–8. Xavf va tekshirish
    "xavf": "",
    "qadam": "",
    "natija": "",
}
