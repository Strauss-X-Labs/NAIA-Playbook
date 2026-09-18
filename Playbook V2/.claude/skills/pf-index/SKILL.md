---
name: pf-index
description: "מפת-על ונקודת כניסה לכל סוכני מפעל הבעיות (Problem Factory) בכור ההאצה. Use this skill FIRST whenever the user asks about running, orchestrating, or choosing between Problem Factory agents, or asks a general question about the problem-intake pipeline without naming a specific step. Hebrew triggers: מפעל הבעיות, כור האצה, אילו סוכנים יש, איזה סוכן מתאים, הרצת הצינור, מפת סוכנים. Do NOT use for a task that clearly belongs to one named sub-agent — invoke that skill directly."
metadata:
  stage: 01-מפעל-הבעיות
  role: index
  version: 1.0.0
---

# מפעל הבעיות — מפת סוכנים ונקודת כניסה

מסמכי העיצוב המלאים: `08-ארכיטקטורת-המימוש/01-מפעל-הבעיות/`. הקובץ הזה הוא **הניתוב בלבד** — לא משכפל את התוכן.

## עקרונות-על שחלים על כל סוכן כאן

1. **SOLID** — אחריות יחידה לכל סוכן
2. **ברור ופשוט** — הפתרון הפשוט ביותר שעובד
3. **3 אופני פעולה**: לפני · במהלך · אחרי
4. **Human in the Loop תמיד** — סוכן מציע (R), אדם מחליט (A). **אין החלטה אוטונומית.**

## הצינור המלא

```
A. הזנה וסיווג      pf-source-scanning → pf-content-analysis → pf-problem-classification
B. תיעדוף וניקוד    pf-scoring-eligibility → pf-problem-scoring → pf-escalation-triggers → pf-approval-dossier
C. תיעדוף דינמי     pf-score-refresh (מריץ מחדש את B על כרטיס קיים)
D. Funnel Review    pf-funnel-review (רבעוני)
E. קו-אופק          pf-horizon-scanning → מזין את C
F. הרכבת צוות       pf-expert-suggestions
I. מי הבאה?         pf-next-candidate (התפנה Mission Lead) → מקדים את שער G
G. שער יציאה        pf-approval-dossier (ריצה 2) → pf-handoff-package

חוצה-הכל:  pf-decision-logging (אחרי כל החלטה) · pf-live-companion (סיוע בזמן אמת)
           pf-parameter-registry (H — כל ערך פרמטר נקרא ומשתנה דרכו)
```

## שתי פרדיגמות — חשוב להבין את ההבדל

| שאלה | סוכן | פרדיגמה |
|---|---|---|
| "מה הציון של הבעיה הזו?" | [`pf-problem-scoring`](../pf-problem-scoring/SKILL.md) | **דחיפה** — כרטיס בודד עולה |
| "האם המשפך בריא?" | [`pf-funnel-review`](../pf-funnel-review/SKILL.md) | תמונת-על רבעונית |
| **"מי הבעיה הבאה שנקדם?"** | [`pf-next-candidate`](../pf-next-candidate/SKILL.md) | **משיכה** — קיבולת התפנתה |

## טבלת בחירה מהירה

| צריך | סוכן | אופן |
|---|---|---|
| לסרוק מקור מידע חדש | [`pf-source-scanning`](../pf-source-scanning/SKILL.md) | לפני |
| לנתח פריט גולמי שנאסף | [`pf-content-analysis`](../pf-content-analysis/SKILL.md) | לפני |
| להחליט: בעיה חדשה או עדכון? | [`pf-problem-classification`](../pf-problem-classification/SKILL.md) | לפני |
| לבדוק אם כרטיס בשל לניקוד | [`pf-scoring-eligibility`](../pf-scoring-eligibility/SKILL.md) | לפני |
| לנקד בעיה (12 תתי-קריטריונים) | [`pf-problem-scoring`](../pf-problem-scoring/SKILL.md) | לפני |
| לקבוע רצועה + לזהות הסלמה | [`pf-escalation-triggers`](../pf-escalation-triggers/SKILL.md) | לפני |
| להכין תיק לאישור אנושי | [`pf-approval-dossier`](../pf-approval-dossier/SKILL.md) | לפני |
| לעדכן ציון של בעיה קיימת | [`pf-score-refresh`](../pf-score-refresh/SKILL.md) | לפני |
| להכין סקירה רבעונית | [`pf-funnel-review`](../pf-funnel-review/SKILL.md) | לפני |
| לבדוק אם טכנולוגיה חדשה פותחת בעיה קפואה | [`pf-horizon-scanning`](../pf-horizon-scanning/SKILL.md) | לפני |
| לתעד החלטה שהתקבלה | [`pf-decision-logging`](../pf-decision-logging/SKILL.md) | אחרי |
| לארוז תיק מסירה ל-Mission Lead | [`pf-handoff-package`](../pf-handoff-package/SKILL.md) | אחרי |
| לעזור לאדם בזמן ראיון/הכרעה | [`pf-live-companion`](../pf-live-companion/SKILL.md) | **במהלך** |
| להציע מומחי תוכן לצוות | [`pf-expert-suggestions`](../pf-expert-suggestions/SKILL.md) | לפני |
| **לדעת/לשנות ערך פרמטר** | [`pf-parameter-registry`](../pf-parameter-registry/SKILL.md) | לפני + אחרי |
| **"מי הבעיה הבאה?"** | [`pf-next-candidate`](../pf-next-candidate/SKILL.md) | לפני |

## ⚠️ שני פרמטרים שערכם טרם נקבע

לפני שמסתמכים על ציון, יש לדעת: **משקלות התיעדוף** ו**סף טריגר "פער בין קטגוריות"** טרם אושרו ע"י הנהלת המטה. כל ציון מחושב לפי ברירת מחדל **לדיון בלבד**, ויש לומר זאת במפורש. פרטים: [`pf-parameter-registry`](../pf-parameter-registry/SKILL.md).

## איפה הנתונים חיים

Playbook V2 = מתודולוגיה ניטרלית (סכמות/כללים). **הנתונים בפועל** חיים בספרייה האחות `כורי-בינה/<שם-הכור>/01-מפעל-הבעיות/`. אף סוכן לא כותב נתוני-כור לתוך Playbook V2.

## רקע בוויקי

[ארכיטקטורת המימוש — מפעל הבעיות](../../../08-ארכיטקטורת-המימוש/01-מפעל-הבעיות/README.md) · [מפת סוכנים](../../../08-ארכיטקטורת-המימוש/01-מפעל-הבעיות/מפת-סוכנים.md) · [הפרק במקור](../../../01-מפעל-הבעיות/README.md)
