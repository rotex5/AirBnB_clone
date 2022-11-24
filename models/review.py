#!/usr/bin/python3
""" `Review` class inherits from Base class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class
    """
    place_id = ""
    user_id = ""
    text = ""
