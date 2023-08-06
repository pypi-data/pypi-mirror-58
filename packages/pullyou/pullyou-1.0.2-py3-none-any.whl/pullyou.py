import argparse
import json
import re
import requests
import subprocess
import sys
import webbrowser
import os

def parser():
    parser = argparse.ArgumentParser(description='Open the PR associated with a given commit.')
    parser.add_argument('git_hash', help='the git hash you want to find the PR for')
    parser.add_argument('--repo', '-r', help='the repo to search for the PR in, defaults to the origin remote in the current directory.')

    return parser

def read_auth():
    cred_file = "~/.github_token"
    full_path = os.path.expanduser(cred_file)
    if not os.path.exists(full_path):
        return None

    with open(full_path) as f:
        creds = f.read().strip().split(":")
        if len(creds) != 2:
            print('Error: It appears your github access token file is not formatted correctly.')
            print('pullyou expects `username:token`')
            return None
        return (creds[0], creds[1])

# Searches the GitHub API for a PR that matches the given git hash and project
def search_for_hash(git_hash, git_repo):
    search_params = {'repo': git_repo}
    search_param_strings = []
    for key, value in search_params.items():
        search_param_strings.append(':'.join([key, value]))
    search_param_strings = [git_hash] + search_param_strings
    search = '+'.join(search_param_strings)

    query_params = {'q': search}
    pr_search_url = 'https://api.github.com/search/issues'

    github_auth = read_auth()

    http_response = requests.get(pr_search_url, params=query_params, auth=github_auth)

    code = http_response.status_code
    if code != 200:
        if code == 422:
            print(f'The git repo ({git_repo}) you have attempted to search for either does not exist on github or you do not have access to it.')
            print('To configure access, drop your username and a github personal access token in ~/.github_token')
            print('format: username:token')
            return None
        print(f"Received Error Code: {code}\n{http_response.text}")
        return None

    search_response = json.loads(http_response.text)

    found_count = search_response['total_count']
    if (found_count != 1):
        if found_count > 1:
            print(f'More than one PR matched for {git_hash}. More programming is required...')
        return None

    pull_request = search_response['items'][0]

    web_url = pull_request['html_url']
    return web_url


def current_repo():
    git_remote_args = ['git', 'remote', '-v']
    git_remote = subprocess.run(git_remote_args, capture_output=True)
    git_remote_out = git_remote.stdout.decode('utf-8')

    remote_url_regex = r'^origin\s+.*github\.com:([^.]*)(.git)?\s+\(fetch\)$'
    re_result = re.search(remote_url_regex, git_remote_out, flags=re.MULTILINE)

    if re_result is None:
        return None

    remote_url = re_result.group(1)
    return remote_url


# open_url opens the given url in the default browser
def open_url(url):
    webbrowser.open(url)


def main():
    args = parser().parse_args()
    if args.repo is None:
        args.repo = current_repo()
    if args.repo is None:
        print("No repo was specified, nor was one with a valid origin found in the current directory. Please specify with --repo or search from a git repo.")
        sys.exit(1)

    # 5bb3d053afcf0d83
    web_url = search_for_hash(args.git_hash, args.repo)
    if web_url is None:
        print('No PR found for the given hash.')
        sys.exit(1)

    # print(web_url)
    open_url(web_url)


if __name__ == '__main__':
    main()
