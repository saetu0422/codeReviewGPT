import requests
import json
import mykey

# GitHub Personal Access Token
GITHUB_TOKEN = mykey.github_api

# 리포지토리 정보
OWNER = 'repository_owner'
REPO = 'repository_name'

# 헤더 설정
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github+json'
}

# 1. 코드 스캐닝 경고 목록 가져오기
def get_code_scanning_alerts():
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/code-scanning/alerts'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        alerts = response.json()
        for alert in alerts:
            print(f"Alert ID: {alert['number']}, State: {alert['state']}, Rule: {alert['rule']['description']}")
    else:
        print(f"Failed to fetch alerts: {response.status_code}")

# 2. 특정 경고 상세 정보 가져오기
def get_code_scanning_alert(alert_number):
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/code-scanning/alerts/{alert_number}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        alert = response.json()
        print(json.dumps(alert, indent=2))
    else:
        print(f"Failed to fetch alert: {response.status_code}")

# 함수 실행 예시
if __name__ == '__main__':
    get_code_scanning_alerts()
    # 특정 경고 상세 정보 가져오기
    # get_code_scanning_alert(1)