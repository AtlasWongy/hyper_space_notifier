import requests
import json

def post_request_hyper_space():

    # Perform the API request
    url = "https://beta.api.solanalysis.com/graphql"

    payload = json.dumps({
    "operationName": "GetProjectMPAHistory",
    "variables": {
        "condition": {
        "projects": [
            {
            "project_id": "rascals"
            }
        ],
        "by_mpa_types": [
            "LISTING"
        ]
        },
        "pagination_info": {
        "page_number": 1,
        "page_size": 30,
        "progressive_load": True
        }
    },
    "query": "query GetProjectMPAHistory($condition: GetMarketPlaceActionsByProjectsCondition!, $pagination_info: MPAPaginationConfig) {\n  getProjectHistory(condition: $condition, pagination_info: $pagination_info) {\n    market_place_snapshots {\n      token_address\n      project_id\n      project_name\n      name\n      owner\n      full_img\n      rank_est\n      moonrank\n      howrare_rank\n      meta_data_img\n      market_place_state {\n        marketplace_program_id\n        marketplace_instance_id\n        type\n        price\n        block_timestamp\n        seller_address\n        currency\n        currency_price\n        decimal\n        seller_referral_address\n        seller_referral_fee\n        signature\n        escrow_address\n        buyer_address\n        buyer_referral_address\n        buyer_referral_fee\n        created_at\n        metadata\n        token_address\n        __typename\n      }\n      __typename\n    }\n    pagination_info {\n      current_page_number\n      current_page_size\n      has_next_page\n      __typename\n    }\n    __typename\n  }\n}"
    })
    headers = {
    'authority': 'beta.api.solanalysis.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://hyperspace.xyz',
    'referer': 'https://hyperspace.xyz/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response
