# Sieve Algorithms Test Repository

This repository demonstrates two classic prime number sieve algorithms and showcases Git's multiple ignore mechanisms as discussed in the Hacker News article: [.gitignore Isn't the Only Way To Ignore Files in Git](https://news.ycombinator.com/item?id=48583356)

**⚠️ Important Correction:** `.git/info/exclude` only works for **untracked** files. For files already tracked by git (like the ones in this repo), use `git update-index --skip-worktree` instead. See below for details.

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

This repository showcases Git's ignore mechanisms with **corrected explanations**:

### 1. `.gitignore` (Repository-level, tracked)
Standard method - files listed here are ignored for everyone who clones the repo.
- ✅ Works for untracked files
- ✅ Shared with team
- ❌ Cannot ignore changes to tracked files

### 2. `.git/info/exclude` (Repository-level, local only)
**From the HN discussion - but with important caveat!**

This file lives in `.git/info/exclude` and is **NOT** checked into git.

**⚠️ CRITICAL LIMITATION:** Only works for **UNTRACKED** files!
- ✅ Prevents `git add .` from staging new files
- ✅ Local to your clone only
- ❌ **Does NOT hide changes to files already tracked by git**
- ❌ If file is already in repo, adding to exclude does nothing

**Example that WORKS:**
```bash
# For a NEW file not yet in git:
echo "my-local-notes.txt" >> .git/info/exclude
touch my-local-notes.txt
git status
# File is ignored! Won't show up
```

**Example that DOESN'T WORK:**
```bash
# For a file ALREADY tracked (like sieve_eratosthenes.py):
echo "sieve_eratosthenes.py" >> .git/info/exclude
# Modify the file...
echo "# change" >> sieve_eratosthenes.py
git status
# File STILL SHOWS UP! Exclude doesn't work for tracked files
```

### 3. `git update-index --skip-worktree` (For Tracked Files) ⭐

**This is what you actually need for tracked files!**

```bash
# Hide local changes to a tracked file:
git update-index --skip-worktree sieve_eratosthenes.py

# Verify it's active:
git ls-files -v | grep ^S
# Output: S sieve_eratosthenes.py

# Now modify the file:
echo "# local change" >> sieve_eratosthenes.py
git status
# File does NOT appear! Changes are hidden locally

# To undo:
git update-index --no-skip-worktree sieve_eratosthenes.py
```

### 4. `~/.config/git/ignore` (Global, local only)
Global ignore file for your entire machine.

## The Correct Approach for This Repository

**Goal:** Keep focus on `sieve_atkins.py` while making local experimental changes to `sieve_eratosthenes.py` without committing them.

**Solution:** Since both files are already tracked, use `skip-worktree`, NOT `.git/info/exclude`:

```bash
# Clone the repository
git clone https://github.com/necat101/sieve-algorithms-test.git
cd sieve-algorithms-test

# Apply skip-worktree to the file you want to ignore locally
git update-index --skip-worktree sieve_eratosthenes.py

# Verify it's active
git ls-files -v | grep sieve
# H sieve_atkins.py         # H = tracked normally
# S sieve_eratosthenes.py   # S = skip-worktree enabled

# Now you can modify sieve_eratosthenes.py freely
# Git will ignore your local changes!
echo "# My experimental changes" >> sieve_eratosthenes.py
git status
# sieve_eratosthenes.py does NOT appear!

# Your changes are hidden locally but the file remains
# tracked in the remote repository for others
```

## Summary Table

| Method | Tracked in Git? | Works for Untracked Files? | Works for Tracked Files? | Use Case |
|--------|----------------|----------------------------|--------------------------|----------|
| `.gitignore` | Yes | ✅ Yes | ❌ No | Shared ignores |
| `.git/info/exclude` | No | ✅ Yes | ❌ No | Personal ignores for new files |
| `git update-index --skip-worktree` | No | ❌ No | ✅ Yes | Hide local changes to tracked files |
| `~/.config/git/ignore` | No | ✅ Yes | ❌ No | Global personal ignores |

## Key Takeaways from HN Discussion

1. **`.git/info/exclude` is NOT a replacement for `.gitignore`** - it only works for untracked files
2. **For tracked files, use `git update-index --skip-worktree`** - this is the actual solution for hiding local changes
3. **Choose the right tool:**
   - New files you never want to commit → `.git/info/exclude` or `.gitignore`
   - Existing tracked files with local modifications → `git update-index --skip-worktree`

## Testing the Methods

```bash
# Test 1: .git/info/exclude with untracked file
touch test-untracked.txt
echo "test-untracked.txt" >> .git/info/exclude
git status
# File does NOT appear - SUCCESS!

# Test 2: .git/info/exclude with tracked file (WILL FAIL)
echo "sieve_atkins.py" >> .git/info/exclude
echo "# test" >> sieve_atkins.py
git status
# File DOES appear - exclude doesn't work for tracked files!

# Test 3: skip-worktree with tracked file
git update-index --skip-worktree sieve_atkins.py
git status
# File does NOT appear - SUCCESS!
```

## Learn More

- **HN Discussion:** https://news.ycombinator.com/item?id=48583356
- **Article:** https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/
- **Git Docs:** `man git-update-index`

---

**Correction Note:** An earlier version of this README incorrectly suggested `.git/info/exclude` could hide changes to tracked files. This has been corrected - you must use `git update-index --skip-worktree` for that purpose. Thanks to the HN community for the clarification!
