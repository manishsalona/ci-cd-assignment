import requests

def check_new_commits(repo_owner, repo_name, last_commit_sha=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    params = {}
    if last_commit_sha:
        params["since"] = last_commit_sha

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

if __name__ == "__main__":
    repo_owner = "manishsalona"
    repo_name = "https://github.com/manishsalona/ci-cd-assignment.git"

    # Example usage
    commits = check_new_commits(repo_owner, repo_name)
    if commits:
        print(f"New commits found: {len(commits)}")
        for commit in commits:
            print(f"- Commit message: {commit['commit']['message']}")
    else:
        print("No new commits found.")
