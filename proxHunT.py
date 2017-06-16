#!/usr/bin/python

import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

banner = """
        >======>                                          >=>                          >======>    
        >=>    >=>       >=>>=>                           >=>             >=>>=>       >=>    >=>  
        >=>    >=>          >=>   >=>     >=>    >=>      >=> >=>     >=>    >=>       >=>    >=>  
        >> >==>           >=>      >=>   >=>   >=>  >=>   >=>  >=>   >=>   >=>         >> >==>      #proxHunT
        >=>  >=>             >=>    >=> >=>   >=>    >=>  >=>   >=> >=>       >=>      >=>  >=>    
        >=>    >=>            >=>    >=>=>     >=>  >=>   >=>    >=>=>         >=>     >=>    >=>  
        >=>      >=> >=> >====>       >=>        >=>     >==>     >=>     >====>   >=> >=>      >=>
                                                            fb : https://www.facebook.com/R.3volv3.R
"""

exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MjUgPSIxNTovLzM0LjU2LjQ4Igo5ID0gIjE1Oi8vMzQuNTYuNDgvP2M9JjZhPSY2Yj0xZCZhW109MiY2ZT0wIgoKNDYgMWEoNDcpOgoJNTAgPSA2OS40MSg2NCIoPzVlPDIyPihcZHsxLDN9XC4pezN9XGR7MSwzfVwuPylcNmQrKD81ZTwzZT5cZHsxLDV9KVw2ZCsoPzVlPDE1Plw2Mns0LDV9KSIpCgk1ZiA9IDE2LjJiKCkKCTVmLjcgKCIxOC4xOS4yZS4zNj0nNTklJyIpCgk1Zi40Mig0NykKCTQ5ID0gMjYoIjQ5LjI3IiwgIjYyIikKCTM5ID0gNWYuNjcoIi8zZC8xOS8yOFsxXS8yOFsyXS81MS80YyIpCgkzMiAyMiA0NCAzOS41YS4yYygiXDMxIilbMTA6XToKCQkxMiAiXDNmIiwyMgoJCTcxID0gNTAuMWUoMjIpLjFmKCIxNSIpKyAiOi8vIiArNTAuMWUoMjIpLjFmKCIyMiIpKyI6Iis1MC4xZSgyMikuMWYoIjNlIikrIlwzMSIKCQk0OS4yZig3MSkKCQllKC4zKQoJNDkuMjAoKQoJNWYuNTMoKQoKNDYgMTQoKToKCTQ5ID0gMjYgKCI0OS4yNyIsICI2NCIpLjU3ICgpCgk0NSA9IDE2LjJiICgpCgk0NS40MiAoIjE1Oi8vMzQuZi4zMy42OC9mIikKCTQ1LjcgKCIxOC4xOS4yZS4zNj0nNTklJyIpCgk0NS43ICgiNDMuM2MoMCwgNDApIikKCgkxNyA9IDQ1LjY3ICgnLy8qW0AyZD0iZi0zNyJdLzM4LzM1JykKCTE3LjYgKDQ5KQoJMTEgPSA0NS42NyAoJy8vKltAMmQ9ImYtMzctNmMiXS8yYScpCgkxMS42ICgxYi4xMykKCWUgKDEwKQoJYiA9IDQ1LjY3ICgnLy8qW0AyZD0iMWMtNGQiXS8yOFsxXS8yYScpCgliLjYgKDFiLjEzKQoJZSAoMzApCgk3MCA9IDQ1LjY3ICgnLzNkLzE5LzI4WzFdLzUwWzNdL2FbMl0nKQoJNzAuNiAoMWIuMTMpCgllICgyKQoJNWQgPSA0NS42NyAoJy8vKltAMmQ9IjIxLTYzLTVjIl0vYScpCgk1ZC42ICgxYi4xMykKCWUgKDIpCgk2NiA9IDQ1LjY3ICgnLy8qW0AyZD0iMjEtNjMtNTIiXScpCgoJOCA9IDY2LjI0ICgnNGYnKQoJNGEgPSAyNiAoJzRhLjI3JywgJzYyJykKCTMyIDcxIDQ0IDguMmMgKCJcMzEiKToKCQkxMiAiXDNmIiwgIjFkOi8vIiArIDcxCgkJZSguMykKCQk0YS4yZiAoIjFkOi8vIiArIDcxICsgIlwzMSIpCgk0YS4yMCAoKQoJNDUuMjAoKQoJMTIgIlwzMVsrXSAyMyA3MSA0ZSA0NCA6IDRhLjI3IFwzMSIKCgo1NCAzYSA9PSAnM2InOgoJNTQgNjAoMjkpICE9IDViOgoJCTU1KCJcMzFcM2ZcM2ZcM2ZcM2ZcM2Y8PCEgNjEnNmYgNGIgNjUgNTggIT4+XDMxIikKCTEyIDI5CgkxYSg5KQoJMTIgIlwzMVsrXSAxYyAzMiAyMyA3MSA6IC4uLi4uIgoJMTQoKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|send_keys|execute_script|result_working_proxy|url_high_anon_https|a|button_close_popup|c|d|sleep|checker|10|button_submit|print|RETURN|proxychecker|http|webdriver|text_area|document|body|getproxy|Keys|checking|HTTPS|match|group|close|checked|ip|working|get_attribute|url_all_proxy|open|txt|div|banner|button|Chrome|split|id|style|write|30|n|for|freeproxy|www|textarea|zoom|form|fieldset|page|__name__|__main__|scrollTo|html|port|t|40|compile|get|window|in|browser2|def|url|net|proxylist|working_proxy|TOUCH|tbody|modal|saved|value|p|table|input|quit|if|exit|freeproxylists|read|CODE|85|text|812|tab|button_toogle_https|P|browser|len|DON|w|https|r|MY|text_area_working_proxy|find_element_by_xpath|ru|re|pt|pr|toolbar|s|u|T|button_downlod_working_proxy|proxy".split("|")))








