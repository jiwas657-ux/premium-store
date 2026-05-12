from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Smart LED Lamp",
        "price": 49,
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
        "description": "Modern smart LED lamp with adjustable brightness."
    },
    {
        "id": 2,
        "name": "Wireless Earbuds",
        "price": 79,
        "image": "https://images.unsplash.com/photo-1583394838336-acd977736f90",
        "description": "Premium sound quality with noise cancellation."
    },
    {
        "id": 3,
        "name": "Portable Blender",
        "price": 39,
        "image": "https://images.unsplash.com/photo-1570222094114-d054a817e56b",
        "description": "USB rechargeable blender for smoothies anywhere."
    }
]

base_css = """
<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#fff;
    color:#111;
}

header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 60px;
    border-bottom:1px solid #eee;
    position:sticky;
    top:0;
    background:white;
    z-index:1000;
}

.logo{
    font-size:24px;
    font-weight:bold;
}

nav a{
    margin-left:20px;
    text-decoration:none;
    color:#111;
    font-weight:500;
}

.hero{
    height:85vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:40px;
    background:linear-gradient(to right,#f7f7f7,#ffffff);
}

.hero h1{
    font-size:4rem;
    margin-bottom:20px;
}

.hero p{
    color:#555;
    margin-bottom:30px;
    font-size:1.2rem;
}

.btn{
    display:inline-block;
    padding:14px 28px;
    background:black;
    color:white;
    text-decoration:none;
    border-radius:10px;
    transition:0.3s;
}

.btn:hover{
    opacity:0.8;
}

.section{
    padding:70px 60px;
}

.section-title{
    font-size:2.5rem;
    margin-bottom:40px;
    text-align:center;
}

.products-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:30px;
}

.product-card{
    border:1px solid #eee;
    border-radius:20px;
    overflow:hidden;
    transition:0.3s;
    background:white;
}

.product-card:hover{
    transform:translateY(-8px);
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
}

.product-card img{
    width:100%;
    height:260px;
    object-fit:cover;
}

.product-card-content{
    padding:20px;
}

.product-card h3{
    margin-bottom:10px;
}

.price{
    font-size:1.3rem;
    margin-bottom:20px;
    font-weight:bold;
}

.single-product{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    padding:80px 60px;
}

.single-product img{
    width:100%;
    border-radius:20px;
}

.single-product h1{
    font-size:3rem;
    margin-bottom:20px;
}

.single-product p{
    margin:20px 0;
    color:#555;
    line-height:1.8;
}

.benefits{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:30px;
}

.benefit-card{
    padding:40px;
    background:#f7f7f7;
    border-radius:20px;
    text-align:center;
}

footer{
    padding:40px;
    text-align:center;
    border-top:1px solid #eee;
    margin-top:80px;
}

.contact-form{
    max-width:600px;
    margin:auto;
    display:flex;
    flex-direction:column;
    gap:20px;
}

.contact-form input,
.contact-form textarea{
    padding:16px;
    border:1px solid #ddd;
    border-radius:10px;
}

.contact-form textarea{
    height:150px;
}

@media(max-width:768px){

    header{
        flex-direction:column;
        gap:20px;
    }

    .hero h1{
        font-size:2.5rem;
    }

    .single-product{
        grid-template-columns:1fr;
    }

}
</style>
"""

@app.route("/")
def home():

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Premium Store</title>
        {base_css}
    </head>
    <body>

    <header>
        <div class='logo'>PREMIUM STORE</div>

        <nav>
            <a href='/'>Home</a>
            <a href='/shop'>Shop</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
    </header>

    <section class='hero'>
        <div>
            <h1>Modern Products For Everyday Life</h1>
            <p>Premium trending products sourced globally.</p>
            <a href='/shop' class='btn'>Shop Now</a>
        </div>
    </section>

    <section class='section'>
        <h2 class='section-title'>Featured Products</h2>

        <div class='products-grid'>
    """

    for product in products:
        html += f"""
        <div class='product-card'>
            <img src='{product["image"]}'>
            <div class='product-card-content'>
                <h3>{product["name"]}</h3>
                <div class='price'>£{product["price"]}</div>
                <a class='btn' href='/product/{product["id"]}'>View Product</a>
            </div>
        </div>
        """

    html += """
        </div>
    </section>

    <section class='section'>
        <h2 class='section-title'>Why Choose Us</h2>

        <div class='benefits'>

            <div class='benefit-card'>
                <h3>Fast UK Shipping</h3>
                <p>Reliable delivery across the UK.</p>
            </div>

            <div class='benefit-card'>
                <h3>Premium Quality</h3>
                <p>Carefully sourced trending products.</p>
            </div>

            <div class='benefit-card'>
                <h3>Secure Payments</h3>
                <p>100% protected checkout process.</p>
            </div>

        </div>
    </section>

    <footer>
        <p>© 2026 Premium Store. All rights reserved.</p>
    </footer>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/shop")
def shop():

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shop</title>
        {base_css}
    </head>
    <body>

    <header>
        <div class='logo'>PREMIUM STORE</div>

        <nav>
            <a href='/'>Home</a>
            <a href='/shop'>Shop</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
    </header>

    <section class='section'>
        <h1 class='section-title'>Shop Products</h1>

        <div class='products-grid'>
    """

    for product in products:
        html += f"""
        <div class='product-card'>
            <img src='{product["image"]}'>
            <div class='product-card-content'>
                <h3>{product["name"]}</h3>
                <div class='price'>£{product["price"]}</div>
                <a class='btn' href='/product/{product["id"]}'>View Product</a>
            </div>
        </div>
        """

    html += """
        </div>
    </section>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/product/<int:id>")
def product(id):

    product = next((p for p in products if p["id"] == id), None)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{product['name']}</title>
        {base_css}
    </head>
    <body>

    <header>
        <div class='logo'>PREMIUM STORE</div>

        <nav>
            <a href='/'>Home</a>
            <a href='/shop'>Shop</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
    </header>

    <section class='single-product'>

        <img src='{product["image"]}'>

        <div>
            <h1>{product["name"]}</h1>

            <div class='price'>£{product["price"]}</div>

            <p>{product["description"]}</p>

            <a href='#' class='btn'>Add To Cart</a>
        </div>

    </section>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/about")
def about():

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About</title>
        {base_css}
    </head>
    <body>

    <header>
        <div class='logo'>PREMIUM STORE</div>

        <nav>
            <a href='/'>Home</a>
            <a href='/shop'>Shop</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
    </header>

    <section class='section'>

        <h1 class='section-title'>About Us</h1>

        <p style='max-width:800px;margin:auto;text-align:center;line-height:2;color:#555;'>
        We source premium trending products globally and deliver
        modern ecommerce experiences to customers across the UK.
        Our mission is to provide affordable innovation with premium quality.
        </p>

    </section>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/contact")
def contact():

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact</title>
        {base_css}
    </head>
    <body>

    <header>
        <div class='logo'>PREMIUM STORE</div>

        <nav>
            <a href='/'>Home</a>
            <a href='/shop'>Shop</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
    </header>

    <section class='section'>

        <h1 class='section-title'>Contact Us</h1>

        <form class='contact-form'>

            <input type='text' placeholder='Your Name'>

            <input type='email' placeholder='Your Email'>

            <textarea placeholder='Your Message'></textarea>

            <button class='btn'>Send Message</button>

        </form>

    </section>

    </body>
    </html>
    """

    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=False)
