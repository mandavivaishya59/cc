"""Create a Simple REST Service to demonstrate CRUD operations with "City”
database. Implement the service with fields viz. City_Name, District_Name,
Population. Deploy the service and execute the operations."""

from flask import  Flask , request , jsonify

app=Flask(__name__)

City=[{"id":1,"City_Name":"Mumbai","District_Name":"Palghar","Population":12345699},
          {"id":2,"City_Name":"Delhi","District_Name":"Noida","Population":99995699}]

@app.route("/city")
def city():
    return jsonify(City)

@app.route("/city" , methods=["POST"])
def city_add():
    data=request.json
    c={"id":len(City)+1,"City_Name":data["City_Name"],"District_Name":data["District_Name"],"Population":data["Population"]}
    City.append(c)
    return jsonify("Added")

@app.route("/city/<int:id>" , methods=["PUT"])
def city_up(id):
    data=request.json
    for c in City:
        if c["id"]==id:
            c.update(data)
        return jsonify("Updated")
    
@app.route("/city/<int:id>", methods=["DELETE"])
def city_del(id):
    for c in City:
        if c["id"]==id:
            City.remove(c)
        return jsonify("Deleted")
    
if __name__=="__main__":
    app.run(debug=True,port=1234)