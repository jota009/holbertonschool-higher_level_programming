# JavaScript DOM Manipulation Project

## 🌟 Project Overview

A hands‑on module on dynamic web development: using vanilla JavaScript to select, modify, and interact with HTML elements without reloading the page. Through eight tasks, you practiced element selection, event handling, class management, DOM creation/removal, and network requests via the Fetch API.

---

## 🎯 Learning Objectives

* **Element Selection:** `querySelector`, `querySelectorAll`, and differences between ID, class, and tag selectors.
* **Style & Content Update:** Inline styling (`.style`), class management (`.classList.add/remove/toggle`), and text manipulation (`.textContent`, `innerHTML`).
* **Event Handling:** Wiring user and browser events with `.addEventListener` (e.g., `click`, `DOMContentLoaded`).
* **Dynamic DOM Updates:** Creating (`createElement`), inserting (`appendChild`, `insertBefore`), and removing (`removeChild`) nodes.
* **Fetch API & Promises:** Performing GET and POST requests, parsing JSON, error handling, and using `async/await` alternatives.

---

## 🗂️ Tasks Covered

| Task | Description                                                                                       | Key Methods                          |
| :--: | :------------------------------------------------------------------------------------------------ | :----------------------------------- |
|   0  | Change header color on load (`<header>` → red)                                                    | `querySelector`, `.style.color`      |
|   1  | Change header color on click (ID selector)                                                        | `.addEventListener('click')`         |
|   2  | Add CSS class to header on click                                                                  | `.classList.add('red')`              |
|   3  | Toggle header between `.red` & `.green` on click                                                  | `.classList.contains` + `.replace`   |
|   4  | Append a new `<li>` (“Item”) to `<ul>` on click                                                   | `createElement`, `appendChild`       |
|   5  | Update `<header>` text to “New Header!!!” on click                                                | `.textContent`                       |
|   6  | Fetch a Star Wars character name and display in `<div id="character">`                            | `fetch()`, `.then()`, `.textContent` |
|   7  | Fetch all Star Wars films and list titles in `<ul id="list_movies">`                              | `fetch()`, loop + DOM insertion      |
|   8  | Fetch greeting from external API (`?lang=fr`) and insert into `<div id="hello">` when head‑loaded | `DOMContentLoaded`, `fetch()`        |

---

## 📁 Project Structure

```
javascript-dom_manipulation/
├─ 0-main.html        # Initial HTML skeletons for each task
├─ 0-script.js        # Task 0 implementation
├─ 1-script.js        # Task 1 implementation
├─ …                  # …
└─ 8-script.js        # Task 8 implementation (Fetch + DOMContentLoaded)
```

---

## 🛠 Key Concepts & Tips

* **Selector Precision:** Use `#id` when you need one element, `.class` for groups, and tags (`'header'`) for generic grabs.
* **Event Delegation:** Centralize listeners on parent nodes to handle many children.
* **Promise Chains vs. Async/Await:** Both achieve the same; `async/await` often yields clearer, linear code.
* **Error Handling:** Always check `response.ok` and implement `.catch()` to debug network issues.
* **Performance:** Minimize reflows by batching DOM updates and using DocumentFragments for large insertions.

---

## 🚀 Usage & Testing

1. **Open** each `*-main.html` in Chrome (v57+).
2. **Inspect** the console (F12) for errors and verify DOM updates visually.
3. **Refresh** after changes to re-run scripts.
4. **Optional:** Serve via `python3 -m http.server` for realistic HTTP behavior.

---

## 🙋‍♂️ Author

Josniel Ramos Diaz – JavaScript Enthusiast & Holberton School Student


