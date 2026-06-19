# Git Ignore Methods - Implementation Guide

This document demonstrates the "special Hacker News method" for ignoring files in Git without using `.gitignore`, as discussed in: https://news.ycombinator.com/item?id=48583356

## The Three Levels of Git Ignore

### 1. `.gitignore` (Shared)
- Checked into repository
- Affects all collaborators
- Use for: build artifacts, dependencies, OS files

### 2. `.git/info/exclude` (Local, per-repo) ⭐
- **NOT checked into git**
- Local to your clone only
- Perfect for personal workflow files
- **This is the "special" method from HN!**

### 3. `~/.config/git/ignore` (Global, local only)
- Applies to ALL repositories on your machine
- Never checked into git
- Perfect for OS files (.DS_Store), editor files (*.swp)

## Implementation in This Repository

This repo demonstrates ignoring `sieve_eratosthenes.py` locally while keeping `sieve_atkins.py` as the main focus.

### Method 1: For Untracked Files

```bash
# Add to .git/info/exclude (local only, not tracked)
echo "my-personal-notes.txt" >> .git/info/exclude

# Verify
git check-ignore -v my-personal-notes.txt
# Output: .git/info/exclude:1:my-personal-notes.txt  my-personal-notes.txt
```

### Method 2: For Already-Tracked Files

Since `sieve_eratosthenes.py` is already tracked, `.git/info/exclude` won't work. Use:

```bash
# Tell git to ignore local changes to tracked file
git update-index --skip-worktree sieve_eratosthenes.py

# Verify it's being skipped
git ls-files -v | grep ^S
# Output: S sieve_eratosthenes.py
# The 'S' means skip-worktree is active

# Now you can modify the file locally and git won't show it in status
echo "# My local changes" >> sieve_eratosthenes.py
git status
# File does NOT appear in status!
```

### To Undo:

```bash
# Stop skipping the file
git update-index --no-skip-worktree sieve_eratosthenes.py

# Or to see what you're skipping:
git ls-files -v | grep ^S
```

## Why This Matters

**Scenario:** You're working on a project with both `sieve_atkins.py` and `sieve_eratosthenes.py`, but you want to:
- Keep `sieve_atkins.py` as your main focus (tracked normally)
- Experiment with `sieve_eratosthenes.py` locally without committing changes
- Not affect other collaborators
- Not modify the shared `.gitignore`

**Solution:** Use the HN methods:
1. `.git/info/exclude` for files not yet tracked
2. `git update-index --skip-worktree` for files already tracked

Both keep your local workflow clean without polluting the shared repository!

## Verification Commands

```bash
# Check which ignore file is affecting a path
git check-ignore -v <filename>

# List files with skip-worktree enabled
git ls-files -v | grep ^S

# List files with assume-unchanged enabled  
git ls-files -v | grep ^h

# See what's in your local exclude file
cat .git/info/exclude

# See what's in your global ignore file
cat ~/.config/git/ignore
```

## Key Differences

| Method | Tracked in Git? | Scope | Use Case |
|--------|----------------|-------|----------|
| `.gitignore` | Yes | Repository | Shared ignores (build/, node_modules/) |
| `.git/info/exclude` | No | Single clone | Personal files (notes.txt) |
| `~/.config/git/ignore` | No | All repos on machine | OS files (.DS_Store) |
| `skip-worktree` | No | Single file | Ignore local changes to tracked files |

## References

- **HN Discussion:** https://news.ycombinator.com/item?id=48583356
- **Article:** https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/
- **Git Docs:** `man gitignore` and `man git-update-index`
