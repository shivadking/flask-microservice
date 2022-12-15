from flask_restx import Namespace, Resource, fields
from api.service.data import get_all_data, add_data, get_data_by_id, delete_data_by_id
from flask import request

rest_api = Namespace("data", description="Data related operations")


# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

"""
    Flask-Restx routes
"""

@rest_api.route('/')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        items = get_all_data()
        
        return {"success" : True,
                "msg"     : "Items found ("+ str(len( items ))+")",
                "datas"   : str( items ) }, 200

    """
       Create new item
    """
    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the information    
        item_data = req_data.get("data")

        new_item = add_data(item_data)
        
        return {"success": True,
                "msg"    : "Item successfully created ["+ str(new_item.id)+"]"}, 200

@rest_api.route('/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        item = get_data_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.toJSON()}, 200

    """
       Update Item
    """
    @rest_api.expect(update_model, validate=True)
    def put(self, id):

        item = get_data_by_id(id)

        # Read ALL input from body  
        req_data = request.get_json()

        # Get the information    
        item_data = req_data.get("data")

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        item.update_data(item_data)
        item.save()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully updated",
                "data"    :  item.toJSON()}, 200 

    """
       Delete Item
    """
    def delete(self, id):

        # Locate the Item
        item = get_data_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        delete_data_by_id(id)

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully deleted"}, 200   