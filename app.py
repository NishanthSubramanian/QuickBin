
# from flask import Flask, render_template, request, redirect, url_for
# import datetime
# import sqlite3 as sql
# import random
# app = Flask(__name__)


# @app.route('/')
# def hello():
#     # a = datetime.datetime.now()
#     # print(int(a.total_seconds()*1000))
#     return "<script>console.log(" + str(int(datetime.datetime.now().strftime("%s")) * 1000)  + ")</script>" + render_template('hello.html')


# @app.route('/enternew')
# def new_student():
#     return render_template('student.html')

# # Generate random URL using input

# # @app.route("/getTime", methods=['GET'])
# # def getTime():
# #     print("browser time: ", request.args.get("time"))
# #     print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
# #     return "Done"


# # 

# # @app.route('/editable')
# # def editable():
# #     return render_template("edit.html")
    

# # @app.route('/success/' + '<i>/' +'<rand>/'+'/edit')
# # def edit(i,rand):
# #     con = sql.connect("Hello.db")
# #     con.row_factory = sql.Row
# #     cur = con.cursor()
# #     # cur.execute("select * from students where pin=? ",
# #     #             ("success/" + name + "/" + paste + "/" + rand,))
# #     cur.execute("select * from students where name_id=? ",
# #                 (i,))


# #     rows = cur.fetchall()
# #     return render_template("edit.html", rows=rows)


# @app.route('/addrec', methods=['POST', 'GET'])
# def addrec():
#     if request.method == 'POST':
#         try:
#             nm = request.form['nm']
#             addr = request.form['add']
#             # r = request.form['exp']
#             rand = int(r)*1000*60
#             # rand = str(random.randint(0, 10000))
#             # paste=addr
#             # paste=addr.replace('\n','')
#             pin = "success/"
#             millis = int(round(time.time() * 1000))
#             # pin = "success/" + i + "/" + rand + "/"
#            #  pin = request.url
#             with sql.connect("Hello.db") as con:
#                 cur = con.cursor()

#                 cur.execute(
#                     "INSERT INTO students (name,addr,pin,time,expiry) VALUES (?,?,?)", (nm, addr, pin))
#                 con.commit()
#                 rand=str(rand)
#                 i=str(cur.lastrowid)
#                 cur.execute("UPDATE students SET pin = ? WHERE name_id = ?",("success/" + i + "/" + rand + "/",i))
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.rollback()
#             msg = "error in insert operation"

#         finally:
#             # return """<script>console.log("""+ i +""")</script>"""
#             # return redirect(url_for('success', name=nm, paste=addr, rand=rand, msg=msg))
#             return redirect(url_for('success',i=i,rand=rand,msg = msg))
#            #  return render_template("result.html",msg = msg)
#             con.close()


# @app.route(('/success/' + '<i>/' +'<rand>/'), methods=['POST', 'GET'])
# # @app.route(('/success/' + '<name>/' + '<paste>/' + '<rand>/'))
# # @app.route(('/<pin>'))
# # def success(name, paste, rand):
# # def success(pin):
# def success(i,rand):
#     con = sql.connect("Hello.db")
#     con.row_factory = sql.Row

#     cur = con.cursor()
#     # cur.execute("select * from students where pin=? ",
#     #             ("success/" + name + "/" + paste + "/" + rand,))
#     cur.execute("select * from students where name_id=? ",
#                 (i,))
#     rows = cur.fetchall()
#     return render_template("display.html", rows=rows)

# @app.route('/list')
# def list():
#     m = int(round(time.time() * 1000))-10000
#     con = sql.connect("Hello.db")
#     con.row_factory = sql.Row

#     cur = con.cursor()
#     cur.execute("DELETE FROM students WHERE time + expiry  <= ?",(m,))
#     cur.execute("select * from students")

#     rows = cur.fetchall()
#     return render_template("list.html", rows=rows)


# if __name__ == '__main__':
#     app.run(debug=True)








from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import random
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('index.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')

# Generate random URL using input


@app.route(('/success/' + '<i>/' +'<rand>/'), methods=['POST', 'GET'])
# @app.route(('/success/' + '<name>/' + '<paste>/' + '<rand>/'))
# @app.route(('/<pin>'))
# def success(name, paste, rand):
# def success(pin):
def success(i,rand):
    con = sql.connect("Hello.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    # cur.execute("select * from students where pin=? ",
    #             ("success/" + name + "/" + paste + "/" + rand,))
    cur.execute("select * from students where name_id=? ",
                (i,))
    rows = cur.fetchall()
    return render_template("display.html", rows=rows)

# @app.route('/editable')
# def editable():
#     return render_template("edit.html")
    

# @app.route('/success/' + '<i>/' +'<rand>/'+'/edit')
# def edit(i,rand):
#     con = sql.connect("Hello.db")
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     # cur.execute("select * from students where pin=? ",
#     #             ("success/" + name + "/" + paste + "/" + rand,))
#     cur.execute("select * from students where name_id=? ",
#                 (i,))


#     rows = cur.fetchall()
#     return render_template("edit.html", rows=rows)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            rand = str(random.randint(0, 10000))
            # paste=addr
            # paste=addr.replace('\n','')
            pin = "success/"
            # pin = "success/" + i + "/" + rand + "/"
           #  pin = request.url
            with sql.connect("Hello.db") as con:
                cur = con.cursor()

                cur.execute(
                    "INSERT INTO students (name,addr,pin) VALUES (?,?,?)", (nm, addr, pin))
                con.commit()
                i=str(cur.lastrowid)
                cur.execute("UPDATE students SET pin = ? WHERE name_id = ?",("success/" + i + "/" + rand + "/",i))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            # return """<script>console.log("""+ i +""")</script>"""
            # return redirect(url_for('success', name=nm, paste=addr, rand=rand, msg=msg))
            return redirect(url_for('success',i=i,rand=rand,msg = msg))
           #  return render_template("result.html",msg = msg)
            con.close()


@app.route('/list/')
def list():
    con = sql.connect("Hello.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
