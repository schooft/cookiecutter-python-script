#!/bin/bash
git init \
&& git config user.name "{{cookiecutter.author_name}}" \
&& git config user.email {{cookiecutter.author_email}} \
&& git add . \
&& git commit -m "Initial setup" \
&& git remote add origin git@github.com:{{cookiecutter.github_user}}/{{cookiecutter.project_name}}.git \
&& echo "TODO: Create new repository {{cookiecutter.github_user}}/{{cookiecutter.project_name}} on github at https://github.com/new" \
&& echo "TODO: Activate Travis CI Github App integration for this project" \
&& echo "TODO: Execute: git push -u origin master"

