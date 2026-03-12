from flask import  Flask , request , jsonify

app=Flask(__name__)

Employee=[{"id":1,"Employee_Name":"Shyam","age":24,"Phone_no":12345699,"Department":"CS"},
          {"id":2,"Employee_Name":"Ram","age":20,"Phone_no":99995699,"Department":"IT"}]

@app.route("/emp")
def emp():
    return jsonify(Employee)

@app.route("/emp" , methods=["POST"])
def emp_add():
    data=request.json
    e={"id":len(Employee)+1,"Employee_Name":data["Employee_Name"],"age":data["age"],"Phone_no":data["Phone_no"],"Department":data["Department"]}
    Employee.append(e)
    return jsonify("Added")

@app.route("/emp/<int:id>" , methods=["PUT"])
def emp_up(id):
    data=request.json
    for e in Employee:
        if e["id"]==id:
            e.update(data)
        return jsonify("Updated")
    
@app.route("/emp/<int:id>", methods=["DELETE"])
def emp_del(id):
    for e in Employee:
        if e["id"]==id:
            Employee.remove(e)
        return jsonify("Deleted")
    
if __name__=="__main__":
    app.run(debug=True,port=1234)