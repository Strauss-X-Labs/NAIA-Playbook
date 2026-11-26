# שלב 3 · פיתוח

> הצוות מגדיר את מפת הדרכים המפורטת של המיזם ומתקדם מרעיון לביצוע מעשי ולהוכחת ערך מהירה (POV). בשלב זה מפותחת גרסת מוצר ראשונית (MVP) ונבחנת ההיתכנות הטכנולוגית והעסקית.

## מטרה

אחרי ש[הגדרת המיזם](../02-הגדרת-המיזם/README.md) הניבה בריף מיזם ושותף מקצועי, השלב הזה מתרגם את הרעיון למפת דרכים ממשית ולהוכחת ערך בשטח — לא רק על נייר. המתודולוגיה כאן ניטרלית-כלים: כל צוות ושותף מקצועי בוחר את השיטה הספציפית המתאימה למיזם (Design Thinking, Lean Startup וכו'), אך חמשת תתי-השלבים ותוצריהם מחייבים.

## מי אחראי על מה בשלב הזה

האחריות על **התהליך** נמצאת תמיד אצל המכון. האחריות על **הביצוע** תהיה אצל המכון או אצל השותף המקצועי, בהתאם לאופיו וליכולותיו. זו החלטת המכון, והיא [מוגדרת מראש עם בחירת השותף המקצועי](../02-הגדרת-המיזם/05-roadshow-ובחירת-שותפים.md#חלוקת-האחריות-בשלב-הפיתוח). גם כשהאחריות אצל המכון, הפיתוח עצמו נעשה בעזרת גורם חיצוני.

## תתי-השלבים

| תת-שלב | מטרה | תוצר | סוכנים |
|---|---|---|---|
| [בחירת הפתרון](01-בחירת-הפתרון.md) | סקירת פתרונות אפשריים, Startups וניתוח תקציב (Build/Buy/Partner), על בסיס ה-RFI מהגדרת המיזם | החלטת פתרון מתועדת ומנומקת | [`dv-solution-refresh`](../.claude/skills/dv-solution-refresh/SKILL.md) · [`dv-startup-scan`](../.claude/skills/dv-startup-scan/SKILL.md) · [`dv-budget-analysis`](../.claude/skills/dv-budget-analysis/SKILL.md) · [`dv-decision-drafting`](../.claude/skills/dv-decision-drafting/SKILL.md) |
| [עיצוב המוצר (Architecture & Product Design)](02-עיצוב-המוצר-וארכיטקטורה.md) | הגדרת שאלת ההיתכנות העסקית (MVP), בניית קונספט מוצרי מבוסס MVP עם הסתכלות על התמונה הכוללת (PMF) | קונספט מוצרי, ארכיטקטורה מאפשרת, הגדרת הטכנולוגיות בשימוש | [`dv-canvas-update`](../.claude/skills/dv-canvas-update/SKILL.md) · [`dv-concept-drafting`](../.claude/skills/dv-concept-drafting/SKILL.md) · [`dv-mvp-question-drafting`](../.claude/skills/dv-mvp-question-drafting/SKILL.md) · [`dv-mvp-question-check`](../.claude/skills/dv-mvp-question-check/SKILL.md) · [`dv-architecture-drafting`](../.claude/skills/dv-architecture-drafting/SKILL.md) · [`dv-architecture-review`](../.claude/skills/dv-architecture-review/SKILL.md) |
| [מפת הדרכים (Roadmap & GTM)](03-מפת-הדרכים-ו-gtm.md) | יצירת תוכנית עבודה רב-שלבית, מפורטת וישימה | מפת דרכים מלאה עם אבני דרך מוסכמות | [`dv-roadmap-drafting`](../.claude/skills/dv-roadmap-drafting/SKILL.md) · [`dv-roadmap-check`](../.claude/skills/dv-roadmap-check/SKILL.md) |
| [פיתוח ה-MVP](04-פיתוח-ה-mvp.md) | בנייה בפועל של גרסת ה-MVP בתכולה שנקבעה, והקמת סביבת ה-Test לניסוי | MVP עובד בסביבת Test, מוכן לניסוי | אין סוכני בנייה — הבנייה אנושית. מבנה הניסוי: [`dv-experiment-design`](../.claude/skills/dv-experiment-design/SKILL.md) · סטיות: [`dv-decision-drafting`](../.claude/skills/dv-decision-drafting/SKILL.md) |
| [הוכחת ערך (POV)](05-הוכחת-ערך-pov.md) | בחינת היתכנות מהירה של ליבת הפתרון בתכולה מינימלית | תשובה חיובית (או שלילית מוסברת) על שאלת ה-MVP | [`dv-experiment-design`](../.claude/skills/dv-experiment-design/SKILL.md) · [`dv-pov-dossier`](../.claude/skills/dv-pov-dossier/SKILL.md) |

כל הסוכנים מנסחים, מרכזים או בודקים — אף אחד מהם אינו מכריע ואינו כותב קוד. איך הם משתלבים: [ארכיטקטורת המימוש של שלב 3](../08-ארכיטקטורת-המימוש/03-mvp-poc/README.md).

לוח הזמנים והשערים המלאים: [gates-וזמנים.md](gates-וזמנים.md).

## עיקרון מרכזי: MVP הוא לא "גרסה חלקית" — הוא כלי לתשובה לשאלה אחת

> **MVP — המינימום הנדרש כדי שהמשתמש יגיד "WoW, כזה אני צריך".**

שאלת ה-MVP היא ההשערה הקריטית ביותר שעליה עומד או נופל המיזם. היא נגזרת מהיעד העסקי ומהבעיה שזוהתה בשלב החקר, ממוקדת ובדידה, בעלת קריטריון הכרעה ברור מראש, ובת-מענה בכמה שבועות. השרשרת המלאה: **שאלת ה-MVP (3.2) → [פיתוח גרסת MVP מינימלית](04-פיתוח-ה-mvp.md) (3.4) → הוכחת ערך (POV, 3.5)**.

## מעבר לשלב הבא

הוכחת ערך (POV) שעברה בהצלחה ואושרה — עוברת ל[יישום ופריסה: Production](../04-pmf-production-scale/01-production-mvp.md), ומשם ל-PMF ול-Scale. אם התשובה על שאלת ה-MVP שלילית, חוזרים לזיקוק הבעיה מחדש (ב[הגדרת המיזם](../02-הגדרת-המיזם/README.md)) או להגדרת הפתרון מחדש (בתוך שלב זה).

> אם המיזם כולל טרנספורמציה של מערכת ליבה טכנולוגית ותיקה (לא רק בניית מוצר דיגיטלי חדש) — ראו גם את הנספח [שיטת פיתוח אג'נטי ו-ADR](../05-שיטת-פיתוח-אגנטי-וadr/README.md), שמפרט את המתודולוגיה הטכנית המתאימה למקרה הזה.
