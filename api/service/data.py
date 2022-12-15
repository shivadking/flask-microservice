
from api.models.data import db, Datas

def get_all_data():
    return Datas.query.all()

def add_data(item_data):
    # Create new object
    new_item = Datas(data=item_data)

    # Save the data
    new_item.save()
    return new_item


def get_data_by_id(id):
    return Datas.get_by_id(id)

def delete_data_by_id(id):
     # Delete and save the change
    Datas.query.filter_by(id=id).delete()
    db.session.commit()