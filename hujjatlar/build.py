#!/usr/bin/env python3
"""Saralash hujjatlari: tashkilotchi shablonlari tuzilmasida, O'zMU uslubida A4 PDF.

Ishlatish (hujjatlar/ papkasidan):
    python3 build.py            -> chiqish/Kanvas.pdf, chiqish/MVP.pdf, chiqish/Jurnal.pdf
    python3 build.py kanvas     -> faqat bittasi (kanvas | pasport | jurnal)
    python3 build.py shablon    -> bo'sh shablonlar (kulrang ko'rsatmalar bilan)

Matn:  kanvas.py, pasport.py (ochiq, repoda)
       ../maxfiy/jamoa.py  (sardor telefoni, tarkib)   ../maxfiy/jurnal.py  (intervyular)
       maxfiy/ repoga tushmaydi. Yo'q bo'lsa namuna_jamoa.py / namuna_jurnal.py ishlatiladi.
Bo'sh qoldirilgan maydon kulrang ko'rsatma bilan chiqadi: topshirishdan oldin bitta ham kulrang qolmasin.
**qalin** -> qalin. Oddiy ' yozing: o‘/g‘ avtomatik.
"""
import html, re, runpy, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "chiqish"


def load(name, private=None):
    p = ROOT / "maxfiy" / f"{private}.py" if private else None
    if p and p.exists():
        return runpy.run_path(str(p))["DATA"]
    src = HERE / (f"namuna_{private}.py" if private else f"{name}.py")
    return runpy.run_path(str(src))["DATA"]


