import os
import openai
import subprocess
from dotenv import load_dotenv
import time
import webbrowser

load_dotenv()

client = openai.OpenAI()


def generate_code(prompt):
    # You can replace 'gpt-4' with 'gpt-3.5-turbo' or Codex if you prefer
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a coding assistant. Generate React component code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content


def create_react_app(app_name):
    # print(f"Creating React app: {app_name}")
    # subprocess.run(["npx", "create-react-app", shell=True, app_name])
    # subprocess.run("npx create-react-app {app_name}", shell=True, check=True)

    # Step 1: Initialize Vite project
    print("🔨 Initializing React project with Vite...")

    subprocess.run(
        f"npx create-vite {app_name} --template react", shell=True, check=True)

    os.chdir(app_name)

    # Step 2: Install dependencies
    print("📦 Installing dependencies...")

    subprocess.run("npm install", shell=True, check=True)

    # Start the dev server
    subprocess.Popen("npm run dev", shell=True)

    # Wait a few seconds for server to start
    time.sleep(5)

    # # Open browser to localhost:5173 (default Vite port)
    webbrowser.open("http://localhost:5173")


def update_file(file_path, new_code):
    with open(file_path, 'w') as f:
        f.write(new_code)
    print(f"Updated {file_path}")


def main():
    app_name = "my-todo-app"
    if not os.path.exists(app_name):
        create_react_app(app_name)

    while True:
        user_input = input(
            "Describe the feature/update you want in the React app:\n")
        if user_input.lower() in ["exit", "quit"]:
            break

        target_file = input(
            "Which file do you want to update? (e.g., src/App.js)\n")
        prompt = f"Update the React to-do app with this feature: {user_input}. Here is the current content of {target_file}:\n"
        # file_path = os.path.join(app_name, target_file)
        # if not os.path.exists(file_path):
        #     print(
        #         f"❌ The file {file_path} does not exist. Please check the path.")
        #     continue

        with open(os.path.join(app_name, target_file), 'r') as f:
            existing_code = f.read()

        # prompt = f"Update the React to-do app with this feature: {user_input}. Here is the current content of {target_file}:\n"

        full_prompt = prompt + existing_code
        updated_code = generate_code(full_prompt)

        update_file(os.path.join(app_name, target_file), updated_code)
        print(f"Feature '{user_input}' applied to {target_file}.\n")


if __name__ == "__main__":
    main()
