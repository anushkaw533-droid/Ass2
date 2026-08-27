from flask import Flask
app=Flask(__name__)
@app.route('/order/<customer>/<product>/<int:quantity>/<int:price>')
def order(customer,product,quantity,price):
    total=quantity*price
    if total>10000:
        discount=total*0.15
    else:
        discount=0
    subtotal=total-discount
    gst=subtotal*0.18
    final_amount=subtotal+gst
    return f"""
<h1>ORDER SUMMARRY</h1>
<b>costomer name:</b>{customer}<br><br>
<b>product:</b>{product}<br><br>
<b>quantity:</b>{quantity}<br><br>
<b>price:</b>{price}<br><br>
<b>discount(15%):</b>{discount}<br><br>
<b>gst(%18):</b>{gst}<br><br>
<h2>final payable amount:{final_amount:2f}</h2>
"""
if __name__=="__main__":
    app.run(debug=True)
