# crud 
from flask import Flask,jsonify,request
from flask_restful import Api,Resource
from pymongo import MongoClient






app = Flask(__name__)
api =Api(app)
app.db= MongoClient("mongodb+srv://hritik:Hritik1234@cluster0.e9ya9.mongodb.net/test" )
app.collects=app.db.books
my_dict= dict()

class mymethod(Resource):
    def get(self):
        get_all = dict()
        my_listt =( list(app.collects.books.find({})))
        for i in my_listt:
            get_all[i["id"]]=i["name"]
        return jsonify(get_all)   

class addnew(Resource):
    def post(self,id ,name):
        app.collects.books.insert_one({"id":id,"name": name})
        my_listt =( list(app.collects.books.find({})))
        global my_dict
        
        for i in my_listt:
            my_dict[i["id"]]=i["name"]
        return jsonify(my_dict)         
        
        
        
        
        
    def put(self,id , name):
        updated =dict()
        filter = { 'id': id }
        newvalues = { "$set": { 'name': name } }
 

        app.collects.books.update_one(filter, newvalues)
        for i in app.collects.books.find({}):
            updated[i["id"]]= i["name"]
        return jsonify(updated)
        
        
        
       
            
class mydelete(Resource):
    def delete(self,id):
        remaing=dict()
        app.collects.books.delete_one({"id":id})
        for i in app.collects.books.find({}):
            remaing[i["id"]]= i["name"]
        return jsonify(remaing)    
                  
                    
    

api.add_resource(mymethod,"/books")
api.add_resource(addnew,"/new/<int:id>/<string:name>")
api.add_resource(mydelete , "/book/delete/<int:id>")
if __name__ == "__main__":
    app.run( debug=True)