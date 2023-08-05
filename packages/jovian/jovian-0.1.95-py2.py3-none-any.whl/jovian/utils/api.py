from jovian._version import __version__
from jovian.utils.credentials import get_api_key, get_guest_key, read_api_url, read_org_id
from jovian.utils.error import ApiError
from jovian.utils.logger import log
from jovian.utils.misc import timestamp_ms
from jovian.utils.request import get, post, pretty
from jovian.utils.url import urljoin


def _u(path):
    """Make a URL from the path"""
    return urljoin(read_api_url(), path)


def _h():
    """Create authorization header with API key"""
    return {"Authorization": "Bearer " + get_api_key(),
            "x-jovian-source": "library",
            "x-jovian-library-version": __version__,
            "x-jovian-guest": get_guest_key(),
            "x-jovian-org": read_org_id()}


def _v(version):
    """Create version query parameter string"""
    if version is not None:
        return "?gist_version=" + str(version)
    return ""


def get_gist(slug, version=None):
    """Get the metadata for a gist"""
    if '/' in slug:
        parts = slug.split('/')
        username, title = parts[0], parts[1]
        url = _u('user/' + username + '/gist/' + title + _v(version))
    else:
        url = _u('gist/' + slug + _v(version))
    res = get(url=url, headers=_h())
    if res.status_code == 200:
        return res.json()['data']
    raise Exception('Failed to retrieve metadata for notebook "' +
                    slug + '": ' + pretty(res))


def get_gist_access(slug):
    """Get the access permission of a gist"""
    res = get(url=_u('/gist/' + slug + '/check-access'), headers=_h())
    if res.status_code == 200:
        return res.json()['data']
    raise Exception('Failed to retrieve access permission for notebook "' +
                    slug + '" (retry with create_new=True to create a new notebook): ' + pretty(res))


def create_gist_simple(filename=None, gist_slug=None, secret=False):
    """Upload the current notebook to create a gist"""
    auth_headers = _h()

    with open(filename, 'rb') as f:
        nb_file = (filename, f)
        log('Uploading notebook..')
        if gist_slug:
            return upload_file(gist_slug=gist_slug, file=nb_file)
        else:
            res = post(url=_u('/gist/create'),
                       data={'public': 0 if secret else 1},
                       files={'files': nb_file},
                       headers=auth_headers)
            if res.status_code == 200:
                return res.json()['data']
            raise ApiError('File upload failed: ' + pretty(res))


def upload_file(gist_slug, file, folder=None, version=None, artifact=False):
    """Upload an additional file to a gist"""
    data = {'artifact': 'true'} if artifact else {}
    if folder:
        data['folder'] = folder

    res = post(url=_u('/gist/' + gist_slug + '/upload' + _v(version)),
               files={'files': file}, data=data, headers=_h())
    if res.status_code == 200:
        return res.json()['data']
    raise ApiError('File upload failed: ' + pretty(res))


def post_blocks(blocks, version=None):
    url = _u('/data/record' + _v(version))
    res = post(url, json=blocks, headers=_h())
    if res.status_code == 200:
        return res.json()['data']
    else:
        raise ApiError('Data logging failed: ' + pretty(res))


def post_block(data, data_type, version=None):
    """Upload metrics, hyperparameters and other information to server"""
    blocks = [{"localTimestamp": timestamp_ms(),
               "data": data,
               'recordType': data_type}]
    return post_blocks(blocks, version)


def commit_records(gist_slug, tracking_slugs, version=None):
    """Associated tracked records with a commit"""
    url = _u('/data/' + gist_slug + '/commit' + _v(version))
    res = post(url, json=tracking_slugs, headers=_h())
    if res.status_code == 200:
        return res.json()['data']
    else:
        raise ApiError('Data logging failed: ' + pretty(res))


def post_slack_message(data, safe=False):
    """Push data to Slack, if slack is integrated with jovian account"""
    url = _u('/slack/notify')
    res = post(url, json=data, headers=_h())
    if res.status_code == 200:
        return res.json()
    elif safe:
        return {'data': {'messageSent': False}}
    else:
        raise ApiError('Slack trigger failed: ' + pretty(res))
