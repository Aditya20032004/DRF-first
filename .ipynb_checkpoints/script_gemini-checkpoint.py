import os
import subprocess
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('AIzaSyA7xPz-EqDFk43IcORE2mat9s1IV0xx-Qw')

genai.configure(api_key='AIzaSyA7xPz-EqDFk43IcORE2mat9s1IV0xx-Qw')

model = genai.GenerativeModel('gemini-pro')


def generate_and_commit():
  git_changes = subprocess.run(["git", "diff"], capture_output=True, text=True)
  if git_changes.stdout:
    response = model.generate_content('''You are an expert at creating a github commit message for a set of changes. Here is a diff of changes we need a commit message for:''' + str(git_changes))
    commit_message = response.text  # Extract the text from the response
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message]) 
    print("Changes committed successfully!")
  else:
    print("No changes detected. Skipping commit message generation.")

if __name__ == '__main__':
  generate_and_commit()