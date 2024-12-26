import os
import subprocess
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('AIzaSyA7xPz-EqDFk43IcORE2mat9s1IV0xx-Qw')

genai.configure(api_key='AIzaSyA7xPz-EqDFk43IcORE2mat9s1IV0xx-Qw')

model = genai.GenerativeModel('gemini-pro')


def generate_commit_message():
  git_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
  # Check if there's actual output before generating a message
  if git_changes.stdout:
    return model.generate_content('''You are an expert at creating a github commit message for a set of changes. Here is a diff of changes we need a commit message for:''' + str(git_changes))
  else:
    # Handle the case where there are no cached changes
    return "No changes detected. Skipping commit message generation."

if __name__ == '__main__':
  print(generate_commit_message().text)