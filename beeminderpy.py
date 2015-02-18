import urllib
import urllib2
import settings

# based on https://www.beeminder.com/api

debug = True

class Beeminder:
    def __init__(self, this_auth_token=None):
        self.auth_token = this_auth_token
        self.base_url = 'https://www.beeminder.com/api/v1'

    def get_user(self, username=settings.BEEMINDER_USERNAME):
        if debug:
            print "get_user(username='%s')" % username

        url = "%s/users/%s.json" % (self.base_url, username)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def get_goal(self, username, goalname):
        if debug:
            print "get_goal(username='%s', goalname='%s')" % (username, goalname)

        url = "%s/users/%s/goals/%s.json" % (self.base_url, username, goalname)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def get_datapoints(self, username, goalname):
        if debug:
            print "get_datapoints(username='%s', goalname='%s')" % (username, goalname)

        url = self.base_url + 'users/' + username + '/goals/' + goalname + '/datapoints.json'
        url = "%s/users/%s/goals/%s/datapoints.json" % (self.base_url, username, goalname)
        values = {'auth_token': self.auth_token}
        result = self.call_api(url, values, 'GET')
        return result

    def create_datapoint(self, username, goalname, timestamp, value, comment=' ', sendmail='false'):
        if debug:
            print "create_datapoint(username='%s', goalname='%s', timestamp='%s', value='%s', comment='%s', sendmail='%s')" % (username, goalname, timestamp, value, comment, sendmail)

        url = self.base_url + 'users/' + username + '/goals/' + goalname + '/datapoints.json'
        url = "%s/users/%s/goals/%s/datapoints.json" % (self.base_url, username, goalname)
        values = {'auth_token': self.auth_token,
                  'timestamp': timestamp,
                  'value': value,
                  'comment': comment,
                  'sendmail': sendmail}
        result = self.call_api(url, values, 'POST')
        return result

    def call_api(self, url, values, method='GET'):
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
        return result
