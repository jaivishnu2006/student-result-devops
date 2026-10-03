from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []


@app.route("/")
def index():
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll_no = request.form["roll_no"]
        mark1 = int(request.form["mark1"])
        mark2 = int(request.form["mark2"])
        mark3 = int(request.form["mark3"])

        total = mark1 + mark2 + mark3
        percentage = total / 3
        result = "PASS" if percentage >= 40 else "FAIL"

        student = {
            "name": name,
            "roll_no": roll_no,
            "mark1": mark1,
            "mark2": mark2,
            "mark3": mark3,
            "total": total,
            "percentage": round(percentage, 2),
            "result": result
        }

        students.append(student)
        return redirect(url_for("index"))

    return render_template("add_student.html")


@app.route("/result/<roll_no>")
def result(roll_no):
    student = next(
        (student for student in students if student["roll_no"] == roll_no),
        None
    )
    return render_template("result.html", student=student)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
