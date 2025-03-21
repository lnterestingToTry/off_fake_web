from loguru import logger

from .helpers import count_words, check_link

from .api_requests import get_user
from .api_requests import add_new_domain
from .api_requests import get_requests
from .api_requests import count_requests_last_month

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
def get_answer(message:str):
    #tg_id = message.from_user.id
    #user_lang = get_user_lang(tg_id=tg_id)
    user_lang = default_lang
    text = message
    
    answer = {}
    
    is_link = check_link(text)
    
    user_requests = get_requests(num=10, query_type=2)
    user_requests_url = get_requests(num=10, query_type=0)
    
    count_requests = count_requests_last_month()
    logger.info(count_requests)
    
    answer['count_requests'] = count_requests['count']
    
    if user_requests['requests_list']:
        answer['user_requests'] = user_requests['requests_list']
        
    if user_requests_url['requests_list']:
        answer['user_requests_url'] = user_requests_url['requests_list']

    
    if is_link:
        answer['result'] = url_analysis_answer(url=text, language=user_lang)
        answer['type'] = 'url'
        
        add_new_domain(url=text)

    if count_words(text) < 20 and not is_link:
        answer['result'] = sites_analysis_answer(query=text, language=user_lang)
        logger.info(answer)
        if answer != None:
            tg_channels_analysis_answer_ = tg_channels_analysis_answer(query=text, language=user_lang)
            logger.info(tg_channels_analysis_answer_)
            if tg_channels_analysis_answer_ != None:
                answer['result'] += tg_channels_analysis_answer_
        else:
            answer['result'] = tg_channels_analysis_answer(query=text, language=user_lang)
        answer['type'] = 'sites'
    else:
        answer['result'] = article_analysis_answer(text, user_lang)
        answer['type'] = 'article'
    
    #logger.info(f"{answer}, {tg_id}, {text}, {answer}")

    return answer