from flask import Flask, render_template, redirect, request, url_for
import os
import requests
import json

app = Flask(__name__)
pc_base_url = "https://api.eu.prismacloud.io"
pc_access_key = os.environ.get('PC_KEY')
pc_secret_key = os.environ.get('PC_SECRET')


@app.route("/")
@app.route("/list-compliance-frameworks")
def list_compliance_frameworks():
    url = pc_base_url + "/compliance"
    pc_session_token = prisma_cloud_get_token()

    payload = {}
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
        'x-redlock-auth': pc_session_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = response.json()
    # print(resp_json)

    return render_template('compliance.html', results=resp_json)


@app.route("/list-compliance-reqs/<request_framework>/<comp_id>")
def list_compliance_reqs(comp_id, request_framework='NotCaught'):
    url = pc_base_url + "/compliance/" + comp_id + "/requirement"
    pc_session_token = prisma_cloud_get_token()

    payload = {}
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
        'x-redlock-auth': pc_session_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = response.json()
    # print(resp_json)

    return render_template('compliance-reqs.html', results=resp_json, request_framework=request_framework)


@app.route("/list-compliance-req-section/<request_requirement>/<req_id>")
def list_compliance_req_sections(req_id, request_requirement='NotCaught'):
    url = pc_base_url + "/compliance/" + req_id + "/section"
    pc_session_token = prisma_cloud_get_token()

    payload = {}
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
        'x-redlock-auth': pc_session_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = response.json()
    # print(resp_json)

    return render_template('compliance-req-sections.html', results=resp_json, request_requirement=request_requirement)


@app.route("/list-policies-per-section/<request_requirement>/<sec_id>")
def list_policies_per_section(sec_id, request_requirement='NotCaught'):
    url = pc_base_url + "/v2/policy?policy.complianceSection=" + sec_id
    pc_session_token = prisma_cloud_get_token()

    payload = {}
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
        'x-redlock-auth': pc_session_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = response.json()
    # print(resp_json)

    return render_template('policies-per-section.html', results=resp_json, sec_id=sec_id,
                           request_requirement=request_requirement)


@app.route("/get-policy-detail/<policy_id>")
def get_policy_detail(policy_id):
    url = pc_base_url + "/policy/" + policy_id
    pc_session_token = prisma_cloud_get_token()

    payload = {}
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
        'x-redlock-auth': pc_session_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = response.json()
    # print(resp_json)

    return render_template('policy-detail.html', results=resp_json)


#### Utility Functions ####

# Log in with access and secret key to get session token used in subsequent requests
def prisma_cloud_get_token():
    url = pc_base_url + "/login"

    payload = json.dumps({
        "username": pc_access_key,
        "password": pc_secret_key
    })
    headers = {
        'accept': 'application/json; charset=UTF-8',
        'content-type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resp_json = response.json()
    return resp_json['token']
    # pc_session_token = resp_json['token']
    # print(pc_session_token)
    # print(response.text)


app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
