from flask import Flask
app=Flask(__name__)
@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name,price,category):
    discount=price*0.10
    subtotal=price-discount
    gst=subtotal*0.18
    final_price=subtotal+gst
    return f"""
<h1>product information</h1>
<b>product name:</b>{product_name}<br><br>
<b>price:</b>{price}<br><br>
<b>category:</b>{category}<br><br>
<b>discount(10%):</b>{discount}<br><br>
<b>gst(%18):</b>{gst}<br><br>
<h2>final price:{final_price:2f}</h2>
"""
if __name__=="__main__":
    app.run(debug=True)
