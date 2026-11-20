# 577E PYTHON BANKING & ATM MANAGEMENT SYSTEM

> **Fundamentals of Programming — Group 577E Collaborative Project**

<br>

## 1. PROJECT OVERVIEW

A console-based, multi-user banking and ATM simulation developed in Python. The system manages user authentication, account balances, daily transaction limits, commission calculations, shared ATM cash reserves, account-to-account transfers, and persistent file storage across program restarts.

<br>

---

<br>

## 2. TEAM MEMBERS & RESPONSIBILITIES

| Role | Student Name | Primary Modules & Responsibilities |
| :--- | :--- | :--- |
| **Member A** | **Nəzrin Kərimova** | Authentication, failed-attempt tracking, 60-second lockout timer, permanent card blocking, and password management. |
| | | |
| **Member B** | **Mehdi Məhərrəmli** | Account balances, daily deposit limit, cash withdrawals, 2% excess fee calculation, shared ATM reserve, and daily limits screen. |
| | | |
| **Member C** | **Akif Teymurov** | Account-to-account transfers, 5-transfer daily restriction, per-user transaction history, and persistent data storage. |

<br>

**Shared Responsibilities:** End-to-end integration testing, Git conflict resolution, Pull Request reviews, bug fixes, and documentation.

<br>

---

<br>

## 3. DEFAULT DEMONSTRATION ACCOUNTS

On the initial run, the application automatically generates the following three active accounts if no valid storage file is found:

| Username | Initial Password | Opening Balance | Account Status |
| :--- | :--- | :--- | :--- |
| **`user01`** | `Test@123` | `2,500.00 AZN` | Active |
| **`user02`** | `Test@456` | `1,500.00 AZN` | Active |
| **`user03`** | `Test@789` | `3,000.00 AZN` | Active |

<br>

---

<br>

## 4. FINANCIAL RULES & SYSTEM LIMITS

| Operation / Feature | Limit / Rule | Notes & Commission |
| :--- | :--- | :--- |
| **Temporary Lockout** | 3 failed login attempts | Disables login for **60 seconds** with a live countdown. |
| **Permanent Block** | 6 total failed attempts | Permanently blocks the card/account across restarts. |
| **Password Policy** | Min. 8 characters | Must include uppercase, lowercase, digit, and differ from old password. |
| **Daily Cash Deposit** | **2,000.00 AZN** / day | **0% commission**; increases both user balance and ATM cash. |
| **Fee-Free Withdrawal** | **500.00 AZN** / day | **0% commission** up to 500.00 AZN per calendar day. |
| **Excess Withdrawal Fee** | **2% commission** | Applied strictly to the portion exceeding 500.00 AZN. |
| **Hard Withdrawal Limit** | **1,000.00 AZN** / day | Maximum daily cash withdrawal cap per user. |
| **Shared ATM Reserve** | **5,000.00 AZN** initial | Shared across all users; unaffected by electronic transfers. |
| **Daily Transfers** | **5 transfers** / day | Maximum 5 successful outgoing transfers per calendar day. |

<br>

---

<br>

## 5. PROJECT DIRECTORY STRUCTURE

| File / Folder | Description |
| :--- | :--- |
| `main.py` | Entry point, interactive banking menu, and user session flow |
| `auth.py` | Login verification, lockout countdown, card blocking, and password change |
| `storage.py` | Persistent data loading, saving, and default state initialization |
| `transactions.py` | Deposits, withdrawals, commission logic, ATM reserve, and transfers |
| `data.json` | Persistent JSON storage file (auto-generated on first run) |
| `README.md` | Project documentation and team workflow guide |

<br>

---

<br>

## 6. GIT & GITHUB COLLABORATION WORKFLOW

| Branch | Purpose |
| :--- | :--- |
| `main` | Stable, production-ready version for final delivery. |
| `develop` | Shared integration branch where completed features are combined and tested. |
| `feature/*` | Individual feature branches (`feature/authentication`, `feature/storage`, etc.) merged into `develop` via reviewed Pull Requests. |

<br>

---

<br>

## 7. HOW TO RUN

1. Ensure **Python 3.8+** is installed on your computer.

2. Clone the repository and open the project directory:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-team-org>/577E-Python-Banking-System.git
   cd 577E-Python-Banking-System