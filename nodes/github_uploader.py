from nodes.github_push import push_code_to_github

def upload_files(files: list, commit_msg="Update code"):
    for file_path in files:
        push_code_to_github(file_path, commit_msg)