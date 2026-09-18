---
name: md-index
description: "מפת-על ונקודת כניסה לכל סוכני שלב הגדרת המיזם (Mission Definition) בכור ההאצה. Use FIRST when asked about running or choosing between stage-02 agents, or about the workshop-based process in general. Hebrew triggers: הגדרת המיזם, שלב 2, סדנאות, Mission Squad, איזה סוכן בסדנה, מפת סוכנים שלב 2. Do NOT use when the task clearly belongs to one named agent — invoke that one directly."
metadata:
  archetype: מצביע
  stage: 02-הגדרת-המיזם
  role: index
  version: 2.0.0
---

# הגדרת המיזם — מפת סוכנים ונקודת כניסה

מסמכי העיצוב: `08-ארכיטקטורת-המימוש/02-הגדרת-המיזם/`. הקובץ הזה מנתב בלבד.

## ⚠️ זה שלב אחר מפרק 1

| | 01 · מפעל הבעיות | **02 · הגדרת המיזם** |
|---|---|---|
| האופי | **מכונה** — רצה תמיד | **פרויקט** — פעם אחת, התחלה וסוף |
| מה מפעיל | Schedule / Trigger | **אבן-דרך אנושית** |
| מרכז הכובד | הסוכנים | **הסדנאות והאנשים** |

## ארבעה מצבי פעולה — לא שלושה

| מצב | מתי | מי |
|---|---|---|
| 🔵 **לפני** | לפני הסדנה | [`md-session-prep`](../md-session-prep/SKILL.md) · המאמתים · [`md-canvas-prefill`](../md-canvas-prefill/SKILL.md) · [`md-partner-mapping`](../md-partner-mapping/SKILL.md) |
| 🟡 **הנחיה** | תוך כדי הדיון — **תהליך בלבד** | [`md-diverge-facilitator`](../md-diverge-facilitator/SKILL.md) · [`md-inquiry-facilitator`](../md-inquiry-facilitator/SKILL.md) · [`md-converge-facilitator`](../md-converge-facilitator/SKILL.md) |
| 🟢 **משוב על תוצר** | אחרי שהקבוצה סיימה — **מעוגן בראיה** | [`md-output-review`](../md-output-review/SKILL.md) |
| 🟣 **אחרי** | אחרי יום הפעילות | [`md-session-capture`](../md-session-capture/SKILL.md) · המנסחים · [`md-rfi-intake`](../md-rfi-intake/SKILL.md) · [`md-budget-analysis`](../md-budget-analysis/SKILL.md) |

## ⛔ החוזה שכולם כפופים לו

> **הסוכן פועל על ה*תהליך*. הקבוצה מחזיקה את ה*תוכן*.**

שני כללים שמחזיקים את כל השאר:
- **כלל הדיבור הראשון** — הסוכן לעולם לא מדבר ראשון על שאלה חדשה
- **כלל השתיקה** — שתיקה בחדר שייכת לקבוצה

הפירוט המלא: [חוזה ההנחיה](../../../08-ארכיטקטורת-המימוש/02-הגדרת-המיזם/חוזה-ההנחיה.md).

## ⛔ החוזה התפעולי — מה כל סקיל חייב להכיל

כל סוכן כאן נגזר מ[חוזה הסוכן](../../../08-ארכיטקטורת-המימוש/00-חוזה-הסוכן.md): **אחריות · טריגר · קלט · תנאי כניסה · אלגוריתם · פלט · גבולות · שרשור**.

**הקלט הוא שלוש עמודות:** חובה (חוסר = עצירה) · רשות (חוסר = מדווח) · ידע (קישור לפרקים 00-07, לעולם לא העתקה).

## ⭐ כרטיס המיזם הוא הקלט של כולם

⬜ ה-**Mission Lead** פותח [כרטיס מיזם](../../../06-כלים-ותבניות/כרטיס-מיזם-תבנית.md) כפעולתו הראשונה בשלב. **לבעיה אחת יכולים להיות כמה מיזמים.**

> ⛔ **בלי כרטיס מיזם פתוח, אף סוכן בשלב אינו רץ.** *(התגלה ב[סבב 3](../../../../כורי-בינה/כור-מעבדה/02-הגדרת-המיזם/דוח-סבב-3.md) — בסבב 2 השלב רץ ישירות על כרטיס הבעיה, ואיש לא שם לב)*

## ⚠️ לצוות המיישם — לא לכולם יש "כפתור הרץ"

| ארכיטיפ | סוכנים | יש מסך עם הרצה ותוצר? |
|---|---|---|
| 🔍 חקר · ✅ בדיקה · ✍️ ניסוח · 📊 ריכוז | רוב הסוכנים | ✅ כן — תוצר MD לפי תבנית בפרק 06 |
| 🎙️ **הנחיה** | 3 המנחים · `md-output-review` | ❌ **לא.** פועלים בזמן אמת מול חדר · הפלט הוא תרומות ליומן |
| 🔗 **מצביע** | `index` · `parameter-registry` · `decision-logging` · `expert-suggestions` | ❌ **לא.** מפנים ללוגיקה שחיה במקום אחר |

## טבלת בחירה מהירה

