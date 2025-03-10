from loguru import logger

from .helpers import count_words, check_link

from .api_requests import get_user
from .api_requests import add_new_domain

from .answers import url_analysis_answer, sites_analysis_answer, article_analysis_answer, tg_channels_analysis_answer


default_lang = 'ua'


@logger.catch
def get_user_lang(tg_id):
    request = get_user(tg_id=tg_id)
    
    if not 'user_dict' in request:
        return default_lang
    
    user_dict = request['user_dict']
    
    if user_dict['language']:
        return user_dict['language']


@logger.catch
async def get_answer(message:str):
    #tg_id = message.from_user.id
    #user_lang = get_user_lang(tg_id=tg_id)
    user_lang = default_lang
    text = message
    
    #answer = ""
    
    is_link = check_link(text)
    
    if is_link:
        answer = url_analysis_answer(url=text, language=user_lang)
        
        add_new_domain(url=text)

    if count_words(text) < 20 and not is_link:
        answer = sites_analysis_answer(query=text, language=user_lang)
        logger.info(answer)
        answer += tg_channels_analysis_answer(query=text, language=user_lang)
    else:
        answer = article_analysis_answer(text, user_lang)
        
    
    #logger.info(f"{answer}, {tg_id}, {text}, {answer}")
    
    return answer