import json
import maccli.helper.http
from maccli.config import RELEASE_ANY
from maccli.view.view_generic import show_error


def get_locations(provider):
    status_code, json, raw = maccli.helper.http.send_request("GET",
                                                             "/provider/locations?provider=%s" % (
                                                                 provider))

    return status_code, json


def get_hardwares(provider, location, release):

    if release is None or release == "":
        release = RELEASE_ANY

    status_code, json, raw = maccli.helper.http.send_request("GET",
                                                             "/provider/hardware?provider=%s&location=%s&release=%s" %
                                                             (provider, location, release))

    if status_code == 400:
        if raw == "No credentials available":
            print ("")
            print ("There is no credentials available in your account for the provider %s" % (provider))
            print ("")
            print (
                "Please login in your account in %s and deploy a production server using the supplier %s" % (
                    maccli.domain, provider))
            print ("")
            print ("You just need to make this action once.")
            print ("")

    return status_code, json


def credentials(provider, client, key):

    params = {
        'provider': provider,
        'client': client,
        'key': key
    }

    json_request = json.dumps(params)

    status_code, json_raw, raw = maccli.helper.http.send_request("POST", "/provider/credentials", data=json_request)

    if status_code == 400:
        show_error("Error while building request: " + raw)

    if status_code == 404:
        show_error("Error while building request: " + raw)

    if status_code == 401:
        show_error("Error while building request: " + raw)

    return status_code, json_raw
