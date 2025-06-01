import React, { useState } from "react";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  // Handle adding a new task
  const handleAddTask = (e) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed) return;
    setTasks([...tasks, { id: Date.now(), text: trimmed, completed: false }]);
    setInput("");
  };

  // Handle toggling task completion
  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  // Handle deleting a task
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  return (
    <div
      style={{
        maxWidth: 400,
        margin: "40px auto",
        padding: 24,
        border: "1px solid #ddd",
        borderRadius: 8,
        boxShadow: "0 2px 8px #f0f0f0",
      }}
    >
      <h2 style={{ textAlign: "center" }}>TODO List</h2>
      <form onSubmit={handleAddTask} style={{ display: "flex", gap: 8 }}>
        <input
          style={{
            flex: 1,
            padding: 8,
            border: "1px solid #ccc",
            borderRadius: 4,
          }}
          type="text"
          placeholder="Add a task..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          type="submit"
          style={{
            padding: "8px 16px",
            border: "none",
            background: "#2d7ff9",
            color: "white",
            borderRadius: 4,
            cursor: "pointer",
          }}
        >
          Add
        </button>
      </form>

      <ul
        style={{
          listStyle: "none",
          padding: 0,
          marginTop: 20,
        }}
      >
        {tasks.length === 0 && (
          <li style={{ color: "#aaa", textAlign: "center" }}>No tasks yet.</li>
        )}
        {tasks.map((task) => (
          <li
            key={task.id}
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              padding: "8px 0",
              borderBottom: "1px solid #f0f0f0",
            }}
          >
            <span
              onClick={() => toggleTask(task.id)}
              style={{
                flex: 1,
                cursor: "pointer",
                textDecoration: task.completed ? "line-through" : "none",
                color: task.completed ? "#aaa" : "inherit",
              }}
              title="Mark as completed"
            >
              {task.text}
            </span>
            <button
              aria-label="Delete"
              onClick={() => deleteTask(task.id)}
              style={{
                marginLeft: 12,
                background: "transparent",
                border: "none",
                color: "#ff6565",
                fontWeight: "bold",
                fontSize: 18,
                cursor: "pointer",
              }}
              title="Delete task"
            >
              &times;
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
