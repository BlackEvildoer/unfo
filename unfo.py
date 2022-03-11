import requests
import json
from time import sleep
import os
import colorama
import pyfiglet
from user_agent import generate_user_agent
from colorama import Style, Fore, Back
colorama.init()
import time
A = "\033[1;91m"#الاحمر
B = "\033[1;90m"#الرصاصي
C = "\033[1;97m"#الابيض
E = "\033[1;92m"#الاخضر
H = "\033[1;93m"#الاصفر
K = "\033[1;94m"#البنفسجي
L = "\033[1;95m"#وردي
M = "\033[1;96m"#السمائي
r = requests.session()
a = 0 
z = 0
t = 0 
L20 =f"""
{M} __{C}__ __________   _____      ._{M}_{C}  .__                 
{M}| {C}   |   \      {M}\_/{C} ____\__{M}__{C} |  | |  |   ______  _  __
|    |  {C} /   |   \   {M}__\{C}/  _ \|  | |  |  /  _ \ \/ {M}\/ /{C}
|    |  /    |    \  | {M}(  {C}<_> {M}) {C} |_|  |_(  <_> )     / 
{M}|____{C}__/\____|__  /__|  \____/|____/___{M}_/\{C}____/ \/{M}\_/  
                {M}\/ 
                
\033[1;93m < \033[1;92mTHIS TOOL UNFOLLOW INSTAGRAM\033[1;93m >  \033[1;91m 
 --------------------------
\033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTELE   : @B_1_2_4
\033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTELE CH     : BESTxHACKER
\033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTELE GP  : BESTxHACKERx      

                                                                        """
print(L20)
def L455():
    global a,z,t
    user = input(A+"("+E+"⌯"+A+") "+H+ "Enter Your username"+A+':\n'+C)
    passs = input(A+"("+E+"⌯"+A+") "+H+ "Enter Your Passowrd"+A+':\n'+C)
    c ='https://www.instagram.com/accounts/login/ajax/'
    head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '336',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'x-asbd-id': '437806',
        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': 'caee87137ae9',
        'x-requested-with': 'XMLHttpRequest'
    }
    tim = str(time.time()).split('.')[1]
    data1 = {
        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passs}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'

    }
    rq = requests.post(c,headers=head1,data=data1)
    if ('"user":true,') and ('"authenticated":true,') in rq.text :

        co = rq.cookies
        coo =co.get_dict()
        tok = coo['csrftoken']
        cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
        
        url22 = f'https://www.instagram.com/{user}/?__a=1'
        head1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookiee,
            'referer': 'https://www.instagram.com/{}/'.format(user),
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-asbd-id': '437806',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
            'x-requested-with': 'XMLHttpRequest'
        }
        rr = r.get(url22,headers=head1).json()
        idd = str(rr['logging_page_id'])
        ss = idd.split('_')[1]
        
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(L20)
            L3653unf = int(input(A+"("+E+"⌯"+A+") "+H+ "Enter Your Number Your unfolling Accunts"+A+':\n'+C))
        except ValueError as error : 
            print('Plasss input Number.>!')
            exit()
        try:
            os.system('cls'if os.name=='nt' else'clear')
            print(L20)
            L3563sleep = int(input(A+"("+E+"⌯"+A+")"+B+ "Enter Your sleep unfooling "+A+':\n'+C))
        except ValueError as error : 
            print('Plasss input Number.>!')
            exit()
            
        

        url1 =f'https://i.instagram.com/api/v1/friendships/{ss}/following/?count={L3653unf}'
        head1 ={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookiee,
            'referer': 'https://www.instagram.com/7v.51/',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-asbd-id': '198387',
            
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKRG6',
            'x-requested-with': 'XMLHttpRequest'
        }
        data1 = {
            'count': L3653unf
            
        }
        req2 = r.get(url1,headers=head1,data=data1).json()
    

        for req1 in range(0,L3653unf):
            if req1 ==41417151988:
                print('Exit Tools .!')
                exit()
            

            login = str(req2['users'][req1]['pk'])
            url3 = f'https://www.instagram.com/web/friendships/{login}/unfollow/'
            head3 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookiee,
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{user}/following/',
                'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': generate_user_agent(),
                'x-asbd-id': '198387',
                'x-csrftoken': tok,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKRG6',
                'x-instagram-ajax': '640423fc30e1',
                'x-requested-with': 'XMLHttpRequest'
            }
            req3 = r.post(url3,headers=head3).text
            print(req3)
            if ('"status":"ok"') in req3:
                z+=1
                os.system('cls'if os.name=='nt' else'clear')
                print(L20)
                print(B+"┌────────────────────────┐ ")
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[32m Done unfooling'+H+':'+E+str(z))
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[31m Bad unfooling'+H+':'+A+str(a))
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[1;90m overall'+H+ ':'+B+str(a+z))
                print(B+"└────────────────────────┘ ")
                print(H+"Telegram  "+A+" : "+E+"@BESTxHACKER")
                sleep(L3563sleep)
            else:
                a+=1
                os.system('cls'if os.name=='nt' else'clear')
                print(L20)
                print(B+"┌────────────────────────┐ ")
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[32m Hit'+H+':'+E+str(z))
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[31m Bad'+H+':'+A+str(a))
                print('  ' '\033[1;91m(\033[1;92m⌯\033[1;91m)\033[1;90m Sum'+H+ ':'+B+str(a+z))
                print(B+"└────────────────────────┘ ")
                print(H+"Telegram  "+A+" : "+E+"@BESTxHACKER")
                exit()

L455()
