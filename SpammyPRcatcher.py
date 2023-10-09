import re

def is_spammy_pr(pr):
  """Returns True if the PR is spammy, False otherwise."""

  # Check for common spammy PR patterns
  if re.search(r'hacktoberfest', pr.title, re.IGNORECASE):
    return True
  if re.search(r't-shirt', pr.title, re.IGNORECASE):
    return True
  if re.search(r'giveaway', pr.title, re.IGNORECASE):
    return True
  if re.search(r'free', pr.title, re.IGNORECASE):
    return True

  # Check for PRs that are only trivial changes
  if len(pr.changes) == 1 and pr.changes[0].type == 'M':
    # The PR is only a modification to a single file
    if pr.changes[0].file.endswith('.md'):
      # The PR is a modification to a README file
      return True

  # The PR is not spammy
  return False

# Example usage:

prs = [
  # Spammy PR
  {
    "title": "Hacktoberfest: Add my name to the contributors list",
    "changes": [
      {
        "type": "M",
        "file": "README.md"
      }
    ]
  },
  # Not spammy PR
  {
    "title": "Fix typo in README.md",
    "changes": [
      {
        "type": "M",
        "file": "README.md"
      }
    ]
  }
]

for pr in prs:
  if is_spammy_pr(pr):
    print("Spammy PR:", pr["title"])
