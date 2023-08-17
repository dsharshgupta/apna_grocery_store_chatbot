from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Float
from fastapi import FastAPI, Request

app = FastAPI()

# Database setup
DATABASE_URL = "mysql://root:1234@localhost:3306/apna_grocery_code"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    user_id = Column(Integer)

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(String)
    category_selection = Column(Integer)
    rate = Column(Integer)
    user_id = Column(Integer)

# Function to query database for available categories
def get_available_categories():
    session = SessionLocal()
    categories = session.query(Category.name).all()
    session.close()
    return [category.name for category in categories]

# Function to query database for available products and their prices
def get_available_products():
    session = SessionLocal()
    products = session.query(Product.name, Product.rate).all()
    session.close()
    return [{"name": product.name, "price": product.rate} for product in products]

# Route for Dialogflow fulfillment
@app.post("/")
async def dialogflow_fulfillment(request: Request):
    data = await request.json()  # Extract JSON data from the request

    # Get the intent name from the request
    intent_name = data["queryResult"]["intent"]["displayName"]

    if intent_name == "Available categories":
        # Query your database for available categories
        categories = get_available_categories()

        # Construct the response message
        response_text = f"Available categories: {', '.join(categories)}"

        # Construct the Dialogflow fulfillment response
        fulfillment_response = {
            "fulfillmentText": response_text
        }

        return JSONResponse(content=fulfillment_response)

    elif intent_name == "available products":
        # Query your database for available products and their prices
        products = get_available_products()

        # Construct the response message
        response_text = "Available products:\n"
        for product in products:
            response_text += f"{product['name']} - Price: {product['price']} INR\n"

        # Construct the Dialogflow fulfillment response
        fulfillment_response = {
            "fulfillmentText": response_text
        }

        return JSONResponse(content=fulfillment_response)

    else:
        # Handle other intents
        fulfillment_response = {
            "fulfillmentText": "Sorry, I couldn't understand your request."
        }

        return JSONResponse(content=fulfillment_response)


    return JSONResponse(content=fulfillment_response)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)