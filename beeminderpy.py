import urllib
import urllib2
import settings
import json

# based on https://www.beeminder.com/api

debug = True

class Beeminder:
    def __init__(self, this_auth_token=settings.BEEMINDER_AUTH_TOKEN, username=settings.BEEMINDER_USERNAME, goalname=""):
        self.auth_token = this_auth_token
        self.username = username
        self.goalname = goalname
        self.base_url = 'https://www.beeminder.com/api/v1'

    def get_user(self):
        """Return user data JSON->Dict.
        """

        if debug:
            print "get_user()"

        url = "%s/users/%s.json" % (self.base_url, self.username)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def get_goal(self):
        """Return goal JSON->Dict
        """

        if debug:
            print "get_goal(username='%s', goalname='%s')" % (self.username, self.goalname)

        url = "%s/users/%s/goals/%s.json" % (self.base_url, self.username, self.goalname)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def get_datapoints(self):
        """Return JSON->Dict
        """

        if debug:
            print "get_datapoints()"

        url = self.base_url + 'users/' + self.username + '/goals/' + self.goalname + '/datapoints.json'
        url = "%s/users/%s/goals/%s/datapoints.json" % (self.base_url, self.username, self.goalname)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def create_datapoint(self, timestamp, value, comment=' ', sendmail='false'):
        """Return
        """

        if debug:
            print "create_datapoint(timestamp='%s', value='%s', comment='%s', sendmail='%s')" % (timestamp, value, comment, sendmail)

        url = self.base_url + 'users/' + self.username + '/goals/' + self.goalname + '/datapoints.json'
        url = "%s/users/%s/goals/%s/datapoints.json" % (self.base_url, self.username, self.goalname)
        values = {'auth_token': self.auth_token,
                  'timestamp': timestamp,
                  'value': value,
                  'comment': comment,
                  'sendmail': sendmail}
        result = self.call_api(url, values, 'POST')
        return result

    def call_api(self, url, values, method='GET'):
        """Return
        """

        if debug:
            print "call_api(url='%s', values='%s', method='%s')" % (url, values, method)

        result = ''
        data = urllib.urlencode(values)

        if method == 'POST':
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
        else:
            response = urllib2.urlopen(url + '?' + data)
        result = response.read()
        result_dict = json.loads(result)
        return result_dict
