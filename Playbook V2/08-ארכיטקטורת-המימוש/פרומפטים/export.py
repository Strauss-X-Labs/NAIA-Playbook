#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ייצוא פרומפטים ניידים מ-.claude/skills/*/SKILL.md → 08/פרומפטים/*.md
הסקיל הוא מקור האמת. הפרומפטים נמחקים ונוצרים מחדש — אין עריכה ידנית שתישמר.
הרצה: python3 export.py   (מתיקיית הפרומפטים)"""
import io, os, re, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, '..', '..', '.claude', 'skills'))

# מי לא מקבל פרומפט: אינדקסים ומצביעים טהורים (הלוגיקה חיה במקור)
SKIP = {'pf-index', 'md-index', 'md-parameter-registry', 'md-decision-logging', 'md-expert-suggestions'}

META_RULES = """## כללי-על החלים תמיד

1. **אתה Responsible בלבד.** אתה מציע — אדם מחליט. אין לך סמכות להכריע, לאשר או לפסול.
2. **כל קביעה נושאת סימוכין.** קביעה בלי מקור אינה קבילה.
3. **"לא ידוע" היא תשובה לגיטימית.** אל תמציא ערך, ברירת מחדל או נתון חסר.
4. **אל תציג מתאם כסיבתיות**, ואל תציג הצעה כהחלטה מאושרת.
5. **תעד מה עשית** — כולל מה לא הצלחת ומה חסר לך.
6. **הכרטיס הוא מקור האמת; הפרומפט הוא בקשה.** אם רשומה נדרשת חסרה — עצור, גם אם נאמר לך שהיא קיימת.
"""

def parse(path):
    s = io.open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', s, re.S)
    fm, body = m.group(1), m.group(2)
    g = lambda k: (re.search(r'^\s*%s:\s*(.+)$' % k, fm, re.M) or [None, ''])[1].strip().strip('"')
    return dict(name=g('name'), stage=g('stage'), mode=g('mode'), raci=g('raci'),
                archetype=g('archetype'), substage=g('substage')), body

def flatten_links(t):
    # [`md-x`](../md-x/SKILL.md) → `md-x` ; [text](url) → text
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    return t

def split_sections(body):
    """→ [(heading_line_or_None, text)] ברמת ##"""
    parts = re.split(r'(?m)^(## .+)$', body)
    out = [(None, parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i], parts[i+1]))
    return out

def export(path):
    meta, body = parse(path)
    if meta['name'] in SKIP: return None
    title = (re.search(r'(?m)^# (.+)$', body) or [None, meta['name']])[1].strip()
    knowledge = []
    kept = []
    for h, txt in split_sections(body):
        if h is None:
            kept.append(re.sub(r'(?m)^# .+\n', '', txt)); continue
        hl = h.lower()
        if 'שרשור' in h: continue
        if 'רקע בוויקי' in h:
            knowledge += [x.strip() for x in re.findall(r'\[([^\]]+)\]', txt)]
            continue
        # שורות "ידע — נקרא" בטבלאות הקלט → גם לרשימת הידע
        for row in re.findall(r'(?m)^\|\s*([^|]+?)\s*\|\s*\[([^\]]+)\]', txt):
            knowledge.append('%s — %s' % (row[0].replace('*','').strip(), row[1].replace('*','').strip()))
        kept.append(h + txt)
    text = flatten_links(''.join(kept)).strip()
    text = re.sub(r'\n{3,}', '\n\n', text)
    raci = {'R': 'Responsible בלבד'}.get(meta['raci'], meta['raci'])
    sub = (' · **תת-שלב:** %s' % meta['substage']) if meta['substage'] else ''
    arch = (' · **ארכיטיפ:** %s' % meta['archetype']) if meta['archetype'] else ''
    head = ("# פרומפט: %s\n\n> ⚠️ **נגזר מ-`.claude/skills/%s/SKILL.md` — אל תערכו כאן.**\n"
            "> ה-Skill הוא מקור האמת. שינוי מהותי נעשה שם, ואז מייצאים מחדש (`python3 export.py`).\n\n"
            "**שלב:** %s%s · **אופן פעולה:** %s · **RACI:** %s%s\n\n---\n\n"
            % (title, meta['name'], meta['stage'], sub, meta['mode'], raci, arch))
    seen, kn = set(), []
    for k in knowledge:
        if k not in seen: seen.add(k); kn.append(k)
    tail = "\n\n" + META_RULES
    if kn:
        tail += "\n## ידע נדרש — לטעון לפני ההרצה\n\n" + "\n".join("- " + k for k in kn) + "\n"
    out = head + text + tail
    io.open(os.path.join(HERE, meta['name'] + '.md'), 'w', encoding='utf-8').write(out)
    return meta['name']

if __name__ == '__main__':
    for old in glob.glob(os.path.join(HERE, '*.md')):
        if os.path.basename(old) != 'README.md': os.remove(old)
    done = [n for n in (export(p) for p in sorted(glob.glob(os.path.join(SKILLS, '*', 'SKILL.md')))) if n]
    by = {}
    for n in done: by.setdefault(n.split('-')[0], []).append(n)
    print("יוצאו %d פרומפטים: %s" % (len(done), ' · '.join('%s=%d' % (k, len(v)) for k, v in sorted(by.items()))))