# ---------------------------------------------------------------- uslub
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');
@page { size: A4 %(orient)s; margin: 12mm 13mm 12mm 13mm }
:root { --navy:#232856; --gold:#BEA587; --gold-d:#8C6D45; --gold-l:#F6F1EA; --edge:#DADCE8; --mute:#8A8CA6; --ink:#1E2247 }
* { box-sizing:border-box; margin:0; padding:0 }
body { font-family:'Montserrat',Arial,sans-serif; font-size:11pt; line-height:1.35; color:var(--ink);
  -webkit-print-color-adjust:exact; print-color-adjust:exact }
header { display:flex; align-items:center; gap:12px; background:var(--navy); color:#fff; border-radius:10px;
  padding:10px 16px; border-bottom:3px solid var(--gold); margin-bottom:10px }
header img { height:46px; background:#fff; border-radius:50%%; padding:3px }
header .t { flex:1 }
header .org { font-size:7.5pt; color:var(--gold); font-weight:600; letter-spacing:.02em }
header h1 { font-size:15pt; font-weight:700; line-height:1.15 }
header h1 span { font-size:9pt; font-weight:500; color:#C9CBE0; margin-left:8px }
header .meta { text-align:right; font-size:8pt; color:#C9CBE0; line-height:1.35 }
header .meta b { color:var(--gold); font-weight:600 }
.rule { border:1px solid var(--gold); background:var(--gold-l); border-radius:8px; padding:6px 10px; font-size:11pt; margin-bottom:8px }
section { margin-bottom:9px; break-inside:avoid }
section.flow { break-inside:auto }
h2 { font-size:12pt; font-weight:700; color:var(--navy); display:flex; align-items:center; gap:7px;
  border-bottom:1.5px solid var(--navy); padding-bottom:3px; margin-bottom:5px }
h2 i { font-style:normal; background:var(--gold); color:var(--navy); border-radius:5px; font-size:9pt;
  min-width:20px; height:20px; display:inline-flex; align-items:center; justify-content:center }
.intro { font-size:8.5pt; color:var(--mute); margin-bottom:4px }
table { width:100%%; border-collapse:separate; border-spacing:0; border:1px solid var(--edge); border-radius:8px; overflow:hidden }
td, th { border-bottom:1px solid var(--edge); padding:4px 8px; vertical-align:top; text-align:left }
tr:last-child td { border-bottom:none }
th { background:var(--navy); color:#fff; font-size:11pt; font-weight:600 }
td.k { width:28%%; background:#F4F5FA; font-weight:600; font-size:11pt; color:var(--navy) }
td.n { width:26px; text-align:center; font-weight:700; color:var(--gold-d) }
.box { border:1px solid var(--edge); border-radius:8px; padding:6px 10px }
ul { padding-left:16px } li { margin:1px 0 } li::marker { color:var(--gold-d) }
b { font-weight:700; color:var(--gold-d) }
.hint { color:#A3A5BA; font-style:italic; font-size:9pt }
a { color:var(--navy) }
footer { margin-top:8px; font-size:7.5pt; color:var(--mute); display:flex; justify-content:space-between;
  border-top:1px solid var(--edge); padding-top:4px }
"""


def rich(v):
    s = html.escape(str(v), quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', s)
    return s.replace("\n", "<br>")


def val(v, hint):
    """Qiymat bo'sh bo'lsa kulrang ko'rsatma. Ro'yxat -> nuqtali ro'yxat."""
    if isinstance(v, (list, tuple)):
        v = [x for x in v if str(x).strip()]
        if not v:
            return f'<span class="hint">{rich(hint)}</span>'
        return "<ul>" + "".join(f"<li>{rich(x)}</li>" for x in v) + "</ul>" if len(v) > 1 else rich(v[0])
    if v is None or not str(v).strip():
        return f'<span class="hint">{rich(hint)}</span>'
    return rich(v)


def kv(rows, d):
    return "<table>" + "".join(f'<tr><td class="k">{rich(lbl)}</td><td>{val(d.get(key, ""), hint)}</td></tr>'
                               for lbl, key, hint in rows) + "</table>"


def grid(cols, items, min_rows, numbered=True):
    items = list(items) + [{}] * max(0, min_rows - len(items))
    head = ('<th class="n">№</th>' if numbered else "") + "".join(f"<th>{rich(c[0])}</th>" for c in cols)
    body = ""
    for i, it in enumerate(items, 1):
        body += "<tr>" + (f'<td class="n">{i}</td>' if numbered else "")
        body += "".join(f"<td>{val(it.get(c[1], ''), c[2] if i == 1 else '')}</td>" for c in cols) + "</tr>"
    return f"<table><tr>{head}</tr>{body}</table>"


def sec(n, title, inner, intro="", flow=False):
    i = f'<p class="intro">{rich(intro)}</p>' if intro else ""
    return f'<section class="{"flow" if flow else ""}"><h2><i>{n}</i>{rich(title)}</h2>{i}{inner}</section>'


def page(title, sub, body, jamoa, orient="portrait", foot=""):
    meta = (f"<b>{html.escape(jamoa.get('jamoa') or 'Jamoa nomi')}</b><br>"
            f"Zakovat Hackaton 2026<br>Saralash bosqichi")
    return f"""<!doctype html><html lang="uz"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{CSS % {'orient': orient}}</style></head><body>
<header><img src="{(HERE / 'assets/nuu-logo.svg').as_uri()}" alt="O'zMU"><div class="t">
<div class="org">MIRZO ULUG'BEK NOMIDAGI O'ZBEKISTON MILLIY UNIVERSITETI</div>
<h1>{html.escape(title)}<span>{html.escape(sub)}</span></h1></div><div class="meta">{meta}</div></header>
{body}
<footer><span>{rich(foot)}</span><span>Zakovat Hackaton 2026 · Saralash bosqichi</span></footer>
</body></html>"""


# ---------------------------------------------------------------- 1. Kanvas
def kanvas(k, j):
    s = []
    s.append(sec(1, "Umumiy ma'lumot", kv([
        ("Jamoa nomi", "jamoa", "Jamoa nomi"),
        ("OTM", "otm", "to'liq nomi"),
        ("Yo'nalish", "yonalish", "masalan: 2-yo'nalish. Raqamli davlat, huquq va adolat"),
        ("Vazifa", "vazifa", "vazifa raqami va nomi"),
        ("Sardor va tarkib", "tarkib", "sardor: F.I.Sh., telefon, Telegram; ishtirokchilar: F.I.Sh. vergul bilan"),
    ], {**j, **{x: k.get(x, "") for x in ("yonalish", "vazifa")}})))
    s.append(sec(2, "Muammo", kv([
        ("Muammo", "muammo", "3 ta gap: qanday muammoni, kim uchun va qayerda hal qilasiz. Aniq O'zbekiston yoki hudud haqida, \"butun dunyoda\" kabi umumiy gaplarsiz"),
        ("Mahalliy raqam", "raqam", "muammo ko'lamini ko'rsatadigan bitta raqam"),
        ("Manba", "manba", "ishlaydigan havola: stat.uz, lex.uz, UNDP Uzbekistan, Jahon banki, vazirliklar"),
    ], k)))
    s.append(sec(3, "Mikro-maqsadli auditoriya", kv([
        ("Ular kim", "kim", "yoshi, jinsi, oilaviy holati"),
        ("Geografiya", "geografiya", "hudud, aholi punkti turi"),
        ("Daromadi yoki iqtisodiy holati", "daromadi", "daromad yoki iqtisodiy holat"),
        ("Muammoni hal qilish uchun hozir nima qilishadi", "hozir", "hozirgi yo'l va uning kamchiligi"),
        ("O'zbekistonda bunday odamlar qancha", "soni", "taxminiy son va uni qanday hisobladingiz"),
    ], k), "Yechimingiz mo'ljallangan bitta aniq odamlar guruhi. Butun bozor emas."))
    s.append(sec(4, "Intervyu insaytlari", grid([
        ("Suhbatdosh: ismi yoki initsiallari, yoshi, hududi", "kim", "masalan: D.R., 20 yosh, Toshkent"),
        ("U nima dedi", "dedi", "1–2 so'zma-so'z iqtibos"),
        ("Biz nimani tushundik", "tushundik", "nima tasdiqlandi yoki o'zgardi"),
    ], k.get("insaytlar", []), 3), "Maqsadli auditoriya vakillari bilan suhbatlardan kamida 3 ta insayt."))
    s.append(sec(5, "Yechim", f'<div class="box">{val(k.get("yechim", ""), "4–6 ta gap: nimani taklif qilasiz, maqsadli auditoriyangizdagi odam undan qanday foydalanadi, yechim mavjud yechimlardan nimasi bilan farq qiladi.")}'
                 f'<p style="margin-top:5px"><b style="color:var(--navy)">MVP-layt havolasi:</b> {val(k.get("mvp_havola", ""), "havola")}</p></div>'))
    s.append(sec(6, "Biznes-model", kv([
        ("Kim to'laydi", "kim_tolaydi", "to'lovchi"),
        ("Nima uchun", "nima_uchun", "qaysi qiymat uchun to'laydi"),
        ("Qancha", "qancha", "narx va taxminiy hisob-kitob"),
        ("Foydalanuvchi uchun bepul bo'lsa", "bepul", "kim moliyalashtiradi va nima uchun"),
    ], k)))
    s.append(sec(7, "Asosiy xavf", f'<div class="box">{val(k.get("xavf", ""), "Noto‘g‘ri chiqsa, g‘oyani barbod qiladigan bitta taxmin. \"Pul yetmaydi\" yoki \"raqobat\" emas, balki foydalanuvchi, bozor yoki model haqidagi mazmunli taxmin.")}</div>'))
    s.append(sec(8, "Birinchi navbatda nimani tekshirish kerak", kv([
        ("Qadam", "qadam", "aniq nima qilasiz (bir hafta va $500 bilan)"),
        ("Gipoteza tasdiqlanadigan natija", "natija", "masalan: 20 kishidan 10 tasi ariza qoldirdi"),
    ], k), "Agar sizda bir hafta va $500 bo'lsa, 7-bo'limdagi taxminni qanday tekshirgan bo'lardingiz?"))
    return page(k.get("loyiha") or "Jamoa kanvasi", "Jamoa kanvasi" if k.get("loyiha") else "", "".join(s), j,
                foot="Manbalar havolalari ishlaydi. Raqamlar faqat manbadan yoki intervyudan.")


# ---------------------------------------------------------------- 2. MVP pasporti
def pasport(p, j):
    s = []
    s.append(sec(1, "Mahsulot haqida", kv([
        ("Mahsulot nomi", "nomi", "nomi"),
        ("MVP turi", "turi", "maket, lending, prototip, metodika yoki huquqiy shablon"),
        ("Kim uchun", "kim_uchun", "kanvasning 3-bo'limidan bitta qator"),
        ("Qaysi muammoni hal qiladi", "muammo", "bitta gap"),
    ], p)))
    s.append(sec(2, "Havolalar", kv([
        ("MVP", "mvp_havola", "havola orqali ro'yxatdan o'tmasdan yoki quyidagi test akkaunti bilan ochiladi"),
        ("Repozitoriy yoki ishchi papka", "repo", "https://github.com/farrux05-ai/ozmu-zakovat-2026"),
        ("Hakamlar uchun test akkaunti", "test_akkaunt", "agar MVP ularsiz ochilmasa, login va parol; aks holda \"kerak emas\""),
    ], {"repo": "https://github.com/farrux05-ai/ozmu-zakovat-2026", **p})))
    s.append(sec(3, "Asosiy ssenariy", grid([
        ("Foydalanuvchi nima qiladi", "qiladi", "qadam"), ("U nima oladi", "oladi", "natija"),
    ], p.get("ssenariy", []), 5), "Auditoriyangizdagi odam muammodan natijagacha qanday yo'l bosadi: 3–7 qadam."))
    s.append(sec(4, "Nima ishlaydi va nima hali ishlamaydi", kv([
        ("Hozirning o'zida ishlaydi", "ishlaydi", "ishlaydigan qismlar"),
        ("Hozircha taqlid qilinadi", "taqlid", "\"parda ortida\" qo'lda bajariladigan yoki vaqtinchalik o'rinbosar bilan ko'rsatilgan qismlar"),
        ("Keyin nima qilamiz", "keyin", "keyingi qadam"),
    ], p)))
    s.append(sec(5, "Hakamlar MVPni qanday tekshiradi", grid([
        ("Harakat va kutilgan natija", "harakat", "nimani ochish, nimani bosish, nima ko'rinishi kerak"),
    ], p.get("tekshirish", []), 3), "3–5 qadam: nimani ochish, nimani bosish, hakamlar nimani ko'rishi kerak."))
    s.append(sec(6, "Vositalar, SI va begona materiallar", kv([
        ("Vositalar va texnologiyalar", "vositalar", "dasturlash tili, platforma, servislar"),
        ("SIdan foydalanish", "si", "qaysi vositalar va nima uchun: kod, matnlar, tasvirlar, tahlil, tarjima. Foydalanmagan bo'lsangiz, \"yo'q\""),
        ("Begona materiallar", "begona", "shablonlar, kutubxonalar, ma'lumotlar, tasvirlar: nima, qayerdan, qanday shartlarda. Yo'q bo'lsa, \"yo'q\""),
    ], p)))
    s.append(sec(7, "Foydalanuvchilar bilan birinchi sinov", f'<div class="box">{val(p.get("sinov", ""), "MVPni auditoriyadagi odamlarga ko‘rsatishga ulgurgan bo‘lsangiz: necha kishi, ular nima qildi, nima dedi. Agar yo‘q bo‘lsa, qanday va qachon ko‘rsatishingizni yozing.")}</div>'))
    return page("MVP-layt pasporti", p.get("nomi") or "", "".join(s), j)


# ---------------------------------------------------------------- 3. Intervyu jurnali
def jurnal(jr, j):
    s = []
    s.append('<div class="rule">Barcha suhbatlar haqiqiy. Suhbatdoshlar ism/initsial, yosh va hududni ko\'rsatishga '
             'hamda tashkilotchilarning nazorat qo\'ng\'irog\'iga rozilik bergan. Jurnal faqat tashkilotchilar uchun.</div>')
    s.append(sec(1, "Jurnal", grid([
        ("Suhbatdosh", "kim", "ismi yoki initsiallari, yoshi, hududi; vazifa uchun u kim; sana va format: yuzma-yuz yoki qo'ng'iroq"),
        ("Kontakt va rozilik", "kontakt", "telefon yoki Telegram; nazorat qo'ng'irog'iga rozilik: ha"),
        ("U nima dedi", "dedi", "asosiy fikr o'z so'zlaringiz bilan va 1–2 ta so'zma-so'z iqtibos"),
        ("Biz nimani tushundik", "tushundik", "nima tasdiqlandi, gipotezada nima o'zgardi"),
    ], jr.get("intervyular", []), 5), flow=True))
    s.append(sec(2, "Intervyu natijalari", kv([
        ("Nima tasdiqlandi", "tasdiqlandi", "tasdiqlangan taxminlar"),
        ("Gipotezamizni nima rad etdi yoki o'zgartirdi", "rad_etdi", "rad etilgan yoki o'zgargan taxminlar"),
        ("Nima hayratlantirdi", "hayrat", "kutilmagan topilma"),
    ], jr)))
    return page("Intervyular jurnali", "", "".join(s), j, orient="landscape",
                foot=f"Intervyular soni: {len([x for x in jr.get('intervyular', []) if x.get('kim')])}")


# ---------------------------------------------------------------- yig'ish
def uz(doc):
    """o' g' -> o‘ g‘, qolgan ' -> ’ (faqat teglar orasidagi matnda, havolalardan tashqari)."""
    head, body = doc.split("<body>", 1)
    def fix(m):
        t = m.group(0)
        if "http" in t:
            return t
        t = re.sub(r"([oOgG])'", "\\1\u2018", t)
        return t.replace("'", "\u2019")
    return head + "<body>" + re.sub(r">[^<]+<", fix, body)


def render(name, doc, fname):
    OUT.mkdir(exist_ok=True)
    h = OUT / f"{fname}.html"
    h.write_text(uz(doc), encoding="utf-8")
    pdf = OUT / f"{fname}.pdf"
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", h.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))
    shown = pdf.relative_to(ROOT) if pdf.is_relative_to(ROOT) else pdf
    warn = "  <- KANVAS 2 BETDAN OSHDI (+20% gacha ruxsat), qisqartiring" if name == "kanvas" and pages > 2 else ""
    print(f"OK  {shown}  ({pages} bet){warn}")


if __name__ == "__main__":
    args = sys.argv[1:]
    blank = "shablon" in args
    want = [a for a in args if a in ("kanvas", "pasport", "jurnal")] or ["kanvas", "pasport", "jurnal"]
    j = {} if blank else load("jamoa", "jamoa")
    jn = j.get("jamoa") or "Jamoa"
    sfx = "_shablon" if blank else ""
    if "kanvas" in want:
        render("kanvas", kanvas({} if blank else load("kanvas"), j), f"Kanvas_{jn}_OzMU{sfx}")
    if "pasport" in want:
        render("pasport", pasport({} if blank else load("pasport"), j), f"MVP_{jn}{sfx}")
    if "jurnal" in want:
        render("jurnal", jurnal({} if blank else load("jurnal", "jurnal"), j), f"Jurnal_{jn}{sfx}")
