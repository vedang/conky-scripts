''''This piece o' junk hack of python and twitter was created by
 Travis Moore (@travist120). Some 17 year old kid who decided that he
 was severely bored one day and decided to create this instead of doing
 his Essay and french homework. 
'''





'''Oh, and the licence. I have to make sure that those who copy will 
give back.'''

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see 
.

'''

import os
import string
import twitter
#set your user name and password here.
username=''
password=''

api = twitter.Api(username, password)
status = api.GetFriendsTimeline()
#how many tweets you want displayed at a time
twitterSize = 3;
i = 0
for s in status:
	i = i+1
	print s.user.name, "(@"+s.user.screen_name+")"
	print s.text
	print
	if i == twitterSize:
		break
