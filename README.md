# Sieve Algorithms Test Repository

This repository demonstrates two classic prime number sieve algorithms and showcases Git's multiple ignore mechanisms as discussed in the Hacker News article: [.gitignore Isn't the Only Way To Ignore Files in Git](https://news.ycombinator.com/item?id=48583356)

## Algorithms Included

### 1. Sieve of Atkins (`sieve_atkins.py`)
A modern algorithm (2004) using quadratic forms to find primes efficiently.
- **Time Complexity:** O(n / log log n)
- **Focus:** This is the primary algorithm in this repository

### 2. Sieve of Eratosthenes (`sieve_eratosthenes.py`)
An ancient algorithm (~200 BCE) using iterative marking of multiples.
- **Time Complexity:** O(n log log n)
- **Note:** This file demonstrates local git ignore techniques

## Git Ignore Methods Demonstrated

This repository showcases the three levels of git ignore as discussed in the HN article:

### 1. `.gitignore` (Repository-level, tracked)
Standard method - files listed here are ignored for everyone who clones the repo.

### 2. `.git/info/exclude` (Repository-level, local only) ⭐
**The "special" method from the HN discussion!**

This file lives in `.git/info/exclude` and is **NOT** checked into git. It's perfect for:
- Ignoring files locally without affecting other collaborators
- Keeping personal test files out of git
- Experimenting without polluting `.gitignore`

**Example usage for this repo:**
```bash
# To locally ignore sieve_eratosthenes.py (keep focus on Atkins):
echo "sieve_eratosthenes.py" >> .git/info/exclude

# Verify it's ignored:
git check-ignore -v sieve_eratosthenes.py
# Output: .git/info/exclude:1:sieve_eratosthenes.py  sieve_eratosthenes.py

# The file is now ignored locally but still tracked in the remote!
# Other collaborators will still see it.
```

### 3. `~/.config/git/ignore` (Global, local only)
Global ignore file for your entire machine. Perfect for:
- `.DS_Store` (macOS)
- `*.swp` (vim)
- IDE-specific files

## Why Use `.git/info/exclude`?

From the HN article discussion, this is useful when:
- You want to ignore files **locally only**
- You don't want to modify the shared `.gitignore`
- You're testing/experimenting with files
- You have personal workflow files

**In this repository:**
- `sieve_atkins.py` - **Tracked** (main focus)
- `sieve_eratosthenes.py` - Can be **locally ignored** via `.git/info/exclude` to keep focus on Atkins

## Usage

### Run Sieve of Atkins:
```bash
python sieve_atkins.py
```

### Run Sieve of Eratosthenes:
```bash
python sieve_eratosthenes.py
```

### Compare Performance:
Both scripts include performance benchmarks for finding primes up to 1,000,000.

## Testing the Ignore Methods

```bash
# Clone the repository
git clone https://github.com/necat101/sieve-algorithms-test.git
cd sieve-algorithms-test

# Check current ignore status
git check-ignore -v sieve_eratosthenes.py
# (No output = not ignored)

# Add to local exclude (NOT tracked in git)
echo "sieve_eratosthenes.py" >> .git/info/exclude

# Verify it's now ignored locally
git check-ignore -v sieve_eratosthenes.py
# Output: .git/info/exclude:1:sieve_eratosthenes.py  sieve_eratosthenes.py

# Check git status - file appears as "deleted" in your working tree
# but this change is NOT tracked!
git status

# The .git/info/exclude file itself is never committed
# Other collaborators won't see your local ignore rules
```

## Key Takeaways from HN Discussion

1. **Three levels of ignoring**: `.gitignore` → `.git/info/exclude` → `~/.config/git/ignore`
2. **Use the right tool**: 
   - Shared ignores → `.gitignore`
   - Personal repo ignores → `.git/info/exclude`
   - Personal global ignores → `~/.config/git/ignore`
3. **`.git/info/exclude` is perfect** for keeping your local workspace clean without affecting others

## Repository Structure

```
sieve-algorithms-test/
├── sieve_atkins.py          # Main focus - tracked in git
├── sieve_eratosthenes.py    # Can be locally ignored via .git/info/exclude
├── README.md                # This file
└── .git/
    └── info/
        └── exclude          # Local ignore rules (not in repo)
```

## Learn More

- **HN Discussion:** https://news.ycombinator.com/item?id=48583356
- **Article:** https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/
- **Git Documentation:** `git help gitignore`

---

**Note:** This is a demonstration repository showing both sieve algorithms and git ignore techniques. The Sieve of Atkins is kept as the primary focus, while the Eratosthenes implementation can be locally ignored using `.git/info/exclude` as demonstrated above.
