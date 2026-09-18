---
name: pf-horizon-scanning
description: "עוקב אחר יכולות AI חדשות ובודק אם הן פותחות בעיות שהוקפאו בגלל חוסר בשלות טכנולוגית. Use for the monthly technology horizon sweep, or when a significant AI capability lands and frozen problems should be re-checked. Hebrew triggers: סריקת קו אופק, טכנולוגיה חדשה, ממתין לטכנולוגיה, בעיה קפואה, יכולת AI חדשה. Compares only against cards frozen for AI-maturity reasons — never a blanket re-scan."
metadata:
  stage: 01-מפעל-הבעיות
  sub_process: E
  mode: לפני
  raci: R
  status: קיים-בתיעוד
  version: 1.0.0
---

# סוכן סריקת-קו-אופק

## אחריות יחידה

לזהות יכולת AI חדשה, ולבדוק **ממוקד** אם היא פותחת בעיה שהוקפאה **בגלל AI** — לא בגלל דאטה או רגולציה.

## אופן פעולה וטריגר

**לפני.** Schedule חודשי; מפעיל טריגר קיים ("התפתחות טכנולוגית AI מהותית") בבקרת-העלות.

## תהליך

1. סרוק מקורות טכנולוגיים מוגדרים (Stanford AI Index, OECD.AI — מקור #27 ב[רשימה המורחבת](../../../07-נספחים/רשימת-מקורות-מורחבת.md))
2. זהה יכולת חדשה מהותית
3. **השוואה ממוקדת בלבד:** מול שדה **"חסמים טכנולוגיים"** של כרטיסים המתויגים "ממתינה לטכנולוגיה X" — ותו לא

```
⛔ לא כל כרטיס מושהה נבדק — רק אלה שהוקפאו בגלל בשלות AI.
   כרטיס שהוקפא בגלל דאטה או רגולציה אינו רלוונטי לסוכן הזה.
```

## פלט

| תוצאה | פעולה |
|---|---|
| אין התאמה | ללא פעולה |
| יש התאמה | זוג `(מזהה-כרטיס, מידע-חדש)` → [`pf-score-refresh`](../pf-score-refresh/SKILL.md) — **אותו פורמט בדיוק** כמו הפלט של [`pf-problem-classification`](../pf-problem-classification/SKILL.md) |

## גבולות — מה הסוכן לעולם לא עושה

- לא מריץ סריקה גורפת על כל הבעיות המושהות (FinOps)
- לא מנקד מחדש בעצמו — מעביר ל-[`pf-score-refresh`](../pf-score-refresh/SKILL.md)
- לא מחליט שבעיה "נפתחה" — רק מסמן התאמה לבדיקה

## שרשור

**לפניו:** [`pf-escalation-triggers`](../pf-escalation-triggers/SKILL.md) (טריגר 2 — הכרטיסים שתויגו "ממתין לטכנולוגיה X" הם בדיוק מרחב החיפוש של הסוכן הזה)
**אחריו:** [`pf-score-refresh`](../pf-score-refresh/SKILL.md)
**מזין גם:** [`pf-funnel-review`](../pf-funnel-review/SKILL.md) (רשימת בעיות בשלות לבדיקה חוזרת ברבעון)
**תיעוד:** [`pf-decision-logging`](../pf-decision-logging/SKILL.md)

## רקע בוויקי

[E-סריקת-קו-אופק](../../../08-ארכיטקטורת-המימוש/01-מפעל-הבעיות/E-סריקת-קו-אופק.md) · [טריגרים בבקרת-עלות](../../../01-מפעל-הבעיות/בקרת-עלות-והרצות-סוכני-AI.md#3-עדכון-לפי-trigger-event-driven)
