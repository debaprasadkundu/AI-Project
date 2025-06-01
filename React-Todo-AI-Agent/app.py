import os
import subprocess
import openai
from dotenv import load_dotenv
import time
import webbrowser

load_dotenv()

client = openai.OpenAI()


def generate_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def create_react_todo_project():
    project_name = "react-todo-app"

    # Step 1: Initialize Vite project
    print("🔨 Initializing React project with Vite...")

    subprocess.run(
        f"npx create-vite {project_name} --template react", shell=True, check=True)

    os.chdir(project_name)

    # Step 2: Install dependencies
    print("📦 Installing dependencies...")

    subprocess.run("npm install", shell=True, check=True)

    # Step 3: Generate App.jsx
    print("✨ Generating App.jsx...")
    app_code = generate_code(
        "Write a complete React App.jsx file for a TODO list app with features to add, delete, and mark tasks as completed. Use React hooks and keep styling minimal."
    )
    with open("src/App.jsx", "w", encoding='utf-8') as f:
        f.write(app_code.rstrip())

    # Step 4: Generate main.jsx(entry point)
    # print("🚀 Generating main.jsx...")
    # main_code = generate_code(
    #     "Write a main.jsx file for a React project created with Vite that renders the App component into the root div."
    # )
    # with open("src/main.jsx", "w", encoding='utf-8') as f:
    #     f.write(main_code.rstrip())

    # Step 5: Generate index.css(optional)
    print("🎨 Generating index.css...")
    css_code = generate_code(
        "Write a minimal index.css file with simple styling for a TODO app. Use modern CSS."
    )
    with open("src/index.css", "w", encoding='utf-8') as f:
        f.write(css_code.rstrip())

    print(f"✅ React TODO app generated successfully in {os.getcwd()}!")

    print("🚀 Launching the React app...")

    # Start the dev server
    process = subprocess.Popen("npm run dev", shell=True)

    # Wait a few seconds for server to start
    time.sleep(5)

    # Open browser to localhost:5173 (default Vite port)
    webbrowser.open("http://localhost:5173")

    # Optional: Keep the Python script running until dev server is stopped
    process.wait()


if __name__ == "__main__":
    create_react_todo_project()
