---
name: pf-score-refresh
description: "מריץ מחדש את שרשרת הניקוד על כרטיס בעיה קיים כשמצטבר מידע חדש — לולאת התיעדוף הדינמי. Use when new information arrives for a problem already on the list, or on a periodic sweep of stale cards. Hebrew triggers: עדכון ציון, תיעדוף דינמי, מידע חדש לבעיה קיימת, לרענן ציון, בעיה שחוזרת. Receives an already-matched (card-id, new-info) pair — does not perform matching itself."
metadata:
  stage: 01-מפעל-הבעיות
  sub_process: C
  mode: לפני
  raci: R
  status: קיים-בתיעוד
  version: 1.0.0
---

# סוכן עדכון-ציון

## אחריות יחידה

להריץ מחדש את שרשרת B על כרטיס **קיים**, עם מידע חדש. לא לגלות בעיות חדשות, לא לשייך מידע לכרטיס.

## אופן פעולה וטריגר

**לפני.** שני מסלולים:
- **Event (עיקרי)** — זוג `(מזהה-כרטיס, מידע-חדש)` שהגיע מ-[`pf-problem-classification`](../pf-problem-classification/SKILL.md) או מ-[`pf-horizon-scanning`](../pf-horizon-scanning/SKILL.md)
- **Schedule (fallback בלבד)** — כרטיס שלא עודכן מעל סף-זמן מוגדר

> **FinOps:** הרצה גורפת שבועית על כל הכרטיסים היא בזבזנית. ברירת המחדל היא Event-driven ממוקד.

## חוזה הממשק — חשוב

הסוכן **מקבל** זוג `(מזהה-כרטיס, מידע-חדש)` **מוכן**. השיוך ("איזה כרטיס לעדכן") נפתר כבר ב-[`pf-problem-classification`](../pf-problem-classification/SKILL.md) — הסוכן הזה לא פותר שיוך בעצמו. זה מונע כפילות לוגיקה.

## תהליך

1. קבל את הזוג `(כרטיס, מידע-חדש)`. ⛔ כרטיס שמתויג "ממתינה להעמקה" (שלב: שערי סף) לא נכנס לשרשרת הניקוד — מעבירים אותו ל-[`pf-threshold-gate`](../pf-threshold-gate/SKILL.md), שמתחיל משער 0
2. הרץ מחדש: [`pf-scoring-eligibility`](../pf-scoring-eligibility/SKILL.md) → [`pf-problem-scoring`](../pf-problem-scoring/SKILL.md) → [`pf-escalation-triggers`](../pf-escalation-triggers/SKILL.md)
3. השווה לציון הקודם. ציון קודם לפי גרסה 1.0 (12 קריטריונים) — **אין השוואה ישירה**: מנקדים מחדש ושומרים את הציון הישן עם גרסתו

## פלט

| תוצאה | פעולה |
|---|---|
| ציון עלה מעל 4.0 | עדכון סטטוס במשפך; אם כבר היה בחקר מעמיק — יתכן שער-G חוזר |
| ציון שהיה מלא והפך לחלקי (ציון ריק) | תיוג "ממתינה להעמקה" (שלב: ניקוד חלקי) → [`pf-funnel-review`](../pf-funnel-review/SKILL.md) |
| ללא שינוי מהותי | ללא פעולה — רק תיעוד הריצה |

## גבולות — מה הסוכן לעולם לא עושה

- לא מבצע שיוך מידע-לכרטיס (זה [`pf-problem-classification`](../pf-problem-classification/SKILL.md))
- לא מוחק בעיות שירד ציונן — הן חוזרות למאגר עם תיוג סיבה
- **לא נוגע בשכבת הניהול** — החלטת מיקוד תחומי וג'וקר הן אנושיות לגמרי

## שכבת הניהול — מחוץ לתחום הסוכן

מעל המנגנון יושבת שכבה **אנושית לחלוטין**:
- **מיקוד תחומי** ("חודשיים על ביטחון לאומי") — מתועד, שקוף, **מוגבל בזמן**; אינו משנה ציונים, רק סדר עדיפויות
- **ג'וקר** — שימוש חוזר ב-[`pf-approval-dossier`](../pf-approval-dossier/SKILL.md) להכנת הבקשה

## שרשור

**לפניו:** [`pf-problem-classification`](../pf-problem-classification/SKILL.md) · [`pf-horizon-scanning`](../pf-horizon-scanning/SKILL.md)
**מעביר ל:** [`pf-threshold-gate`](../pf-threshold-gate/SKILL.md) (כרטיס שממתין בשערי הסף)
**משתמש ב:** [`pf-scoring-eligibility`](../pf-scoring-eligibility/SKILL.md) → [`pf-problem-scoring`](../pf-problem-scoring/SKILL.md) → [`pf-escalation-triggers`](../pf-escalation-triggers/SKILL.md)
**תיעוד:** [`pf-decision-logging`](../pf-decision-logging/SKILL.md)

## רקע בוויקי

[C-תיעדוף-דינמי](../../../08-ארכיטקטורת-המימוש/01-מפעל-הבעיות/C-תיעדוף-דינמי.md) · [ניהול-משפך-ותיעדוף-דינמי](../../../01-מפעל-הבעיות/ניהול-משפך-ותיעדוף-דינמי.md)
