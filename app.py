import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# مهم لتشفير الجلسة (session) - في الاستضافة الحقيقية حط متغير بيئة SECRET_KEY
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

# ------------------------------------------------------------
# بنك الأسئلة: كل سؤال عبارة عن dict فيه النص، الاختيارات، والإجابة الصحيحة
# ------------------------------------------------------------
QUESTIONS = [
    {
        "question": "ما هي وحدة قياس المقاومة الكهربائية؟",
        "options": ["فولت", "أمبير", "أوم", "واط"],
        "answer": "أوم",
    },
    {
        "question": "أي مما يلي يمثل قانون أوم؟",
        "options": ["V = I / R", "V = I x R", "I = V x R", "R = V x I"],
        "answer": "V = I x R",
    },
    {
        "question": "ما هو رمز العنصر 'المكثف' في الدوائر الكهربائية؟",
        "options": ["R", "L", "C", "D"],
        "answer": "C",
    },
    {
        "question": "عاصمة مصر هي؟",
        "options": ["الإسكندرية", "القاهرة", "الأقصر", "أسوان"],
        "answer": "القاهرة",
    },
]


@app.route("/", methods=["GET"])
def home():
    """صفحة البداية: تعرض ترحيب وزر بدء الاختبار"""
    return render_template("home.html", total=len(QUESTIONS))


@app.route("/start")
def start_quiz():
    """بداية الاختبار: تصفير النتيجة والانتقال للسؤال الأول"""
    session["score"] = 0
    session["current"] = 0
    return redirect(url_for("question"))


@app.route("/question", methods=["GET", "POST"])
def question():
    current = session.get("current", 0)

    # لو المستخدم بعت إجابة (POST) بنتأكد منها الأول
    if request.method == "POST":
        selected = request.form.get("option")
        correct_answer = QUESTIONS[current]["answer"]
        if selected == correct_answer:
            session["score"] = session.get("score", 0) + 1
        current += 1
        session["current"] = current

    # لو خلصنا كل الأسئلة، روح لصفحة النتيجة
    if current >= len(QUESTIONS):
        return redirect(url_for("result"))

    q = QUESTIONS[current]
    return render_template(
        "question.html",
        question=q["question"],
        options=q["options"],
        current=current + 1,
        total=len(QUESTIONS),
    )


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(QUESTIONS)
    return render_template("result.html", score=score, total=total)


if __name__ == "__main__":
    # للتشغيل محليًا: python app.py
    # على السيرفر، gunicorn هو اللي بيشغل التطبيق (شوف الـ Procfile)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
