import tinder_api as api
import config
import re
import time

fb_access_token = config.fb_access_token
fb_user_id = config.fb_user_id

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
print (fb_access_token)
print (fb_user_id)

tinder_auth_token = api.get_auth_token(fb_access_token, fb_user_id)
print (tinder_auth_token)
# print api.authverif(fb_access_token, fb_user_id)
# print api.get_self()


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

person_id=''
likes_remaining = 1

def likeAPerson():
    time.sleep(5)
    for key, value in api.get_recommendations().items():
        match = [];
        if(key == "results"):
            for person in value:
                rating = 0
                person_id = ""
                name = ""
                for key, value in person.items():
                    if(key == "_id"):
                        person_id = value
                        time.sleep(5)
                    if key == 'photos' and value:
                        if len(value) >= 2:
                            rating += 1
                    if key == 'name':
                        name = value

                if rating > 0:
                    print("Like on : ",name)
                    match = api.like(person_id)
                    likes_remaining = match["likes_remaining"]
                    if likes_remaining == 0:
                        print("Acabaram os likes, terminei por hoje")
                        quit(0)
                    print(match)
                else:
                    print("Unlike: ",name)


        

count = 10
while count > 0 and likes_remaining > 0:
    print ("count: ",count)
    likeAPerson()
    count -= 1


#matches = api.get_updates()['matches']
#
#with open('data.txt', 'w') as outfile:
#    json.dump(matches, outfile)

#ms = api.send_msg(config.match_id, config.msg)
#print (ms)
