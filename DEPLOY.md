# موقع الأسئلة - تعليمات النشر

## الملفات
```
quiz_site/
├── app.py
├── requirements.txt
├── Procfile
└── templates/
    ├── base.html
    ├── home.html
    ├── question.html
    └── result.html
```

## التشغيل محليًا
```bash
pip install -r requirements.txt
python app.py
```
افتح المتصفح على: http://127.0.0.1:5000

---

## النشر على Render.com (مجاني - موصى به)

1. اعمل حساب على github.com (لو مش عندك) وارفع مجلد المشروع كامل كـ repository جديد.
2. سجّل دخول على render.com بحساب GitHub.
3. من الداشبورد: New + → Web Service.
4. اختر الـ repository بتاعك.
5. الإعدادات:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. تحت "Environment Variables" ضيف متغير:
   - `SECRET_KEY` = أي نص عشوائي طويل (مثلاً استخدم موقع لتوليد مفاتيح عشوائية)
7. اضغط Create Web Service. بعد دقيقتين هيديك رابط زي:
   `https://your-app-name.onrender.com`

---

## النشر على PythonAnywhere (بديل بدون GitHub)

1. اعمل حساب مجاني على pythonanywhere.com.
2. من تبويب Files: ارفع كل الملفات (app.py, requirements.txt, ومجلد templates).
3. من تبويب Consoles، افتح Bash console ونفّذ:
   ```bash
   pip install --user flask
   ```
4. من تبويب Web: Add a new web app → Flask → اختر مسار app.py بتاعك.
5. عدّل مسار الـ working directory ليطابق مكان الملفات اللي رفعتها.
6. اضغط Reload، وهيديك رابط زي:
   `https://yourusername.pythonanywhere.com`

---

## ملاحظات مهمة قبل النشر
- **debug=True** مناسب للتجربة محليًا بس. في مشروع حقيقي يفضل يبقى `False` أو تشيله خالص لما تنشر.
- لازم تحط `SECRET_KEY` كمتغير بيئة حقيقي في الاستضافة (مش تسيبه القيمة الافتراضية).
- لو عايز تضيف أسئلة أكتر، عدّل قائمة `QUESTIONS` في `app.py`.
