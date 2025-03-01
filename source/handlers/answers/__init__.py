from loguru import logger

from urllib.parse import urlparse
from datetime import datetime

from handlers.api_requests import url_analysis, sites_analysis, telegram_channels, article_analysis


country_codes = {'UA': '🇺🇦',
                'RU': '🇷🇺',
                'US': '🇺🇸',
                None: ''}

def flag_by_country(code: str):
    if code in country_codes:
        return country_codes[code]
    else:
        return country_codes[None]



@logger.catch
def url_analysis_answer(url: str, language: str):
    answer = ""
    
    request = url_analysis(url=url, language=language)
    logger.info(request)
    
    if not 'result' in request:
        answer = "no answer"
        return answer

    for key, value in request['result'].items():
        if value == 'None':
            continue
        if key == 'postAuthor':
            answer += '<b>Автор статті: </b>' + value + '\n'
        if key == 'postThesis':
            answer += '<b>Головний тезис: </b>' + value + '\n'
        if key == 'postSource':
            answer += '<b>Джерело новини: </b>' + value + '\n'
        if key == 'postEmotion':
            answer += '<b>Емоційне забарвлення: </b>' + value + '\n'
    
    return answer



@logger.catch
def article_analysis_answer(article: str, language: str):
    answer = ""
    
    request = article_analysis(article=article, language=language)
    logger.info(request)
    
    if not 'result' in request:
        answer = "no answer"
        return answer

    for key, value in request['result'].items():
        if value == 'None':
            continue
        if key == 'postAuthor':
            answer += '<b>Автор статті: </b>' + value + '\n'
        if key == 'postThesis':
            answer += '<b>Головний тезис: </b>' + value + '\n'
        if key == 'postSource':
            answer += '<b>Джерело новини: </b>' + value + '\n'
        if key == 'postEmotion':
            answer += '<b>Емоційне забарвлення: </b>' + value + '\n'
    
    return answer



@logger.catch
def sites_analysis_answer(query: str, language: str):
    answer = ""
    
    request = sites_analysis(query=query, language=language)
    logger.info(request)
    
    show_detailed = 5
    
    if 'result' in request:
        for info in request['result']:
            parsed_url = urlparse(info['url'])
            
            hyperlink = f"<a href='{info['url']}'>{parsed_url.netloc}</a>"
            
            if 'county_code' in info:
                country_code = flag_by_country(info['county_code'])
                answer += f"{ country_code }"

            if info['date'] and show_detailed > 0:
                
                if answer == "":
                    answer += "<b>Ймомовірне первинне джерело поширення:</b>\n"
                
                date_obj = datetime.strptime(info['date'], "%Y-%m-%d %H:%M:%S")
                date = date_obj.strftime("%Y-%m-%d")
                
                answer += f"{date} •"
            
            
            if show_detailed > 0 and not info['date']:
                show_detailed = 0;
                answer += f"\n<b>Згадки на сайтах:</b>\n"
                
            answer += f"{hyperlink}•"
                
            show_detailed -= 1

            if show_detailed > 0:
                answer += "\n"


        
    telegram_analysis_result = tg_channels_analysis_answer(query=query, language=language)
    if telegram_analysis_result != None:
        answer = f"{answer}\n{telegram_analysis_result}"

    return answer



@logger.catch
def tg_channels_analysis_answer(query: str, language: str):
    answer = ""
    
    request = telegram_channels(query=query, language=language)
    
    if not 'result' in request:
        answer = ""
        return answer
    
    telegram_search = request['result']
    
    to_show = 3
    
    for post_info in telegram_search:
        if to_show <= 0:
            break
        to_show -= 1
        
        if len(answer) > 500:
            break

        link = post_info['link']
        post_id = str(post_info['message_id'])
        date = post_info['date']
        
        parsed_url = urlparse(link)
        name = parsed_url.path
            
        answer += f"{date} • <a href='{link}'>{name}</a>  • <a href='{link + '/' + post_id}'>посилання</a> \n"
        
        logger.info(post_info)
        
    if answer != "":
        answer = f"\n<b>Згадки в телеграм каналах:</b>\n{answer}"
        
    return answer