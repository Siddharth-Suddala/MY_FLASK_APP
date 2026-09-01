# from flask import Flask, request
# import requests
# from currency_converter import CurrencyConverter
# import locale
# import json
# app = Flask(__name__)

# # @app.route("/weather", methods=["GET"])
# # def gettempandplace():
# #     latitude = request.args.get("latitude")
# #     longitude = request.args.get("longitude")


# #     if not latitude or not longitude:
# #         return {"error": "Latitude and longitude are required"}, 400

# #     data = requests.get(
# #         f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=036b831f6694771c7bcfa7dbfd09dcb4"
# #     ).json()

# #     return {
# #         "name": data['name'],
# #         "temperature": round(data["main"]["temp"] - 273.15, 2)
# #     }

# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0", port=5000, debug=True)

# # @app.route("/")
# # def currency_converter():
# #     amount = int(request.args.get("amount"))

# #     current_currency = request.args.get("currentcurrency")

# #     destination_currency = request.args.get("destinationcurrency")

# #     c = CurrencyConverter()

# #     converted_amt = c.convert(amount,current_currency,destination_currency)

# #     return f"{converted_amt:,}"

# # if __name__ == "__main__":
# #      app.run(debug=True)

# @app.get("/")
# def handle_home():
#     return "This is the home route!"

# # @app.get("/students/<student_name>")
# # def handle_students(student_name):
# #     return {
# #         "name" : student_name,
# #         "usn" : "007"
# #     }

# # @app.get("/students/<student_name>/fav-food")
# # def handle_food(student_name):
# #     return ["Biriyani","Noodles"]

# # @app.route("/<category>")
# # @app.route("/<category>/<n>")
# # def get_category_items(category, n=None):

# #     itemlist = []

# #     with open("./MOCK_DATA.json") as f:
# #         data = json.load(f)

# #     if n is not None:
# #         count = int(n)

# #         for i in data:
# #             if count == 0:
# #                 break

# #             if i['product_category'] == category:
# #                 itemlist.append(i)
# #                 count -= 1

# #     else:
# #         for i in data:
# #             if i['product_category'] == category:
# #                 itemlist.append(i)

# #     return itemlist


# # if __name__ == "__main__":
# #     app.run(debug=True)

# # app=Flask(__name__)       
# # @app.get("/<p>")
# # def products(p):
# #     res=requests.get("https://dummyjson.com/products")
# #     data=res.json()
# #     ans=[]
# #     for i in data['products']:
# #         if i["category"]==p:
# #             ans.append(i)
# #     return ans
# # if __name__=="__main__":
# #     app.run(debug=True)


# app=Flask(__name__)
# @app.get("/")
# def home():
#     res=requests.get("https://dummyjson.com/products")
#     return res.json()       
# @app.get("/<p>/<rating>")
# def products(p,rating):
#     res=requests.get("https://dummyjson.com/products")
#     data=res.json()
#     ans=list(filter(lambda x:x['category']==p and int(rating)>=x["reviews"][0]["rating"],data['products']))
#     return ans
# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask

from user_bp import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

@app.route("/test")
def handle_home():
    return "HELLO from Test!"

if __name__ == "__main__":
    app.run(debug=True)
