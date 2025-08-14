<<<<<<< HEAD
# 🛒 Flask Products API

A simple **Flask-based REST API** for managing products.  
Supports `GET`, `POST`, and filtering products by price.

---

## 🚀 Features
- Get all products
- Get single product by ID
- Filter products by minimum price
- Add new product (with authentication)

---

## 📦 Tech Stack
- Python 3.x
- Flask
- Postman (API testing)

---

## 📂 API Endpoints

### 1️⃣ Get all products
```http
GET /api/v1/products
# flask-product-api

###2️⃣ Get single product
```http
GET /api/v1/products/<id>

3️⃣ Add a new product
`http
POST /api/v1/products
Headers:
    Content-Type: application/json
    Authorization: Bearer mysecrettoken

Body:
{
  "name": "Headphones",
  "price": 2000
}

📥 Download & Import Postman Collection
You can directly import the Postman collection and test the API:
📦 Download Postman Collection.

🔹 Steps to Import in Postman:

Download the .json file from the above link.(https://github.com/Pratibha742/flask-product-api/raw/refs/heads/main/flask_products_api.postman_collection.json)

Open Postman → Click Import.

Select the file → Done ✅.

▶️ How to Run Locally
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/USERNAME/REPO-NAME.git

# 2. Navigate into the folder
cd REPO-NAME

# 3. Create virtual environment
python -m venv .venv

# 4. Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the server
python run.py







