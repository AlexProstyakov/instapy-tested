# imports
from instapy import InstaPy
from instapy import smart_run


# login credentials
insta_username = 'Akvaprint_almaty.kz'
insta_password = 'pilotpilot565'

comments = ['Таксопарк Bolt приглашает на работу от 20000 в день +7 700 246 05 84{}',
        'Таксопарк Bolt с бонусами до 80 000 тг в месяц +7 700 246 05 84{}',
        'Приглашаем на работу водителей в таксопарк Bolt Лучшие условия среди таксопарков + 7 700 246 05 84',
        'Такси Bolt - новый еро таксопарк до 500 000 тенге в месяц!',
        'Такси Болт - Самые высокие комиссии taxi-bolt.kz 2000 За регистрацию',
        'Таксопарк Болт - регистрируйтесь. Лучше Яндекс и Лидер такси! taxi-bolt.kz{}',
        'тоже так хочу{}',
        'можно и так{}',
        'как клево',
        'реально']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  #session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
  #                         style="FIFO",
  #                         unfollow_after=12 * 60 * 60, sleep_delay=601)
  session.unfollow_users(amount=250, nonFollowers=True, style="RANDOM", unfollow_after=426060, sleep_delay=60)
  session.unfollow_users(amount=60, instapy_followed_enabled=(True, "ALL"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
  session.like_by_tags(["работаастана"], amount=100)
  session.set_do_comment(enabled=True, percentage=25)
  session.set_comments(['Таксопарк Bolt приглашает на работу от 20000 в день +7 700 246 05 84','Таксопарк Bolt с бонусами до 80 000 тг в месяц +7 700 246 05 84','taxi_bolt_nursultan +7 700 246 50 84'])
  session.like_by_tags(["стиль"], amount=80)
  session.like_by_tags(["almaty_city"], amount=50)
  session.set_do_comment(enabled=True, percentage=50)
  session.set_comments(['Самый выгодный таксопарк Bolt EuroТакси +7 700 246 50 84','Приглашаем на работу водителей в таксопарк Bolt Лучшие условия среди таксопарков + 7 700 246 05 84','Таксопарк Bolt! Бонусы для водителей до 80 000 в месяц + 7 700 246 50 84'])
  session.follow_user_followers(['nursultan', 'astanacity', 'rabota_nursultan.kz'], amount=1000, randomize=False, interact=True)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments') 