| צריך | סוכן |
|---|---|
| להכין חומר לפני סדנה | [`md-session-prep`](../md-session-prep/SKILL.md) |
| להנחות סיעור מוחות / Diverge | [`md-diverge-facilitator`](../md-diverge-facilitator/SKILL.md) |
| להנחות Five Whys / עץ בעיות | [`md-inquiry-facilitator`](../md-inquiry-facilitator/SKILL.md) |
| להנחות קיבוץ / בחירה / הצבעה | [`md-converge-facilitator`](../md-converge-facilitator/SKILL.md) |
| לתת משוב על תוצר של הקבוצה | [`md-output-review`](../md-output-review/SKILL.md) |
| לתעד את מה שקרה בחדר | [`md-session-capture`](../md-session-capture/SKILL.md) |
| לבדוק זמינות דאטה | [`md-data-validation`](../md-data-validation/SKILL.md) |
| לבדוק אם AI מתאים | [`md-ai-fit`](../md-ai-fit/SKILL.md) |
| לבדוק סיבתיות ומנוף של שורש | [`md-evidence-validation`](../md-evidence-validation/SKILL.md) |
| לבדוק מה נוסה בעולם | [`md-market-scan`](../md-market-scan/SKILL.md) |
| לנסח מסמך פנימי | [`md-document-drafting`](../md-document-drafting/SKILL.md) |
| לנסח בריף לשותפים | [`md-brief-drafting`](../md-brief-drafting/SKILL.md) ⚠️ חיצוני |
| למלא Lean Canvas | [`md-canvas-prefill`](../md-canvas-prefill/SKILL.md) |
| למזג קנבסים | [`md-canvas-merge`](../md-canvas-merge/SKILL.md) 🔶 |
| RFI על **הבעיה** | [`md-rfi-problem`](../md-rfi-problem/SKILL.md) ⚠️ חיצוני |
| RFI על **הפתרון** | [`md-rfi-solutions`](../md-rfi-solutions/SKILL.md) ⚠️ חיצוני |
| לרכז מענים | [`md-rfi-intake`](../md-rfi-intake/SKILL.md) |
| טווח תקציב / Build-Buy-Partner | [`md-budget-analysis`](../md-budget-analysis/SKILL.md) |
| למפות מועמדים לשותף | [`md-partner-mapping`](../md-partner-mapping/SKILL.md) |
| אין שותף — לסגור בכבוד | [`md-return-to-factory`](../md-return-to-factory/SKILL.md) |
| ערך פרמטר | [`md-parameter-registry`](../md-parameter-registry/SKILL.md) |
| לתעד החלטה | [`md-decision-logging`](../md-decision-logging/SKILL.md) |
| לפתוח כרטיס מיזם | ⬜ **אנושי** — [תבנית](../../../06-כלים-ותבניות/כרטיס-מיזם-תבנית.md) |
| להרכיב Mission Squad | [`md-expert-suggestions`](../md-expert-suggestions/SKILL.md) |

## ⬜ איפה אין AI כלל — וזו החלטה

- **שיחות ה-Roadshow** — משא ומתן ואמון אנושי
- **"הכרטיס האחד"** ברעיונאות — 2 דקות, אדם מציג
- **הכתיבה השקטה** — כל הסוכנים מושתקים
- פרסום RFI · חתימת שותף

## 🔶 שתי הכרעות באחריות הצוות

1. **מנגנון מיזוג הקנבסים** → [`md-canvas-merge`](../md-canvas-merge/SKILL.md) פועל במצב מוגבל
2. **מה נקלט מסדנה** (צילום? תמלול? מי מזין?) → [`md-session-capture`](../md-session-capture/SKILL.md) ממתין

## ⚠️ שני פרמטרים שלא הוגדרו — וחוסמים את תתי-שלבים 4-5

**חלון מענה ל-RFI הפתרונות** (תת-שלב 4) · **סף כישלון Roadshow** (תת-שלב 5). **אל תמציא ערך** — ראו [`md-parameter-registry`](../md-parameter-registry/SKILL.md).

> `md-rfi-solutions` **עוצר** בתנאי הכניסה כל עוד חלון המענה לא נקבע. זו הסיבה המעשית שחצי השלב השני מעולם לא הורץ בכור-מעבדה.
> *(שער האישור לפלט חיצוני — הפרמטר השלישי שהופיע כאן — **הוגדר 31.08.2026**.)*

## גבולות

- **מנתב בלבד** — אינו מבצע אף משימה של סוכן אחר
- **אינו משכפל לוגיקה** — כל ערך, כלל והגדרה חיים בקובץ שאליו הוא מפנה
- אינו מכריע בין סוכנים כשהמשימה ברורה — אז פונים ישירות לסוכן

## רקע בוויקי

[ארכיטקטורת המימוש — הגדרת המיזם](../../../08-ארכיטקטורת-המימוש/02-הגדרת-המיזם/README.md) · [חוזה ההנחיה](../../../08-ארכיטקטורת-המימוש/02-הגדרת-המיזם/חוזה-ההנחיה.md) · [מפת נגיעות ה-AI](../../../08-ארכיטקטורת-המימוש/02-הגדרת-המיזם/מפת-נגיעות-ai.md) · [הפרק במקור](../../../02-הגדרת-המיזם/README.md)
