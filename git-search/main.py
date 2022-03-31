import configparser
from git import Repo
import os

def main():
	print("HW")
	config = configparser.RawConfigParser(allow_no_value=True,interpolation=None,delimiters=('='))
	config.read('config.ini')

	#Method 1
	list_git_projects = config['git-projects']
	list_terms = config['terms-to-search']

	for git_projects in list_git_projects:
		print(git_projects)
		download_from_git(git_projects)

	for term in list_terms:
		search_for_string(term)


def search_for_string(keyword):
	path = './data'

	rootdir = ('./data')
	for folder, dirs, files in os.walk(rootdir):
		for file in files:
			try:
				fullpath = os.path.join(folder, file)
				with open(fullpath, 'r') as f:
					for line in f:
						if keyword in line:
							print(str(keyword) + ":" + str(fullpath))
							break
			except Exception as e:
				print(str(e))


def download_from_git(git_url):
	#Get project name from git_url
	user = git_url.split("/")[-2]
	project = git_url.split("/")[-1]

	all_repo_dir = "./data"
	dir = str(user) + "-" + str(project)

	repo_dir = all_repo_dir + "/" + dir
	print(repo_dir)
	#Create directory if not exists
	if not os.path.exists(repo_dir):
		os.makedirs(repo_dir)
		Repo.clone_from(git_url, repo_dir)

if __name__ == "__main__":
	main()