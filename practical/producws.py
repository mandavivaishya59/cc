from flask import Flask , request , jsonify

app=Flask(__name__)

product=[
    {'id':1,"Product_name":"Cosmatic" , "Quantity":'10' , "Expiry_date":'12/12/2026'},
    {'id':2,"Product_name":"Food" , "Quantity":'5' , "Expiry_date":'12/10/2025'},
    {'id':3,"Product_name":"Grocery" , "Quantity":'2' , "Expiry_date":'01/09/2024'},
]

@app.route("/product")
def get_product():
    return jsonify(product)

@app.route("/add_product",methods=["POST"])
def add_product():
    data=request.json
    pro={'id':len(product)+1,"Product_name":data["Product_name"] , "Quantity":data["Quantity"] , "Expiry_date":data["Expiry_date"]}
    product.append(pro)
    return jsonify({"Uploded " : pro})

@app.route("/update_product/<int:id>" ,methods=["PUT"])
def update_product(id):
    data=request.json
    for pro in product:
        if pro["id"]==id:
            pro.update(data)
            return jsonify({"Product updated successfully": pro})
    return jsonify({"Error": "Product not found"})
        
@app.route("/delete_product/<int:id>", methods=["DELETE"])
def del_product(id):
    for pro in product:
        if pro["id"] == id:
            product.remove(pro)
            return jsonify({"message": "Deleted successfully"})
    return jsonify({"message": "Product not found"})


if __name__=="__main__":
    app.run(debug=True , port= 2526)