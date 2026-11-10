# Bharadwaj Classes

<p align="center">
  <a href="Bharadwaj_Classes%20Demo.mp4">
    <img src="img/Bharadwaj_Classes%20Demo%20thumbnail.png" alt="Watch the Bharadwaj_Classes demo video" width="720">
  </a>
  <br>
  <sub>▶ <b><a href="Bharadwaj_Classes%20Demo.mp4">Watch the Bharadwaj_Classes demo</a></b> (74 s): the feature table and commits, the README quick start on a fresh clone, then both versions live: the Tkinter app from login to the QR payment, and the Bootstrap site in Chrome</sub>
</p>

**One coaching-centre experience built twice — as a Tkinter desktop app and as a responsive Bootstrap website.**

[![Python](https://img.shields.io/badge/Python-Tkinter-3776AB?logo=python&logoColor=white)](GUI.py)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-7952B3?logo=bootstrap&logoColor=white)](Bharadwaj%20Classes%20using%20Bootstrap/index.html)
[![HTML](https://img.shields.io/badge/HTML_·_CSS_·_JS-no_build_step-E34F26?logo=html5&logoColor=white)](Bharadwaj%20Classes%20using%20Bootstrap/)
[![Scope](https://img.shields.io/badge/scope-academic_·_portfolio-lightgrey)](#license)

For the fictional "Bharadwaj Classes": a student registers, logs in, picks a
course in one of three learning modes, and pays by QR code. The desktop version
came first; the website rebuilds the same workflow for the browser and adds the
things a public site needs.

---

## Contents

| Section | |
|---|---|
| [What it does](#what-it-does) | The two versions, side by side |
| [Architecture](#architecture) | Desktop flow and web page structure |
| [How a student enrols](#how-a-student-enrols) | Register, choose, pay |
| [Quick start](#quick-start) | Run the app, open the site |
| [Project status](#project-status) | What each version covers |
| [Design decisions](#design-decisions) | Why rebuild it for the web |
| [Repository layout](#repository-layout) | Where things live |
| [Team](#team) | Who built it |

---

## What it does

| Area | Tkinter app | Bootstrap website |
|---|---|---|
| **Accounts** | Login and registration with input validation (e.g. digits-only age) | Modal sign-up and an embedded Google Form |
| **Courses** | Course selection with details per language | Course cards for Virtual, Hybrid and In-Person modes, with pricing and benefits |
| **Payment** | QR-code payment confirmation | — |
| **Information** | — | Instructor cards, an FAQ accordion, a newsletter sign-up, a live Leaflet map |
| **Layout** | Fixed desktop window | Fully responsive, Bootstrap Icons |

<p align="center">
  <img src="img/gui.jpg" width="32%" alt="Tkinter GUI preview" />
  &nbsp;
  <img src="img/website.jpg" width="62%" alt="Website preview" />
</p>

---

## Architecture

```mermaid
graph LR
    subgraph desktop["GUI.py — Tkinter"]
        LOGIN["Login"] --> REG["Registration<br/>validated inputs"]
        REG --> COURSE["Course selection<br/>details per language"]
        COURSE --> PAY["Payment<br/>QR.png"]
    end

    subgraph web["index.html — Bootstrap 5"]
        HERO["Showcase"] --> MODES["Learning modes<br/>Virtual · Hybrid · In-Person"]
        MODES --> INSTR["Instructors"]
        INSTR --> FAQ["FAQ accordion"]
        FAQ --> FORM["Google Form · newsletter"]
        FORM --> MAP["Leaflet map"]
    end

    PAY -. "same workflow, rebuilt for the browser" .-> MODES
```

---

## How a student enrols

```mermaid
sequenceDiagram
    participant S as Student
    participant A as Tkinter app
    participant Q as QR payment

    S->>A: log in or register
    A->>A: validate the fields
    S->>A: choose a course
    A-->>S: course details
    S->>A: proceed to pay
    A->>Q: show QR.png
    Q-->>S: scan and pay
    A-->>S: confirmation (or an error if the QR image is missing)
```

---

## Quick start

```bash
# desktop app — Python 3 with Tkinter; run from the repo root so QR.png is found
python GUI.py

# website — no server or install
#   open "Bharadwaj Classes using Bootstrap/index.html" in a browser
```

---

## Project status

Both versions are complete for their scope. The website was added in July 2025,
eight months after the desktop app, as a rebuild of the same workflow.

| Version | Status |
|---|---|
| Tkinter desktop app | ✅ login, registration, course selection, QR payment |
| Bootstrap website | ✅ responsive landing site with forms, FAQ and map |

---

## Design decisions

**Rebuild, don't port.** The website keeps the desktop app's flow — choose a
mode, see what it costs, sign up — but uses the web's own patterns: modals,
accordions and an embedded form instead of extra windows.

**Static on purpose.** The site is plain HTML, CSS and Bootstrap from a CDN, so it
opens from the filesystem with nothing to install or host.

**Three learning modes.** Virtual, Hybrid and In-Person, each with its own price
and benefits, mirror how real coaching centres sell courses.

---

## Repository layout

```
.
├── GUI.py                                Tkinter desktop app
├── QR.png                                payment QR used by the app
├── Bharadwaj Classes using Bootstrap/
│   ├── index.html                        the website
│   ├── style.css
│   └── img/                              logo and illustrations
└── img/                                  screenshots for this README
```

---

## Team

| Member | Focus |
|---|---|
| **Guru R Bharadwaj** | Both versions — desktop app and website |

---

## License

Built for academic and portfolio purposes. The branding is fictional.
**Redistributing or presenting this project as your own is prohibited.**
