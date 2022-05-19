from gql.transport.requests import RequestsHTTPTransport
from django.contrib.auth.models import User
from gql import gql, Client
from datetime import datetime
import calendar

from . import models

# API constants
API_KEY = 'KXfzN0UTapfsP7jWc9wlPoKpMPsbKFq_7TfdmnD0Ym0GDxvQNFEagIgPVyIanjpgFuEs3FoMYKTeZLnBjT7G6QzYniRpsASPBiOP2Gh0jd3eUxKgXsVQCtqn5fUnYnYx' # YELP API Bearer key
def get_response():
  HEADER = {'Authorization': 'bearer %s' % API_KEY}
  # Build the request framework
  transport = RequestsHTTPTransport(url='https://api.yelp.com/v3/graphql', headers=HEADER, use_json=True)
  # Create the client
  client = Client(transport=transport, fetch_schema_from_transport=True)
  # define a simple query
  query = gql(''' 
  {
    search(term:"downtown",
          location:"Chico, 95928",
          categories:"restaurants") {
      total
      business {
        name
        hours {
          is_open_now
          open {
            start
            end
            day
          }
        }
        photos
        rating
        price
        location {
          formatted_address
        }
        display_phone
      }
    }
  }
  ''')
  response_q = client.execute(query)
  for i in range(0,20):
    if response_q['search']['business'][i]['hours']:
      start_hours = response_q['search']['business'][i]['hours'][0]['open'] # change [] before start to have 1-4 or however many values
      for c, start in enumerate(start_hours):
        change_start = datetime.strptime(start['start'], '%H%M').strftime('%I:%M %p')
        change_end = datetime.strptime(start['end'], '%H%M').strftime('%I:%M %p')
        change_day = calendar.day_abbr[start['day']]
        response_q['search']['business'][i]['hours'][0]['open'][c]['start'] = change_start
        response_q['search']['business'][i]['hours'][0]['open'][c]['end'] = change_end
        response_q['search']['business'][i]['hours'][0]['open'][c]['day'] = change_day

  # rest_name = []
  # tup_name = []
  # for response in response_q['search']['business'][0:20]:
  #   rest_name.append(response['name'])
  # tup_name = [tuple([x,x]) for x in rest_name]
  # print(tup_name[0][0])
  return response_q['search']['business'][0:20]

def get_rest_name():
  response_q = get_response()
  rest_name = []
  for response in response_q:
    rest_name.append(response['name'])

  return rest_name

def get_usernames():
  usernames =  User.objects.all()
  user_list = []
  for user in usernames:
    user_list.append(user)

  return user_list