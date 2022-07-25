# mutations.py
from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post

@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        today = date.today()
        post = Post(
            title=title, description=description, created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload


def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if not title or not description:
            raise ValueError("Missing some data...")
        if not post:
            raise Exception("Post not found")
        post.title = title
        post.description = description
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        if not post:
            raise Exception("Post not found")
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload