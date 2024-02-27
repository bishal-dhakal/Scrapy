import html
# from sqlalchemy import func
from fastapi import (
    HTTPException,
    status
)
import json
# from core.utils.constants import Message
import requests
import trending.Utils as Utils


# db = SessionLocal()

content_url = 'http://127.0.0.1:8000/api/v1/bot/content'

def postnews(content:json=None):
    try:
        header = content['title']
        # source_name = content['source_name']
        # source = db.query(ModelSource).filter(ModelSource.name == source_name).first()
        # content['source_id'] = source.id
        # content.pop('source_name')
        text= Utils.escape(header) 
        content['title'] = html.unescape(text)
        res = requests.post(content_url,json=content)

    #     if not content:
    #         print('No news content')
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST, detail=Message.INVALID_DATA
    #             )
        
    #     is_date_valid = utils.is_valid_date_format(str(content['published_date']))
    #     if not is_date_valid:
    #         print('Date is not Valid')
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail=Message.INVALID_DATE_FORMAT
    #             ) 

    #     does_content_exist = db.query(
    #             ModelContent
    #         ).filter(
    #             ModelContent.source_id==content['source_id'],
    #             ModelContent.title==html.unescape(content['title'])
    #         ).first()

    #     if does_content_exist:
    #         print('News already Exist')
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail=Message.DUPLICATE_DATA
    #             )
        
    #     if content['category_name']:
    #         category = db.query(
    #             ModelCategory
    #             ).filter(
    #             ModelCategory.name==content['category_name']
    #             ).first()
    #         if category is None:
    #             print('Category Does not Exist')
    #             raise HTTPException(
    #                 status_code=status.HTTP_400_BAD_REQUEST,
    #                 detail=Message.CATEGORY_DOES_NOT_EXIST
    #             )
    #     else:
    #         category = db.query(ModelCategory).filter(
    #         ModelCategory.name=="Other"
    #         ).first()

    #     # check does source exits
    #     is_source_valid = db.query(ModelSource).filter(ModelSource.id==content['source_id']).first()
    #     if is_source_valid is None:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="Invalide news source"
    #         )
    #     content_dict = content
        
    #     # data for database
    #     content_dict.pop('category_name')
    #     content_dict['category_id'] = category.id
    #     content_dict['title'] = html.unescape(content_dict['title'])
    #     content_modal_dict = ModelContent(**content_dict)
    #     db.add(content_modal_dict)
    #     db.commit()
    #     db.refresh(content_modal_dict)
    #     print(f"{content_dict['title']} added to the database")

    except Exception as e:
        print(e)


