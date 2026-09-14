# Updating an Existing Linear Issue

Fetch the current issue immediately before preparing an update. Treat its title, description, and metadata as the source
of truth; do not rely on an earlier copy when the live issue is available.

Compare the proposed revision with the current issue and preserve unrelated changes. If the live issue has changed since
the version used to prepare the revision, show the material differences and ask the user how to reconcile them before
writing the update.

Present the fields that will change when the effect is not already clear from the user's request. An explicit request to
apply a clear revision is sufficient authorization; ask for confirmation only when the update would overwrite conflicting
content or unresolved metadata could materially change the result.

After updating, fetch or inspect the issue again when possible and return its identifier and link.
